from crewai import Crew, Process
from langchain_groq import ChatGroq
from agents import (
    StoryCollectorAgent,
    SafetyGuardAgent,
    PathwayOptimizerAgent,
    PatientAdvocateAgent
)
from tasks import (
    StoryCollectionTask,
    SafetyAssessmentTask,
    PathwayOptimizationTask,
    PatientAdvocacyTask
)
import os
import sys
import warnings
from io import StringIO
from dotenv import load_dotenv

# Suppress specific warnings
warnings.filterwarnings('ignore', message='Overriding of current TracerProvider is not allowed')
os.environ['OTEL_SDK_DISABLED'] = 'true'

class HealthcareCrew:
    """
    Main Healthcare AI Crew orchestrator
    Manages the multi-agent workflow for patient care
    """
    
    def __init__(self, groq_api_key=None, model="groq/llama-3.3-70b-versatile"):
        """
        Initialize the Healthcare Crew
        
        Args:
            groq_api_key: Groq API key (will use env var if not provided)
            model: Groq model to use (MUST include groq/ prefix)
        """
        load_dotenv()
        
        # Set up Groq API key
        if groq_api_key:
            os.environ["GROQ_API_KEY"] = groq_api_key
        elif not os.getenv("GROQ_API_KEY"):
            raise ValueError("GROQ_API_KEY must be provided or set in .env file")
        
        # Initialize LLM with groq/ prefix for CrewAI/LiteLLM compatibility
        self.llm = ChatGroq(
            temperature=0.7,
            model=model,
            api_key=os.getenv("GROQ_API_KEY")
        )
        
        # Initialize agents
        self.story_collector = StoryCollectorAgent(self.llm).create_agent()
        self.safety_guard = SafetyGuardAgent(self.llm).create_agent()
        self.pathway_optimizer = PathwayOptimizerAgent(self.llm).create_agent()
        self.patient_advocate = PatientAdvocateAgent(self.llm).create_agent()
    
    def process_patient(self, patient_input):
        """
        Process a patient through the entire healthcare workflow
        
        Args:
            patient_input: Patient's initial complaint/symptoms
            
        Returns:
            Final patient action plan
        """
        
        # Create tasks
        task1 = StoryCollectionTask.create_task(self.story_collector, patient_input)
        task2 = SafetyAssessmentTask.create_task(self.safety_guard, [task1])
        task3 = PathwayOptimizationTask.create_task(self.pathway_optimizer, [task1, task2])
        task4 = PatientAdvocacyTask.create_task(self.patient_advocate, [task1, task2, task3])
        
        # Create crew
        crew = Crew(
            agents=[
                self.story_collector,
                self.safety_guard,
                self.pathway_optimizer,
                self.patient_advocate
            ],
            tasks=[task1, task2, task3, task4],
            process=Process.sequential,
            verbose=False
        )
        
        # Suppress all output from crew execution
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        
        try:
            # Execute workflow
            result = crew.kickoff()
        finally:
            # Restore stdout and stderr
            sys.stdout = old_stdout
            sys.stderr = old_stderr
        
        return result
    
    def process_patient_with_progress(self, patient_input):
        """
        Process a patient with progress display
        
        Args:
            patient_input: Patient's initial complaint/symptoms
            
        Returns:
            Final patient action plan
        """
        agents_info = [
            ("Story Collector", "Gathering patient information"),
            ("Safety Guard", "Assessing risk level"),
            ("Pathway Optimizer", "Finding best care route"),
            ("Patient Advocate", "Creating your action plan")
        ]
        
        # Create tasks
        task1 = StoryCollectionTask.create_task(self.story_collector, patient_input)
        task2 = SafetyAssessmentTask.create_task(self.safety_guard, [task1])
        task3 = PathwayOptimizationTask.create_task(self.pathway_optimizer, [task1, task2])
        task4 = PatientAdvocacyTask.create_task(self.patient_advocate, [task1, task2, task3])
        
        tasks = [task1, task2, task3, task4]
        agents = [self.story_collector, self.safety_guard, self.pathway_optimizer, self.patient_advocate]
        
        # Process each task individually with progress display
        results = []
        for i, (task, agent, (agent_name, agent_action)) in enumerate(zip(tasks, agents, agents_info), 1):
            # Show agent starting
            print(f"🔄 Agent {i}: {agent_name} - {agent_action}")
            print(f"   ⏳ Analyzing...")
            
            # Create mini-crew for this task
            mini_crew = Crew(
                agents=[agent],
                tasks=[task],
                process=Process.sequential,
                verbose=False
            )
            
            # Suppress output and warnings
            old_stdout = sys.stdout
            old_stderr = sys.stderr
            sys.stdout = StringIO()
            sys.stderr = StringIO()
            
            try:
                # Execute this specific task
                result = mini_crew.kickoff()
                results.append(result)
            finally:
                sys.stdout = old_stdout
                sys.stderr = old_stderr
            
            # Show agent complete
            print(f"   ✓ Analysis complete!")
            
            # Show passing to next agent
            if i < 4:
                print(f"   📤 Passing results to Agent {i + 1}...\n")
        
        # Return final result
        return results[-1] if results else None

    def save_result(self, result, filename="patient_care_plan.txt"):
        """
        Save the result to a file
        
        Args:
            result: The crew execution result
            filename: Output filename
        """
        output_path = os.path.join("outputs", filename)
        os.makedirs("outputs", exist_ok=True)
        
        with open(output_path, 'w') as f:
            f.write(str(result))
        
        print(f"\n✅ Care plan saved to: {output_path}")
        return output_path