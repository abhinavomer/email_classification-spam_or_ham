import streamlit as st
import numpy as np
import pickle
#st.image("fr.jpg")
st.title("Email Classification")
email=st.text_input("Email::-")
if st.button("Submit"):
    li=[]
    li.append(email)
    transformer=pickle.load(open('vector.pkl', 'rb'))
    li=transformer.transform(li)
    model = pickle.load(open('email.pickle', 'rb'))
    x=model.predict(li)
    if x[0]==0:
        st.write("Ham")
    else:
        st.write("spam")
        