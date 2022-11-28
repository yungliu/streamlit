import streamlit as st
import requests
st.title('Bienvenue')
txtInput1=st.text_area('textinput1', value="Mon test sur Streamlit")
click = st.button("Resume")

url = 'https://azfpowerapps.azurewebsites.net/api/httptriggerpowerapps'
myobj = {'name':txtInput1}
st.write('envoi',myobj)

x = requests.post(url, json = myobj)

st.write('Reponse HTTP ', x)

st.write('Le Résume ', x.text)
