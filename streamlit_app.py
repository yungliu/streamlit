import streamlit as st
import openai

st.title('Bienvenue')
txtInput1=st.text_area('textinput1', value="##### Fix bugs in the below function\n \n### Buggy Python\nimport Random\na = random.randint(1,12)\nb = random.randint(1,12)\nfor i in range(10):\n    question = \"What is \"+a+\" x \"+b+\"? \"\n    answer = input(question)\n    if answer = a*b\n        print (Well done!)\n    else:\n        print(\"No.\")\n    \n### Fixed Python")
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

 
