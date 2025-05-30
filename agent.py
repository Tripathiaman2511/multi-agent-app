import time
"""
This module defines an Agent class that interacts with a model client to process instructions and context.
It includes methods for running the agent and handling retries in case of rate limits.
"""
class Agent:
    def __init__(self, model: str, client:object):
        self.model = model
        self.client = client

    def run(self, instructions: str,context:str,) -> str:
        return self.client.call(model=self.model, instructions=instructions, inputs=context).text.strips()

    def call_with_retry(self, instructions, context, max_retries=5):
        ouptput = ""
        for attempt in range(max_retries):
            try:
                response = self.client.call(model=self.model, instructions=instructions, inputs=context)
                for chunk in response:
                    ouptput+= chunk.text
                    print(chunk.text, end="")
                return ouptput
            except Exception as e:
                wait = 2 ** attempt
                print(f"Rate limit exceeded, retrying in {wait} seconds... {e}")
                time.sleep(wait)
        raise Exception("Max retries exceeded for API call.")
