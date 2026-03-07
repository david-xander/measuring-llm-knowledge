import os
from openai import OpenAI
import pandas as pd
import json
import re
from abc import ABC, abstractmethod
from ollama import Client as OLlamaClient
from datetime import datetime
import time

class LLMPrompting(ABC):
    def __init__(self, model):
        self.model = model
        self.context = []
    
    def add_to_context(self, content):
        self.context.append({"role": "user", "content": content})

    def add_to_context_as_assistant(self, content):
        self.context.append({"role": "assistant", "content": content})

    def get_context(self):
        return self.context

    def clear_context(self):
        self.context = []

    def delete_last_prompt_from_context(self):
        self.context.pop()

    @abstractmethod
    def run_and_get_result(self, add_response_to_context=True, response_format=None):
        pass

class OpenAIPrompting(LLMPrompting):
    def __init__(self, model):
        super().__init__(model)
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(
            api_key=api_key
        )

    def run_and_get_result(self, add_response_to_context=True, response_format=None):
        try:
            kwargs = {
                "model": self.model,
                "messages": self.get_context(),
                # "temperature": 0.3,
            }

            if response_format is not None:
                kwargs["response_format"] = {
                    "type": "json_schema",
                    "json_schema": {
                        "name": response_format.get("title", "schema"),
                        "schema": response_format
                    }
                }

            chat_completion = self.client.chat.completions.create(**kwargs)
            response = chat_completion.choices[0].message.content

            if add_response_to_context:
                self.add_to_context_as_assistant(response)

            return response

        except Exception as e:
            print(f"Error while calling OpenAI API: {e}")
            return "Error generating code."


class AzureAIPrompting(LLMPrompting):
    def __init__(self, model):
        super().__init__(model)
        endpoint = os.getenv("AZUREAI_ENDPOINT_URL")
        api_key = os.getenv("AZUREAI_API_KEY")
        self.client = OpenAI(
            base_url=f"{endpoint}",
            api_key=api_key
        )

        # retry config
        self.base_delay = 8
        self.rate_limit_delay = 30
        self.max_retries = 5        

    def run_and_get_result(self, add_response_to_context=True, response_format=None):
        retries = 0

        kwargs = {
            "model": self.model,
            "messages": self.get_context(),
            "temperature": 0.3,
        }

        if response_format is not None:
            kwargs["response_format"] = {
                "type": "json_schema",
                "json_schema": {
                    "name": response_format.get("title", "schema"),
                    "schema": response_format
                }
            }

        while retries <= self.max_retries:
            try:
                # Baseline delay
                time.sleep(self.base_delay)

                chat_completion = self.client.chat.completions.create(**kwargs)
                response = chat_completion.choices[0].message.content

                if add_response_to_context:
                    self.add_to_context_as_assistant(response)

                return response

            except Exception as e:
                message = str(e).lower()
                status_code = getattr(e, "status_code", None)

                # Rate limit detection (Azure-style)
                if status_code == 429 or "rate limit" in message or "throttl" in message:
                    retries += 1
                    print(
                        f"Rate limit hit (retry {retries}/{self.max_retries}). "
                        f"Waiting {self.rate_limit_delay}s..."
                    )
                    time.sleep(self.rate_limit_delay)
                    continue

                # Any other error → do not retry
                print(f"Non-retriable error: {e}")
                break

        return "Error: exceeded retry attempts due to rate limiting."


class OLlamaPrompting(LLMPrompting):
    def __init__(self, model):
        super().__init__(model)
        self.client = OLlamaClient(host="http://ollama.:11434")

    def save_context_to_file(self, content):
        # Convert context to JSON string
        json_content = json.dumps(content)
        
        # Calculate character count
        char_count = len(json_content)
        # print(f"JSON character count: {char_count}")
        
        # Create a timestamped filename to avoid overwriting previous backups
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"last_prompt_log.json"
        
        # Ensure backup directory exists
        backup_dir = "_context_backup"
        os.makedirs(backup_dir, exist_ok=True)
        
        # Save to file
        filepath = os.path.join(backup_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(json_content)
        
        # print(f"Context successfully saved to {filepath}")
        return filepath, char_count
    

    def add_to_context(self, content):
        content = self.preprocess_input(content)
        super().add_to_context(content)

    def add_to_context_as_assistant(self, content):
        content = self.preprocess_input(content)
        super().add_to_context_as_assistant(content)        

    def preprocess_input(self, content):
        content = re.sub(r'\n\s*\n', '\n', content.strip())
        return self.sanitize_and_check(content)
    
    def sanitize_and_check(self, content):
        sanitized = ''.join(c for c in content if c.isprintable())
        # if content != sanitized:
        #     print("Special characters removed.")
        return sanitized
    
    def stack_the_context(self, content):
        res = []
        for item in content:
            res.append(item["content"])

        res = [{"role": "user", "content": "\n\n".join(res)}]
        return res


    def run_and_get_result(self, add_response_to_context=True, response_format=None):
        try:

            context_content = self.stack_the_context(self.get_context())

            self.save_context_to_file(context_content)

            options =  {"temperature": 0.3}
            chat_completion = ""
            if response_format is None:
                chat_completion = self.client.chat(
                    model=self.model, 
                    stream=False, 
                    messages=context_content, 
                    options=options,
                )
            else:
                chat_completion = self.client.chat(
                    model=self.model, 
                    stream=False, 
                    messages=context_content, 
                    options=options,
                    format=response_format,
                )

            response = chat_completion.message.content

            # the following is to remove the thinking from DeepSeek models
            response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()

            if add_response_to_context:
                self.add_to_context_as_assistant(response)
            return response
        
        except Exception as e:
            print(f"Error while calling OLlamaPrompting API: {e}")
            return "Error generating code."    