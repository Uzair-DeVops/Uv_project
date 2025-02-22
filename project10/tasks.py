
from crewai import  Task  , LLM
from crewai_tools import SerperDevTool , ScrapeWebsiteTool
from dotenv import load_dotenv

import os 
load_dotenv()


os.getenv("GEMINI_API_KEY")

research_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
class UVSafetyTasks():


    def data_t(self , agent , City_name , Country_name):
        return Task(

            description= f""" Search for today's UV radiation levels from publicly available databases and sensor networks and google and weather related websites. Prioritize data sources based on reliability and geographic relevance.. and also compare data from different data  sources  to ensure data integrity and completeness. 
            
            Parameters :

             Country_name : {Country_name},
             City_Name : {City_name},


            
            """,

            tools=[research_tool,scrape_tool],
            agent=agent,
            expected_output= """  A comprehensive report on today's UV radiation levels from reliable sources, along with a detailed report documenting data sources
            The report should include today uv index value in number and current date in number

            the report should show the uv index value of complete day 

            
            sample output : UV Radiation Levels Report for Islamabad, Pakistan

Date: February 21, 2025

Overall Assessment: The UV radiation levels in Islamabad today range from low to moderate, based on data from multiple sources.

Data Sources:

1.  The Weather Network:
    *   Current UV Index: 0 (Low)
    *   Daily Max UV Index (at 12 PM): 4 (Moderate)
    *   Link: https://www.theweathernetwork.com/en/airport/pk/punjab/islamabad/uv

2.  uvindex.io:
    *   Current UV Index: 0 (Low)
    *   Max UV Index (expected tomorrow): 5.7529 (Moderate)
    *   Link: https://uvindex.io/islamabad

3.  Weather & Radar:
    *   UV Index Today: 4 (Moderate)
    *   Hourly Breakdown: Varies throughout the day (see website for details)
    *   Link: https://www.weatherandradar.co.uk/uv-index/islamabad/12605679

            """,

        )
    def radiation_T(self , agent , context ):
        return Task(

            description= "Analyze the acquired radiation data using appropriate statistical and radiological assessment techniques. Determine the type and level of radiation present in the specified geographic region and time period. Assess potential environmental impacts, including contamination of soil, water, and air. Estimate potential human exposure levels based on established dose models..",
            context = context,
            agent=agent,
            expected_output= "A detailed report summarizing the radiation data analysis, including identified radiation types and levels, environmental impact assessments, and estimated human exposure levels, along with justification for the methods used.",
        )
    def Safety_T(self , agent , context ):
        return Task(

            description= "Develop comprehensive safety protocols for handling radioactive materials and mitigating radiation exposure risks based on the analyzed radiation data. Ensure compliance with all applicable OSHA regulations, EPA guidelines, and radiation safety protocols. Include procedures for personal protective equipment (PPE), radiation monitoring, waste disposal, and emergency response",
            context = context,
            agent=agent,
            expected_output= "A detailed safety protocol document that outlines procedures for safely handling radioactive materials, mitigating radiation exposure risks, and ensuring compliance with regulatory requirements. The document should include specific guidelines for PPE use, radiation monitoring, waste disposal, and emergency response procedures.",
        )
    def Health_T(self , agent , context ):
        return Task(

            description= " Assess the potential health risks associated with the identified radiation levels and provide recommendations for protecting public health. Include preventative measures, exposure limits, and medical surveillance protocols. Consider both acute and chronic health effects of radiation exposure",
            context = context,
            agent=agent,
            expected_output= " A comprehensive health risk assessment report that outlines potential health risks, provides recommendations for protecting public health, and includes guidelines for preventative measures, exposure limits, and medical surveillance protocols.",
        )