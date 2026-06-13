<p align="center">
  <img src="IMG_3333.jpeg" alt="Profile Image" width="400"/>
</p>
# MonFonts // Parametric AI Font Synthesis

![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![Docker Ready](https://img.shields.io/badge/docker-containerized-2496ED.svg?logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B.svg?logo=streamlit&logoColor=white)
![Foundry](https://img.shields.io/badge/Foundry-Smart_Contracts-2C3E50.svg)
![Monad Network](https://img.shields.io/badge/Network-Monad_10k_TPS-8A2BE2.svg)
![Gemini API](https://img.shields.io/badge/AI-Gemini_2.5-8E75B2.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

MonFonts is an advanced, dynamically generating typographic engine. Bypassing traditional static `.ttf` file limitations, it acts as a master vector environment capable of synthesizing over 500,000 unique font archetypes on demand. 

By passing natural language prompts through the Gemini API, the engine deduces strict typographic and mathematical parameters and programmatically compiles valid OpenType/TrueType binaries in real-time.

## Architecture
* **Brain:** `engine/brain.py` (Gemini API schema generation)
* **Synthesizer:** `engine/glyph_builder.py` & `engine/interpolator.py` (Vector math)
* **Compiler:** `engine/compiler.py` (FontTools binary assembly)
* **Registry:** `src/MonFontsBatchRegistry.sol` (Monad high-frequency ledger)
* **Vault:** `engine/vault.py` (AES-256-GCM Sovereign Storage)

## Initialization
1. Clone the repository.
2. Duplicate `.env.example` to `.env` and insert your API keys.
3. Build the container: `docker-compose build`
4. Run the full environment: `docker-compose up`
