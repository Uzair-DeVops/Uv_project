import streamlit as st
from agents import UVSafetyAgents
from tasks import UVSafetyTasks
from crewai import Crew

# Streamlit UI
st.title("UV Radiation Safety Assessment")

# User Inputs
Country_name = st.text_input("Enter Country Name", "Pakistan")
City_name = st.text_input("Enter City Name", "Lahore")

if st.button("Start Analysis"):
    agents = UVSafetyAgents()
    tasks = UVSafetyTasks()

    agent1 = agents.Data()
    task1 = tasks.data_t(agent=agent1, Country_name=Country_name, City_name=City_name)

    crew = Crew(
        agents=[agent1],
        tasks=[task1],
        verbose=True,
    )

    results = crew.kickoff()
    st.write("### Analysis Results:")
    st.write(results)
