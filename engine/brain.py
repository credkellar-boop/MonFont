import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from engine.schema import FontParameters

load_dotenv()

class MonFontsBrain:
    def __init__(self):
        # Initializes the standard 2026 GenAI SDK client
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model_name = "gemini-2.5-flash"

    def conceptualize_font(self, user_prompt: str) -> FontParameters:
        system_instruction = (
            "You are a master typographer and generative AI engine. Analyze the user's prompt "
            "and determine the ideal geometric and parametric values needed to construct a "
            "highly accurate, functional OpenType font corresponding to their request."
        )

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=f"Generate parameters for: {user_prompt}",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json",
                response_schema=FontParameters,
                temperature=0.2,
            )
        )
        
        # Parses the strict JSON output directly back into our Pydantic schema
        return FontParameters.model_validate_json(response.text)
