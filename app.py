import streamlit as st
import openai
import os

# Load your API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Text Summarizer", layout="centered")
st.title("📝 AI Text Summarizer")
st.write("Paste your long text below and get a short summary using GPT-4.")

input_text = st.text_area("Enter your text here", height=300)

if st.button("Summarize"):
    if input_text:
        with st.spinner("Generating summary..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                        {"role": "user", "content": f"Summarize the following:\n\n{input_text}"}
                    ],
                    max_tokens=150,
                    temperature=0.5
                )
                summary = response['choices'][0]['message']['content']
                st.success("Summary:")
                st.write(summary)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some text.")
