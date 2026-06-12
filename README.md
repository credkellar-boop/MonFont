# MonFonts // Parametric AI Font Synthesis

![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![Docker Ready](https://img.shields.io/badge/docker-containerized-2496ED.svg?logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B.svg?logo=streamlit&logoColor=white)
![Gemini API](https://img.shields.io/badge/AI-Gemini_2.5-8E75B2.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

MonFonts is an advanced, dynamically generating typographic engine. Bypassing traditional static `.ttf` file limitations, it acts as a master vector environment capable of synthesizing over 500,000 unique font archetypes on demand. 

By passing natural language prompts through the Gemini API, the engine deduces strict typographic and mathematical parameters (weight, x-height, contrast, bezier roundness) and programmatically compiles valid OpenType/TrueType binaries in real-time.

## Architecture
* **Brain:** `engine/brain.py` (Gemini API schema generation)
* **Synthesizer:** `engine/glyph_builder.py` & `engine/interpolator.py` (Vector math)
* **Compiler:** `engine/compiler.py` (FontTools binary assembly)
* **Interface:** Streamlit App (`app.py`) & FastAPI (`api/main.py`)

## Initialization
1. Clone the repository.
2. Duplicate `.env.example` to `.env` and insert your API keys.
3. Build the container: `docker build -t monfonts-engine .`
4. Run the API: `docker run -p 8000:8000 monfonts-engine`
5. Alternatively, launch the UI locally: `streamlit run app.py`
