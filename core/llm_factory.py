from core.llm_prompting import OpenAIPrompting, OLlamaPrompting, AzureAIPrompting

class PromptingServiceFactory:

    @staticmethod
    def get_instance(model: str):
        if model.startswith("gpt-"):
            return OpenAIPrompting(model)
        elif model == "DeepSeek-V3.1" or model == "Llama-3.3-70B-Instruct":
            return AzureAIPrompting(model)        
        else:
            return OLlamaPrompting(model)
        # else:
        #     raise ValueError(f"Unsupported model: {model}")