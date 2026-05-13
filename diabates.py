import streamlit as st
# from PIL import Image
st.write("enter ")
a=st.number_input("Enter pregnancy level:")  
b =st.number_input("enter glucose level:") 
c =st.number_input("enter blood pressue:")
d=st.number_input("enter insulin level:")
if st.button('predict'):
    with open("diabetes_knn.pk","rb")as file:
       loaded_model=pickle.load(file)
    result=loaded_model.predict([["a","b","c","d"]])
    st.write(result)