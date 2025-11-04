from crewai import Agent
from langchain_groq import ChatGroq
import os

class StoryCollectorAgent:
    """
    Medical Intake Specialist Agent
    Collects comprehensive patient information including symptoms, medical history, and demographics
    """
    
    def __init__(self, llm):
        self.llm = llm
    
    def create_agent(self):
        return Agent(
            role='Medical Intake Specialist',
            goal='Gather complete and accurate patient information including symptoms, medical history, allergies, medications, and demographics',
            backstory="""You are an experienced medical intake specialist with 15 years of experience 
            in patient interviews. You have a warm, empathetic approach and know exactly which questions 
            to ask to get a complete picture of the patient's condition. You never miss important details 
            like allergies, current medications, or relevant medical history. You make patients feel 
            comfortable sharing their health concerns.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            max_iter=3
        )