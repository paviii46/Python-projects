import streamlit as st
# from PIL import Image
st.write("Hello ,let's register first")
name = st.text_input("Enter Your name", "Type Here ...")  # text input
weight = st.number_input("Enter your weight (in kgs)")    # number input

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
if st.button('Predict'):
        st.write("write code for prediction")