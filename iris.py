import streamlit as st
# from PIL import Image
st.write("enter details to understand which species does a flower come")
sepal_length =st.number_input("Enter sepal legth")  
sepal_width =st.number_input("sepal width") 
petal_length =st.number_input("petal length")
petal_width =st.number_input("petal width")
if st.button('predict'):
    with open("iris_model.pk","rb")as file:
       loaded_model=pickle.load(file)
    result=loaded_model.predict([["sepal_length","sepal_width","petal_length","petal_width"]])
    st.write(result)