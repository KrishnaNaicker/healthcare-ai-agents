from crewai import Task

class SafetyAssessmentTask:
    """
    Task for assessing medical risk and urgency
    """
    
    @staticmethod
    def create_task(agent, context_tasks):
        return Task(
            description="""Review the complete patient information report and conduct a thorough risk assessment.
            
            Your task:
            1. Analyze all symptoms and patient information
            2. Identify any RED FLAGS or life-threatening conditions including:
               - Chest pain (heart attack risk)
               - Difficulty breathing (respiratory emergency)
               - Severe bleeding
               - Loss of consciousness
               - Stroke symptoms (facial drooping, slurred speech, arm weakness)
               - Severe head injury
               - Severe abdominal pain
               - Suicidal thoughts
               - Severe allergic reaction
               - Very high fever with confusion
            
            3. Assign urgency level:
               - EMERGENCY: Life-threatening, go to ER immediately
               - URGENT: Serious condition, needs care within 24 hours
               - STANDARD: Needs medical attention, schedule within 1 week
               - ROUTINE: Non-urgent, can schedule regular appointment within 2-4 weeks
            
            4. Provide clear reasoning for the urgency level
            5. List specific warning signs identified
            
            Be conservative - when in doubt, err on the side of caution.""",
            expected_output="""A risk assessment report containing:
            - Urgency Level (EMERGENCY/URGENT/STANDARD/ROUTINE)
            - Red Flags Identified (if any)
            - Risk Factors
            - Reasoning for urgency level
            - Immediate actions required (if emergency)
            - Warning signs to watch for
            
            Format as a clear medical risk assessment.""",
            agent=agent,
            context=context_tasks
        )