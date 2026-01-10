from strands import Agent #Importing Agent class from strands module
from strands_tools import file_read
from strands.models.ollama import OllamaModel

SYSTEM_PROMPT = """
You are the log analysis agent.
You are excellent at understanding and analyzing log files i.e.(.log /var/log/*).
You can deduce results in short and crisp manner.
You are helpful and use Devops Mindset in log analysis and root cause anaylsis.
You won't halluctinate and suggest new changes.
You will not engage in any production action, but suggest changes and ideas to devops engineers.
"""

ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="llama3.1"               # Specify which model to use
)

agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    model=ollama_model, 
    tools = [file_read]
) # calling Bedrock LLMs

# agent("can you read the file called app.log in this directory")
agent("Detect how many times INFO, WARNING, ERROR occurs and return the count only from app.log")





