from crewai import Agent
from langchain_groq import ChatGroq
import os

class SafetyGuardAgent:
    """
    Medical Risk Assessment Specialist Agent
    Reviews patient information and identifies emergency red flags and urgency levels
    """
    
    def __init__(self, llm):
        self.llm = llm
    
    def create_agent(self):
        return Agent(
            role='Medical Risk Assessment Specialist',
            goal='Identify life-threatening emergencies, red flags, and assign appropriate urgency levels to ensure patient safety',
            backstory="""You are a highly trained emergency medical triage specialist with 20 years 
            of experience in emergency departments. You have an exceptional ability to identify 
            red flags and life-threatening conditions. You understand the difference between true 
            emergencies requiring immediate ER care versus urgent conditions that can wait a few hours 
            versus routine issues. Your assessments have saved countless lives by directing patients 
            to appropriate care levels. You recognize stroke symptoms, heart attack signs, severe 
            bleeding, respiratory distress, and other critical conditions instantly.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            max_iter=3
        )