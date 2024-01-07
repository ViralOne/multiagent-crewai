from crewai import Agent
from langchain_openai import ChatOpenAI as OpenAI

# Create an instance of the OpenAIWrapper
local_openai_client = OpenAI(
    base_url="http://localhost:3008/v1", api_key="not-needed", temperature=0.4
)

def create_agent(
    role,
    goal,
    backstory,
    verbose=True,
    allow_delegation=False,
    tools=None,
    llm=local_openai_client,
):
    """
    Create an Agent with default settings. Override as needed for specific agents.
    """
    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        verbose=verbose,
        allow_delegation=allow_delegation,
        tools=tools,
        llm=llm,
    )
