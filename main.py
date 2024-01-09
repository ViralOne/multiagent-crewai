from crewai import Crew
from tasks import task_lead_market_analyst
from tasks import task_competitive_intelligence_specialist
from tasks import task_data_synthesis
from agents.product_research import lead_market_analyst
from agents.product_research import competitive_intelligence_specialist
from agents.product_research import data_synthesis_agent

crew = Crew(
    agents=[
        lead_market_analyst, 
        competitive_intelligence_specialist, 
        data_synthesis_agent
      ],
    tasks=[
        task_lead_market_analyst, 
        task_competitive_intelligence_specialist, 
        task_data_synthesis
       ],
    verbose=True
)

result = crew.kickoff()
print("\n########################")
print("## Here is the report")
print("######################")
print(result)
