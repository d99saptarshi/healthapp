import google.generativeai as genai

import streamlit as st
genai.configure(api_key = st.secrets["google_api_key"])
model = genai.GenerativeModel("gemini-2.5-flash")

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
response = model.generate_content(prompt)

st.markdown(response.text)