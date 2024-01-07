from crewai import Task
from agents.researcher import researcher
from agents.writer import writer

user_input = input("What do you need: ")

taskResearch = Task(
  description=f"""Conduct a comprehensive analysis of {user_input}.
  Identify a minimum of 3 major key points to talk about.
  Your final answer MUST be a full analysis report""",
  agent=researcher
)

taskWrite = Task(
  description=f"""Using the insights provided, develop an engaging blog
  that highlights {user_input}.
  Your post should be informative yet accessible, giving the best details that the user need.
  Make it sound cool, avoid complex words so it doesn't sound like AI.
  Your final answer MUST be for a blog, give more details such as numbers and dates.""",
  agent=writer
)
