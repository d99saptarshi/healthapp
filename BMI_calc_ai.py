from google import genai as ai
import os
import streamlit as st
os.environ["API_KEY"] = "AIzaSyCAfu6mLEQ_kbFNuejOieKCpAxkIqLa3es"
client = ai.Client(api_key = os.getenv("API_KEY"))

st.title("AI based BMI calculator - know your Health!")

name = st.text_input("Enter Your Name: ")
wt = st.number_input("Enter Your Weight in Kg: ")
ht = st.slider(f"Enter Your Height in cm: ",50,250)
age = st.number_input("Enter your age: ")
gender = st.text_input("Enter your gender: ")

bmi = round(wt / (ht/100)**2,2)

if st.button("Calculate BMI"):
    st.write(f"{name}, with your weight {wt} and height {ht}, your BMI is: {bmi}")

prompt = f"Act like a expert nutritionist, comment on the BMI with the following data: height as {ht}, weight as {wt}, age as {age}, gender as {gender} BMI as {bmi}, please suggest how the BMI is"
response = client.models.generate_content(model="gemini-2.5-flash", contents = prompt)

st.markdown(response.text)