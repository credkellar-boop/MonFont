from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from engine.brain import MonFontsBrain
from engine.compiler import FontCompiler
import json
import os

app = FastAPI(title="MonFonts Synthesis API")
brain = MonFontsBrain()
compiler = FontCompiler("./output")

# Load base topology into memory once at startup
with open("data/topology.json", "r") as f:
    TOPOLOGY = json.load(f)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/synthesize")
async def synthesize_font(request: PromptRequest):
    try:
        # 1. Ask Gemini for the structural parameters
        params = brain.conceptualize_font(request.prompt)
        
        # 2. Compile the physical binary
        output_path = compiler.compile(params, TOPOLOGY)
        
        if not os.path.exists(output_path):
            raise HTTPException(status_code=500, detail="Compilation failed.")
            
        # 3. Return the actual .ttf file to the client
        return FileResponse(
            path=output_path, 
            media_type="font/ttf", 
            filename=f"{params.font_name.replace(' ', '_')}.ttf"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
