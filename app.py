import streamlit as st
from engine.brain import MonFontsBrain

st.set_page_config(page_title="MonFonts Engine", page_icon="🔠", layout="wide")

st.title("MonFonts // Parametric AI Font Synthesis")
st.caption("Enter a text description to generate structural mathematical attributes for a new typeface.")

# Initialize the brain module in the background session state
if "brain" not in st.session_state:
    st.session_state.brain = MonFontsBrain()

user_prompt = st.text_input(
    "Describe the font archetype you want to generate:",
    placeholder="e.g., A high-frequency brutalist sans-serif with heavy stems and ultra-sharp edges"
)

if st.button("Synthesize Font Architecture") and user_prompt:
    with st.spinner("Gemini mapping typographic coordinates..."):
        try:
            generated_params = st.session_state.brain.conceptualize_font(user_prompt)
            
            st.success(f"Successfully generated schema mapping for: **{generated_params.font_name}**")
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Typographic Parameters")
                st.write(generated_params.model_dump())
                
            with col2:
                st.subheader("Engine Status")
                st.info("Ready to feed vector paths into the compiler subsystem.")
                
        except Exception as e:
            st.error(f"Execution pipeline halted: {str(e)}")
