import json
import os
from typing import List, Dict
from pydantic import BaseModel
from core.llm_factory import PromptingServiceFactory


class ExcludedKeywordsResponse(BaseModel):
    excluded_keywords: List[str]
    reasoning: str


class SemanticGroupsResponse(BaseModel):
    groups: Dict[str, List[str]]
    reasoning: str


class KeywordGroupingGenerator:
    def __init__(self, language: str, keywords: List[str]):
        self.language = language
        self.keywords = keywords
        self.cache_dir = os.path.join(os.path.dirname(os.getcwd()), "languages", language, "keywords")
        self.model = "gpt-4o-mini"
        
        # Create cache directory if it doesn't exist
        os.makedirs(self.cache_dir, exist_ok=True)
    
    def _get_excluded_keywords_cache_path(self) -> str:
        return os.path.join(self.cache_dir, f"excluded_keywords.json")
    
    def _get_semantic_groups_cache_path(self) -> str:
        return os.path.join(self.cache_dir, f"semantic_groups.json")
    
    def _load_from_cache(self, cache_path: str) -> dict:
        """Load data from cache file if it exists."""
        if os.path.exists(cache_path):
            with open(cache_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    
    def _save_to_cache(self, cache_path: str, data: dict):
        """Save data to cache file."""
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def _get_excluded_keywords_prompt(self) -> str:
        keywords_str = ", ".join([f"'{kw}'" for kw in self.keywords])
        
        return f"""You are an expert in programming language analysis.

Given the following list of keywords extracted from the grammar of the target language:
{keywords_str}

Your task is to identify keywords that should be EXCLUDED from semantic analysis because they are:
1. Operators or symbols without semantic meaning (e.g., punctuation, brackets, quotes)
2. Whitespace or formatting characters
3. Comment markers
4. Special symbols that are syntactic but not semantically meaningful
5. Redundant or derivative forms of other keywords

Provide:
1. A list of keywords to exclude
2. A brief reasoning for why these categories should be excluded

Be conservative - only exclude keywords that truly have no semantic meaning in the language.
"""
    
    def _get_semantic_groups_prompt(self, excluded_keywords: List[str]) -> str:
        # Filter out excluded keywords
        filtered_keywords = [kw for kw in self.keywords if kw not in excluded_keywords]
        keywords_str = ", ".join([f"'{kw}'" for kw in filtered_keywords])
        
        return f"""You are an expert in programming language semantics.

Given the following list of keywords from the target language:
{keywords_str}

Your task is to organize these keywords into semantic groups based on their PURPOSE and FUNCTIONALITY.

Examples of semantic groups:
- Arithmetic operators: keywords for mathematical operations
- Logical operators: keywords for boolean logic
- Control flow: keywords for conditionals, loops
- Type-related: keywords for type definitions, conversions, checks
- Collection operations: keywords for working with collections
- Declaration keywords: keywords for defining variables, functions, classes

Create meaningful semantic groups that:
1. Group keywords by their PURPOSE (what they're used for)
2. Use clear, descriptive group names
3. Ensure each keyword appears in exactly one group

Provide:
1. A dictionary where keys are group names and values are lists of keywords
2. A brief reasoning explaining the grouping strategy

Include ALL keywords in the groups - every keyword must be categorized.
"""
    
    def save_excluded_keywords_to_cache(self, excluded_keywords, reasoning=""):
        cache_path = self._get_excluded_keywords_cache_path()

        # Save to cache
        cache_data = {
            "excluded_keywords": excluded_keywords,
            "reasoning": reasoning,
            "model": self.model,
            "language": self.language
        }
        self._save_to_cache(cache_path, cache_data)        

    def save_groups_to_cache(self, groups, excluded_keywords, reasoning=""):
        cache_path = self._get_semantic_groups_cache_path()

        cache_data = {
            "groups": groups,
            "reasoning": reasoning,
            "excluded_keywords": excluded_keywords,
            "model": self.model,
            "language": self.language
        }
        self._save_to_cache(cache_path, cache_data)        

    def get_excluded_keywords(self) -> List[str]:
        """
        Generate or load excluded keywords list.
        Returns a list of keywords to exclude from analysis.
        """
        cache_path = self._get_excluded_keywords_cache_path()
        
        # Check cache first
        cached_data = self._load_from_cache(cache_path)
        if cached_data is not None:
            print(f"Loading excluded keywords from cache: {cache_path}")
            return cached_data.get("excluded_keywords", [])
        
        # Generate new list
        print(f"Generating excluded keywords for {self.language} using {self.model}...")
        
        prompting = PromptingServiceFactory.get_instance(self.model)
        prompting.clear_context()
        prompting.add_to_context(self._get_excluded_keywords_prompt())
        
        response = prompting.run_and_get_result(
            response_format=ExcludedKeywordsResponse.model_json_schema()
        )
        
        # Parse response
        try:
            cleaned_response = response.strip().strip('```').strip('json').strip()
            parsed_response = json.loads(cleaned_response)
            
            excluded_keywords = parsed_response.get("excluded_keywords", [])
            
            # Save to cache
            self.save_excluded_keywords_to_cache(excluded_keywords, parsed_response.get("reasoning", ""))
            
            print(f"Generated {len(excluded_keywords)} excluded keywords")
            print(f"Saved to: {cache_path}")
            
            return excluded_keywords
            
        except json.JSONDecodeError as e:
            print(f"Error parsing LLM response: {e}")
            print(f"Raw response: {response}")
            return []
    
    def get_semantic_groups(self, excluded_keywords: List[str] = None) -> Dict[str, List[str]]:
        """
        Generate or load semantic groups dictionary.
        Returns a dictionary mapping group names to lists of keywords.
        """
        cache_path = self._get_semantic_groups_cache_path()
        
        # Check cache first
        cached_data = self._load_from_cache(cache_path)
        if cached_data is not None:
            print(f"Loading semantic groups from cache: {cache_path}")
            return cached_data.get("groups", {})
        
        # Get excluded keywords if not provided
        if excluded_keywords is None:
            excluded_keywords = self.get_excluded_keywords()
        
        # Generate new groups
        print(f"Generating semantic groups for {self.language} using {self.model}...")
        
        prompting = PromptingServiceFactory.get_instance(self.model)
        prompting.clear_context()
        prompting.add_to_context(self._get_semantic_groups_prompt(excluded_keywords))
        
        response = prompting.run_and_get_result(
            response_format=SemanticGroupsResponse.model_json_schema()
        )
        
        # Parse response
        try:
            cleaned_response = response.strip().strip('```').strip('json').strip()
            parsed_response = json.loads(cleaned_response)
            
            groups = parsed_response.get("groups", {})
            
            # Save to cache
            self.save_groups_to_cache(groups, excluded_keywords, parsed_response.get("reasoning", ""))
            
            print(f"Generated {len(groups)} semantic groups")
            print(f"Saved to: {cache_path}")
            
            return groups
            
        except json.JSONDecodeError as e:
            print(f"Error parsing LLM response: {e}")
            print(f"Raw response: {response}")
            return {}
