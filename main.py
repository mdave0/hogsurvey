import requests
import json

print("loading")

#add posthog api key
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <POSTHOG API KEY>"
}


data = {
    "query": {
        "kind": "HogQLQuery",
        "query": "   select properties.$survey_response from events"
    }
}

#add your posthog project id
response = requests.post(
    'https://us.i.posthog.com/api/projects/{POSTHOG PROJECT ID}/query', 
    headers=headers, 
    json=data
)

API_Data = response.json() 
  
x = API_Data['results']
y = ','.join(str(i) for i in x)


#At the command line, only need to run once to install the package via pip:

#$ pip install google-generativeai

#it may be useful to install using venv

import google.generativeai as genai

#add gemini api key here
genai.configure(api_key="<GEMINI API KEY>")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

#output formatting
system_instruction = "ignore the input [none] and provide trends, summary, and sentiment analysis of these survey responses, and reformat the data so i can copy it to google sheets"

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])

convo.send_message(y)
print(convo.last.text)

