import os
from google import genai
from dotenv import load_dotenv

# This loads your key safely from the local .env file
load_dotenv()

# The client automatically looks for GEMINI_API_KEY in your environment
client = genai.Client()

def analyze_customer_inquiry(inquiry_text):
    """Uses Gemini to parse and extract structured data from customer messages."""
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
    Hi, my name is Riya Sharma from XYZ Salon. 
    We are completely swamped with phone calls and are missing leads every day. 
    We need an automated text-back system set up as soon as possible. Can we talk tomorrow?
    """

    print("🤖 Processing customer message with AI...\n")
    result = analyze_customer_inquiry(sample_message)
    print(result)
