from crewai import Task
from agents.product_research import lead_market_analyst
from agents.product_research import competitive_intelligence_specialist
from agents.product_research import data_synthesis_agent

print("## Welcome to the competitor reasearch")
print('-------------------------------')
product_name = input("What is the product that you want to investigate?\n")
product_details = input("Any extra details about the product?\n")

tip = "If you do your BEST WORK, I'll tip you $100!"

task_lead_market_analyst = Task(
  description=f"""Conduct a comprehensive analysis of {product_name}. 
                  Extra details {product_details}.
                  You MUST identify a minimum of 10 big products 
                  that would match the product description.
                  You MUST find a minimum of 10 major key differences 
                  between the products and their pricings.
                  Identify at least 3 areas for improvement or new features.
                  Your final answer MUST be a full analysis report that 
                  would include all the necessary data.
                  {tip}""",
  agent=lead_market_analyst
)

task_competitive_intelligence_specialist = Task(
    description=f"""Conduct in-depth research on {product_name}'s competitors.
                   You MUST identify a minimum identify and analyze 
                   10 major competitors in the market.
                   Make sure to highlight their strategies, strengths, 
                   weaknesses, and market positions.
                   Your final answer must be an expanded report that now 
                   provide a detailed comparative analysis.
                   {tip}""",
    agent=competitive_intelligence_specialist
)

task_data_synthesis = Task(
    description="""You are a renowned Senior Writer Specialist, 
                  known for your insightful and very details reports.
                  Generate a report that contains all the detailed information
                  without excluding anything important. Do no forget to add 
                  at the end features, pricing and key differences.
                  {tip}""",
    agent=data_synthesis_agent
)
