import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def analyze_customer_inquiry(inquiry_text):
    """Uses Gemini to parse and extract structured data from customer messages."""
    client = genai.Client()

    prompt = f"""
    Analyze the following customer inquiry and extract these details:
    1. Customer Name
    2. Company / Business Name
    3. Service / Product Requested
    4. Urgency Level (Low, Medium, High)
    5. Recommended Next Action for the Business Owner

    Inquiry Text:
    {inquiry_text}
    """

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    return response.text

if __name__ == "__main__":
    # Sample incoming message from a potential client
    sample_message = """
    Hi, my name is Sarah Jenkins from Apex Landscaping. 
    We are completely swamped with phone calls and are missing leads every day. 
    We need an automated text-back system set up as soon as possible. Can we talk tomorrow?
    """

    print("🤖 Processing customer message with AI...\n")
    result = analyze_customer_inquiry(sample_message)
    print(result)
