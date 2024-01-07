from crewai import Crew, Process
from tasks import taskResearch, taskWrite
from agents.researcher import researcher
from agents.writer import writer

crew = Crew(
    agents=[researcher, writer],
    tasks=[taskResearch, taskWrite],
    verbose=2,
    process=Process.sequential
)

result = crew.kickoff()

print("######################")
print(result)
