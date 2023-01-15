import streamlit as st
import openai



st.title('Bienvenue - Service OpenAI - by YLI')

with st.sidebar:
  st.title('Paramétrages:')
  choix_modeles=st.radio('Modèle',['Ada'
,'Babbage'
,'Curie'
,'Davinci'])
  if choix_modeles == 'Ada':
    st.selectbox('Mod',['Ada1','Ada2'])
  if choix_modeles == 'Babbage':
    st.selectbox('Mod',['Babbage','Babbage'])
  if choix_modeles == 'Curie':
    st.selectbox('Mod',['Curie','Curie'])
  if choix_modeles == 'Davinci':
    st.selectbox('Mod',['Davinci','Davinci'])


txtInput1=st.text_area('Code à Analyser', value="##### Fix bugs in the below function\n \n### Buggy Python\nimport Random\na = random.randint(1,12)\nb = random.randint(1,12)\nfor i in range(10):\n    question = \"What is \"+a+\" x \"+b+\"? \"\n    answer = input(question)\n    if answer = a*b\n        print (Well done!)\n    else:\n        print(\"No.\")\n    \n### Fixed Python",height=300)
txtInputAPPKEY = st.text_input('appKey',value="Appkey")
if st.button("Action"):
  openai.api_key=txtInputAPPKEY
  response = openai.Completion.create(
  model="code-davinci-002",
  prompt=txtInput1,
   temperature=0,
   max_tokens=182,
   top_p=1.0,
   frequency_penalty=0.0,
   presence_penalty=0.0,
   stop=["###"]
  )
  st.write('Le Retour ', response.choices[0].text)

 
