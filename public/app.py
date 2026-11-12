import streamlit as st
from google import genai

st.set_page_config(page_title="Story-to-AI", page_icon="✨")
st.title("✨ Story-to-AI Converter")
st.write("Paste a short story below and watch AI transform it into scenes and interactive choices.")

# Initialize Gemini using Streamlit's hidden secrets
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

story = st.text_area(
    "Your Story:",
    height=150,
    placeholder="Once upon a time, a clumsy wizard accidentally turned his cat into a dragon..."
)

style = st.selectbox(
    "Choose Transformation Style:",
    ["Comic Book Script", "Sci-Fi Movie Trailer", "Choose-Your-Own-Adventure Game"]
)

if st.button("Transform Story", type="primary"):
    if not story.strip():
        st.warning("Please type or paste a story first!")
    else:
        with st.spinner("✨ Weaving your story with AI..."):
            prompt = f"""Transform this story into a {style} experience. 
            Break it into 3 vivid scenes with a title, visual description, and dialogue. 
            End with 2 'What happens next?' choices.

            Story: "{story}" """

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            st.markdown(response.text)
