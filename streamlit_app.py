import streamlit as st
import requests
st.title('Bienvenue')
txtInput1=st.text_area('textinput1', value="Mon test sur Streamlit")
click = st.button("Resume")

url = 'https://azfpowerapps.azurewebsites.net/api/httptriggerpowerapps'
myobj = {'name': 'It was the best of times, it was the worst of times, it wasthe age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, i was the season of Light, it was the season of Darkness, itwas the spring of hope, it was the winter of despair, (...)'}

st.write('envoi',myobj)

x = requests.post(url, json = myobj)

st.write('Retour', x)
