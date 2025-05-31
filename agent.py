import time
from typing import Iterator
"""
This module defines an Agent class that interacts with a model client to process instructions and context.
It includes methods for running the agent and handling retries in case of rate limits.
"""
class Agent:
    def __init__(self, model: str, client:object):
        self.model = model
        self.client = client

    #run the agent with non-streaming response
    def run(self, instructions: str,context:str,max_retries:int = 5) -> str:
       response=self._with_retry(self.client.call, self.model, instructions, context, max_retries=max_retries)
       return response.text.strip()

 
    #run the agent with streaming response
    def run_with_stream(self, instructions:str, context:str, max_retries:int = 5) -> Iterator[str]:
        def stream():
            return self.client.call_with_stream(self.model, instructions, context)
        
        response=self._with_retry(stream, max_retries=max_retries)
        for chunk in response:
            if hasattr(chunk, 'text'):
                yield chunk.text
        
    #retry logic to handle rate limits
    def _with_retry(self, func, *args, max_retries=5,    **kwargs):
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                wait = 2 ** attempt
                print(f"Rate limit exceeded, retrying in {wait} seconds... {e}")
                time.sleep(wait)
        raise RuntimeError(f"Max retries exceeded for function: {func.__name__}")
