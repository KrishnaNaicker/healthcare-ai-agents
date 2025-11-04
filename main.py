#!/usr/bin/env python3
"""
Healthcare AI Multi-Agent System
Main application entry point
"""

from healthcare_crew import HealthcareCrew
import sys
from datetime import datetime

def print_header():
    """Print application header"""
    print("\n" + "="*70)
    print("🏥 HEALTHCARE AI MULTI-AGENT SYSTEM")
    print("="*70)
    print("Powered by CrewAI + Groq")
    print("="*70 + "\n")

def print_agents_info():
    """Print information about the agents"""
    print("👥 YOUR AI MEDICAL TEAM:\n")
    print("🩺 1. STORY COLLECTOR AGENT - Medical Intake Specialist")
    print("   → Gathers your symptoms and medical history\n")
    
    print("🚨 2. SAFETY GUARD AGENT - Medical Risk Assessment Specialist")
    print("   → Identifies emergencies and assigns urgency level\n")
    
    print("🗺️  3. PATHWAY OPTIMIZER AGENT - Healthcare Pathway Strategist")
    print("   → Matches you with the right medical specialty\n")
    
    print("💙 4. PATIENT ADVOCATE AGENT - Patient Care Advocate")
    print("   → Creates your personalized action plan\n")
    print("="*70 + "\n")

def get_patient_input():
    """Get patient symptoms from user"""
    print("📝 PLEASE DESCRIBE YOUR SYMPTOMS:\n")
    print("Tell us about your health concern. Include:")
    print("  • What symptoms you're experiencing")
    print("  • When they started")
    print("  • How severe they are (1-10)")
    print("  • Any relevant medical history")
    print("  • Current medications or allergies\n")
    print("Type your symptoms below and press ENTER when done:\n")
    
    # Simple single-line input
    patient_input = input("➤ ")
    
    if not patient_input.strip():
        print("\n❌ No input provided. Please describe your symptoms.")
        sys.exit(1)
    
    return patient_input.strip()

def run_interactive():
    """Run in interactive mode"""
    print_header()
    print_agents_info()
    
    # Get patient input
    patient_input = get_patient_input()
    
    print("\n" + "="*70)
    print("🤖 AI AGENTS ARE ANALYZING YOUR CASE...")
    print("="*70)
    print("⏳ Processing through 4 specialized agents...\n")
    
    try:
        # Initialize healthcare crew with progress callback
        crew = HealthcareCrew()
        
        # Process patient with progress display
        result = crew.process_patient_with_progress(patient_input)
        
        # Display result
        print("\n" + "="*70)
        print("✨ ANALYSIS COMPLETE!")
        print("="*70)
        print("\n" + "="*70)
        print("📋 YOUR PERSONALIZED CARE PLAN")
        print("="*70 + "\n")
        print(result)
        print("\n" + "="*70)
        
        # Save result
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"care_plan_{timestamp}.txt"
        output_path = crew.save_result(result, filename)
        
        print(f"\n✅ Complete! Your care plan has been saved.")
        print(f"📁 Location: {output_path}\n")
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nPlease check:")
        print("  1. Your GROQ_API_KEY is set in .env file")
        print("  2. You have internet connection")
        print("  3. All dependencies are installed\n")
        sys.exit(1)

def run_with_sample():
    """Run with a sample patient case"""
    print_header()
    print("🧪 RUNNING WITH SAMPLE PATIENT CASE\n")
    
    sample_input = """I've been having severe chest pain for the past 2 hours. 
    The pain is sharp and radiates to my left arm. I'm also feeling short of breath 
    and a bit dizzy. I'm 55 years old, male, and I have a history of high blood pressure. 
    I'm currently taking Lisinopril 10mg daily. I have no known allergies. 
    The pain started suddenly while I was resting and it's getting worse. 
    Pain level is 8/10."""
    
    print("Sample Patient Input:")
    print("-" * 70)
    print(sample_input)
    print("-" * 70 + "\n")
    
    print("="*70)
    print("🤖 AI AGENTS ARE ANALYZING THE CASE...")
    print("="*70)
    print("⏳ Processing through 4 specialized agents...\n")
    
    try:
        crew = HealthcareCrew()
        result = crew.process_patient_with_progress(sample_input)
        
        print("\n" + "="*70)
        print("✨ ANALYSIS COMPLETE!")
        print("="*70)
        print("\n" + "="*70)
        print("📋 CARE PLAN FOR SAMPLE PATIENT")
        print("="*70 + "\n")
        print(result)
        print("\n" + "="*70)
        
        crew.save_result(result, "sample_care_plan.txt")
        print("\n✅ Sample test completed successfully!\n")
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nPlease check your setup and try again.\n")
        sys.exit(1)

def main():
    """Main application entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == "--sample":
        run_with_sample()
    else:
        run_interactive()

if __name__ == "__main__":
    main()