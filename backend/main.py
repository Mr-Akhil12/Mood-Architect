import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY is not set in environment variables.")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, define specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class AffirmationRequest(BaseModel):
    name: str = Field(..., min_length=1, description="Name of the user")
    feeling: str = Field(..., min_length=1, description="Current feeling of the user")

    @validator('name', 'feeling')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Must be a non-empty string')
        return v

class AffirmationResponse(BaseModel):
    affirmation: str

# System instructions for the model
SYSTEM_INSTRUCTION = """
You are a therapeutic affirmation assistant. Your goal is to provide short, warm, and supportive affirmations based on the user's name and how they are feeling.

Rules:
1. No medical or legal advice.
2. No diagnosis of any condition.
3. No self-harm guidance.
4. If the user mentions self-harm or severe distress (e.g., suicide, hurting themselves):
   - Do NOT generate a standard affirmation.
   - Provide a safe, supportive message encouraging them to seek professional help immediately.
   - Example: "I hear that you are going through a very difficult time. Please know that you are not alone, but I am an AI and cannot provide the help you need. Please reach out to a professional or a crisis hotline immediately."
5. Keep the affirmation short (2-4 sentences).
6. Be warm, empathetic, and specific to the user's name and feeling.
"""

@app.post("/api/affirmation", response_model=AffirmationResponse)
async def generate_affirmation(request: AffirmationRequest):
    if not GEMINI_API_KEY:
        raise HTTPException(
            status_code=500, 
            detail="Server configuration error: Gemini API key is missing."
        )

    try:
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash-lite-preview-09-2025", 
            system_instruction=SYSTEM_INSTRUCTION # Note: specific system instruction support depends on library version, otherwise prompt injection
        )
        
        # Constructing the prompt safely
        prompt = f"User Name: {request.name}\nUser Feeling: {request.feeling}\nGenerate an affirmation."

        # Safety settings - high block threshold for safety
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        # For newer google-generativeai versions, system_instruction can be passed to GenerativeModel constructor
        # If using older pattern, adapt prompt. Assuming latest lib.
        
        response = model.generate_content(
            prompt,
            safety_settings=safety_settings
        )

        if not response.text:
            raise ValueError("Empty response from AI")

        return AffirmationResponse(affirmation=response.text)

    except Exception as e:
        # In a real app, log the actual error `e` internally
        print(f"Error generating affirmation: {e}")
        raise HTTPException(
            status_code=502,
            detail="Unable to contact the affirmation spirit guide (AI Service Error). Please try again gently."
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
