import nltk
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

from transformers import pipeline
import streamlit as st

nltk.download("punkt")

chatbot = pipeline("text-generation", model="gpt2-medium")  # or replace with a better model

def healthcare_chatbot(user_input):
    user_input = user_input.lower()

    if "symptom" in user_input:
        return "Please taKe consultation from a doctor for accurate advice."
    elif "appointment" in user_input:
        return "If you're not feeling well, schedule an appointment with your doctor."
    elif "medication" in user_input:
        return "It's important to take your prescribed medicines."
    else:
        response = chatbot(user_input, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User:", user_input)
            with st.spinner("Processing your query... please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant:", response)
        else:
            st.write("Please enter a message to get a response.")

if __name__ == "__main__":
    main()
