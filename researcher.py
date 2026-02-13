import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LeadResearcher:
    def __init__(self):
        # Configuration for Gemini
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def research_company(self, company_name):
        """
        Uses Gemini 1.5 Pro to research a company and provide a strategic summary.
        """
        prompt = f"""
        Research the following company and provide a concise, strategic summary for a sales professional:
        Company: {company_name}
        
        Please include:
        1. Core Product/Service: What do they actually sell?
        2. Target Audience: Who are their customers?
        3. Recent News/Growth: Anything significant in the last 6-12 months?
        4. Technical Needs (Inferred): Based on their business, what kind of AI or automation might they need?
        5. Key Value Proposition: Why do customers choose them?
        
        Format the output as a professional briefing.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error during research: {str(e)}"

    def draft_outreach(self, company_briefing):
        """
        Drafts a personalized outreach message based on the research briefing.
        """
        prompt = f"""
        Based on the following company briefing, draft a highly personalized, professional, and non-salesy introductory email from 'Jio' at 'RAK AI Studio'.
        
        RAK AI Studio provides custom Agentic AI solutions for SMEs to automate manual workflows and improve efficiency.
        
        Company Briefing:
        {company_briefing}
        
        Guidelines:
        - Mention a specific detail from the briefing to show we've done our homework.
        - Focus on how an 'Agentic AI' solution could solve a specific technical need inferred in the briefing.
        - The tone should be 'straightforward, friendly, and visionary'.
        - Keep it under 150 words.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error drafting outreach: {str(e)}"

if __name__ == "__main__":
    # Simple test case
    researcher = LeadResearcher()
    test_company = "A small regional logistics firm in Europe"
    print(f"--- Researching: {test_company} ---")
    briefing = researcher.research_company(test_company)
    print(briefing)
    
    print("\n--- Drafting Outreach ---")
    outreach = researcher.draft_outreach(briefing)
    print(outreach)
