from utils import create_agent
from langchain.tools import DuckDuckGoSearchRun
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain.tools import Tool
from dotenv import load_dotenv

load_dotenv()

searchDDG = DuckDuckGoSearchRun()
wrapperGoogle = GoogleSearchAPIWrapper()

searchGoogle = Tool(
    name="Google Search",
    description="Search Google for recent results.",
    func=wrapperGoogle.run,
)

lead_market_analyst = create_agent(
    role='Lead Market Analyst',
    goal="""Conduct amazing analysis of the products and
            competitors, providing in-depth insights to guide product research
            Provide insights on enhancing the product's value 
            proposition and market alignment""",
    backstory="""As the Lead Market Analyst at a premier
                digital marketing firm, you specialize in dissecting
                online business landscapes""",
    tools=[searchDDG, searchGoogle],
)

competitive_intelligence_specialist = create_agent(
    role='Competitive Intelligence Specialist',
    goal="""Identify competitive advantages and vulnerabilities 
            to assist in strategic decision-making""",
    backstory="""Experienced in competitive analysis across various 
                industries, skilled in recognizing market trends 
                and competitor actions""",
    tools=[searchDDG, searchGoogle],
)

data_synthesis_agent = create_agent(
    role='Senior Writer Specialist',
    goal="""You create detailed reports consolidating all important details.""",
    backstory="""You are known for your insightful and detailed reports that includes
            competitor analysis, market research, user insights, pricing, features, etc.""",
    tools=[],
)
