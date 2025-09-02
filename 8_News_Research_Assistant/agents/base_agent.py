from openai import AsyncOpenAI
from typing import Dict, Any, List
import config
import re
import json

class BaseAgent:
    def __init__(self, role: str, prompt: str):
        self.client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)
        self.role = role
        self.system_prompt = prompt
        self.temperature = config.TEMPERATURE_SETTINGS.get(role, 0.7)

    async def _call_openai(self, messages: List[Dict[str, str]], temperature: float = None) -> str:
        """Make an API call to OpenAI."""
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=messages,
                temperature=temperature or self.temperature,
                response_format={"type": "json_object"}  # Force JSON response
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in OpenAI API call: {e}")
            raise

    def _create_messages(self, user_input: str) -> List[Dict[str, str]]:
        """Create the messages list for the OpenAI API call."""
        return [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_input}
        ]

    def _clean_json_response(self, response: str) -> str:
        """Clean the JSON response from GPT to make it parseable."""
        # Remove markdown code blocks if present
        response = re.sub(r'```json\s*', '', response)
        response = re.sub(r'```\s*$', '', response)
        
        # Remove any leading/trailing whitespace
        response = response.strip()
        
        # Validate that it starts with { or [
        if not response.startswith('{') and not response.startswith('['):
            raise ValueError("Response is not a valid JSON object/array")
            
        return response

    async def _parse_json_response(self, response: str, default_value: Any = None) -> Any:
        """Parse JSON response with error handling."""
        try:
            cleaned_response = self._clean_json_response(response)
            return json.loads(cleaned_response)
        except Exception as e:
            print(f"Error parsing JSON response: {str(e)}")
            print(f"Original response: {response}")
            if default_value is not None:
                return default_value
            raise

    async def process(self, input_data: Any) -> Any:
        """Process the input data. To be implemented by child classes."""
        raise NotImplementedError("Subclasses must implement process method") 