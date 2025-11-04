from crewai import Task

class StoryCollectionTask:
    """
    Task for collecting comprehensive patient information
    """
    
    @staticmethod
    def create_task(agent, patient_input):
        return Task(
            description=f"""Conduct a thorough medical intake interview based on the patient's initial complaint.
            
            Patient's Initial Complaint: {patient_input}
            
            Your task:
            1. Analyze the patient's initial complaint
            2. Identify key symptoms and concerns
            3. Extract information about:
               - Specific symptoms (location, severity 1-10, duration, frequency)
               - When symptoms started
               - Any triggers or patterns
               - Current medications
               - Known allergies
               - Relevant medical history
               - Age, gender (if mentioned)
               - Any previous treatments tried
            
            4. Organize all information into a structured patient story
            5. Flag any missing critical information
            
            Create a comprehensive patient information report that will be used by other medical specialists.
            Be thorough and detail-oriented.""",
            expected_output="""A detailed patient information report containing:
            - Chief Complaint
            - Symptom Details (location, severity, duration, characteristics)
            - Medical History
            - Current Medications
            - Allergies
            - Demographics
            - Timeline of symptoms
            - Any additional relevant information
            
            Format as a clear, organized medical report.""",
            agent=agent
        )