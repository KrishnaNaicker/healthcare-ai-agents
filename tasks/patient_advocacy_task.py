from crewai import Task

class PatientAdvocacyTask:
    """
    Task for creating patient-friendly action plans
    """
    
    @staticmethod
    def create_task(agent, context_tasks):
        return Task(
            description="""Create a clear, patient-friendly action plan that synthesizes all medical information.
            
            Your task:
            1. Review all information from previous agents:
               - Patient symptoms and history
               - Risk assessment and urgency level
               - Recommended care pathway and specialty
            
            2. Create a simple, clear action plan in PLAIN ENGLISH:
               - Avoid medical jargon
               - Use simple, everyday language
               - Break down complex terms
               - Be warm and reassuring but honest
            
            3. Include:
               - What to do NOW (immediate actions)
               - Timeline (today, this week, within 2 weeks)
               - Where to go (specific facility type)
               - Which doctor to see (specialty explained simply)
               - What to bring (ID, insurance card, medication list, etc.)
               - What to expect (brief overview of visit)
               - Warning signs to watch for
               - How to prepare for the appointment
            
            4. Empower the patient with:
               - Clear understanding of their situation
               - Confidence in next steps
               - Knowledge of when to seek additional help
            
            5. Be empathetic and supportive in tone
            
            Make the patient feel informed, supported, and clear on what to do next.""",
            expected_output="""A patient-friendly action plan containing:
            
            1. YOUR SITUATION (simple explanation)
            2. WHAT TO DO NOW (immediate action items with timeline)
            3. WHERE TO GO (specific location type)
            4. WHO TO SEE (specialty explained simply)
            5. WHAT TO BRING (checklist)
            6. WHAT TO EXPECT (brief overview)
            7. WARNING SIGNS (when to seek immediate help)
            8. HOW TO PREPARE (preparation steps)
            
            Written in simple, clear, empathetic language that anyone can understand.
            No medical jargon. Actionable and specific.
            
            Format as a friendly, easy-to-follow action plan.""",
            agent=agent,
            context=context_tasks
        )