import streamlit as st
import pandas as pd

st.title("Machine Learning For NLP App")
st.write("Welcome to the Machine Learning For NLP App!")

st.write("This app demonstrates basic usage of Streamlit for building interactive web applications with Python.")

st.write("You can add more interactive elements like sliders, buttons, and input fields below.")

# Example of a slider
age = st.slider("Select your age", 0, 100, 25)
st.write("Your age is:", age)

# Example of a button
if st.button("Click me"):
    st.write("Button clicked!")

# Example of a text input
name = st.text_input("Enter your name")
st.write("Your name is:", name)

# Example of a checkbox
if st.checkbox("Check me"):
    st.write("Checkbox checked!")

# Example of a selectbox
option = st.selectbox(
    "Select your favorite programming language",
    ["Python", "JavaScript", "C++", "Java"]
)
st.write("Your favorite programming language is:", option)

# Example of a multiselect
languages = st.multiselect(
    "Select the programming languages you know",
    ["Python", "JavaScript", "C++", "Java"]
)
st.write("You know the following programming languages:", languages)

# Example of a radio button
choice = st.radio(
    "Select your preferred development environment",
    ["VS Code", "PyCharm", "Jupyter Notebook", "Sublime Text"]
)
st.write("Your preferred development environment is:", choice)

# Upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)
    # You can also read the contents of the uploaded file
    df = pd.read_csv(uploaded_file)
    st.write("File contents:")
    st.dataframe(df)