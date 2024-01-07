from utils import create_agent
from langchain.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

researcher = create_agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge information',
    backstory="""You work at a leading tech think tank.
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting
  actionable insights""",
    tools=[search_tool],
)
