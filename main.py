from llmclients import GeminiClient
from agent import Agent
if __name__ == "__main__":
    client=GeminiClient()
    agent=Agent(model="gemini-2.0-flash", client=client)
    
    """
    Example of multi-agent interaction using the Agent class.
    This example demonstrates how to use the Agent class to create a multi-agent system
    where each agent processes the output of the previous one.
    """
    # agent1=agent.call_with_retry(instructions="You are Agent 1. Your task is to generate a title based on the context provided.", context="Colors in rainbow")
    # agent2=agent.call_with_retry(instructions="You are Agent 2. Your task is to refine the title and generate a prompt based on the title provided.", context=agent1)
    # agent3=agent.call_with_retry(instructions="You are Agent 3. Your task is to generate the final output based on the prompt provided.", context=agent2)