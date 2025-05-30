import os
from typing import Protocol
from google.genai import types
from google import genai
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(".env"))


"""
LLMClient Protocol and GeminiClient implementation for LLM interactions.
This module defines a protocol for LLM clients and provides an implementation
for the GeminiClient using the Google GenAI API.
"""
class LLMCLient(Protocol):
    def call(self,model:str,instructions: str, inputs: str) -> any:
        """
        Call the LLM with the given model, instructions, and inputs.
        Should return a dictionary with the response content.
        """
        pass

class GeminiClient:
    def __init__(self):
        self.client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def call(self, model: str, instructions: str, inputs: str) -> any:
        return self.client.models.generate_content_stream(
            model=model,
            contents=inputs,
            config=types.GenerateContentConfig(
                system_instruction=instructions
            ),
        )
