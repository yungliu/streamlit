import streamlit as st
import openai

st.title('Bienvenue')
txtInput1=str.text_area('textinput1', value="Mon test sur Streamlit")
txtInputAPPKEY = st.text_input('appKey',value="Appkey")
click = st.button("Resume")

url = 'https://<xxxxxxxx<w'
myobj = {'name':txtInput1}
st.write('envoi',myobj)

openai.api_key=txtInputAPPKEY
response = openai.Completion.create(
  model="code-davinci-002",
  prompt="##### Fix bugs in the below function\n \n### Buggy Python\nimport Random\na = random.randint(1,12)\nb = random.randint(1,12)\nfor i in range(10):\n    question = \"What is \"+a+\" x \"+b+\"? \"\n    answer = input(question)\n    if answer = a*b\n        print (Well done!)\n    else:\n        print(\"No.\")\n    \n### Fixed Python",
  temperature=0,
  max_tokens=182,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["###"]
)

st.write('Le Résume ', response.text)
