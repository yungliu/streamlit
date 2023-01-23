import streamlit as st
import openai

##Parametrage
openai.api_base = "https://tsi-openai.openai.azure.com/"
openai.api_version = "2022-12-01"


st.title('Bienvenue - Service OpenAI - Technologie du SI by YLI/PDU')

with st.sidebar:
  st.title('Paramétrages:')
  choix_modeles=st.radio('Modèles',['Ada'
,'Babbage'
,'Curie'
,'Davinci'])
  if choix_modeles == 'Ada':
    modele_option=st.selectbox('Mod',['NOT IMPLEMENTED','NOT IMPLEMENTED'])
  if choix_modeles == 'Babbage':
    modele_option=st.selectbox('Mod',['NOT IMPLEMENTED','NOT IMPLEMENTED'])
  if choix_modeles == 'Curie':
    modele_option=st.selectbox('Mod',['NOT IMPLEMENTED','NOT IMPLEMENTED'])
  if choix_modeles == 'Davinci':
    modele_option=st.selectbox('Mod',['Code','Text'])
    if (modele_option=='Code'):
      modele_a_charger="de-code-davinci-002"
    if (modele_option=='Text'):
      modele_a_charger="de-text-davinci-002"

  vtemperature = st.slider('Temperature :', value=0.7,min_value=0., max_value=1., step=.1)
  vtoken= st.slider('Token :', value=190,min_value=0, max_value=2048, step=1)
  vtop=st.slider('Top_p :', value=1.0,min_value=0.0, max_value=1.0, step=.1)
  vfreq_penalty=st.slider('frequence penalty :', value=0.0,min_value=0.0, max_value=1.0, step=.1)
  vpres_penalty=st.slider('Presence penalty :', value=0.0, min_value=0.0, max_value=1.0, step=.1)


txtInput1=st.text_area('Code à Analyser', value="### Fix bugs in the below function\n \n### Buggy Python\nimport Random\na = random.randint(1,12)\nb = random.randint(1,12)\nfor i in range(10):\n    question = \"What is \"+a+\" x \"+b+\"? \"\n    answer = input(question)\n    if answer = a*b\n        print (Well done!)\n    else:\n        print(\"No.\")\n    \n### Fixed Python",height=300)
txtInputAPPKEY = st.text_input('appKey',value="Appkey")
if st.button("Action"):
  ##  openai.api_key=txtInputAPPKEY
  ##  response = openai.Completion.create(
  ##  model="de-text-davinci-002",
  ##  prompt=txtInput1,
  ##   temperature=vtemperature,
  ##   max_tokens=vtoken,
  ##   top_p=vtop,
  ##   frequency_penalty=vfreq_penalty,
  ##   presence_penalty=vpres_penalty,
  ##   stop=["###"]
  ##  )
  openai.api_key=txtInputAPPKEY
  response = openai.Completion.create(
    engine="de-text-davinci-002",
    prompt="",
    temperature=0.84,
    max_tokens=910,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

  st.write('Le Retour ', response.choices[0].text)

 
