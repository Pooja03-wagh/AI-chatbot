 
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import streamlit as st

nltk.download("punKt")
nltk.download("stopwords")

chatbot=pipeline("text-generation",model="distilgpt2")


def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "please consult Doctor for accurate advise"
    elif "appointment" in user_input:
        return "if you are not feeling well then schedue your appointment with your doctor"
    elif "medication" in user_input:
        return "its important to taKe presribed medicines"
    else:
        response= chatbot(user_input, max_length= 300,num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input=st.text_input("how can i assist you today?")
    print(user_input)
    if st.button("Submit"):
        if user_input:
            st.write("User :",user_input)
            with st.spinner("processing your query......please wait.....!"):
              response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant :", response)
        else:
            st.write("Please enter a message to get a response.")

if __name__=="__main__":
    main()
