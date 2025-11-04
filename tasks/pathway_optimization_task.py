from crewai import Task

class PathwayOptimizationTask:
    """
    Task for creating optimal healthcare pathways
    """
    
    @staticmethod
    def create_task(agent, context_tasks):
        return Task(
            description="""Based on the patient information and risk assessment, create an optimal healthcare pathway.
            
            Your task:
            1. Review the patient's symptoms and urgency level
            2. Match symptoms to the appropriate medical specialty:
               - Cardiology: Heart, chest pain, blood pressure
               - Dermatology: Skin, hair, nails
               - Orthopedics: Bones, joints, fractures
               - Neurology: Brain, nerves, headaches, seizures
               - Gastroenterology: Digestive system, stomach, intestines
               - Endocrinology: Hormones, diabetes, thyroid
               - Pulmonology: Lungs, breathing
               - Urology: Urinary system, kidneys
               - Gynecology: Women's reproductive health
               - Psychiatry: Mental health
               - ENT: Ear, nose, throat
               - Ophthalmology: Eyes, vision
               - Primary Care: General health, multiple systems
            
            3. Recommend appropriate care setting:
               - Emergency Room (ER): Life-threatening emergencies
               - Urgent Care: Needs care today but not life-threatening
               - Primary Care: General health issues
               - Specialist Appointment: Specific specialty needed
               - Telemedicine: Can be handled remotely
            
            4. Create a step-by-step care pathway
            5. Provide rationale for recommendations
            
            Consider both the urgency level and the specific condition type.""",
            expected_output="""A healthcare pathway recommendation containing:
            - Recommended Medical Specialty
            - Recommended Care Setting (ER/Urgent Care/Primary Care/Specialist)
            - Step-by-Step Care Pathway
            - Rationale for recommendations
            - Expected timeline
            - Alternative options (if applicable)
            
            Format as a clear, actionable care pathway plan.""",
            agent=agent,
            context=context_tasks
        )