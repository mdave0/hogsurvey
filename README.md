# hogsurvey
- Posthog survey response analysis using Gemini. This works for the 'freeform' survey type with just a text input.
- This sort of survey is open ended, and so using an LLM may unlock new insights.
- A useful way to quickly have an always up to date summary of survey responses, and run a huge variety of powerful analyses just by changing the system prompt.

SETUP
- Install google-generativeai before running, and add your Posthog API Key, Project ID, and Gemini API Key.
- See posthog docs for how to get project id.
- Modify system-instruction to change output.

Example output
![image](https://github.com/mdave0/hogsurvey/assets/29395487/633cf4ba-f70c-45e8-9a17-e69007e50a7f)

Survey form
![image](https://github.com/mdave0/hogsurvey/assets/29395487/cf8deae3-6ba2-4dc0-85b2-318dffe5da26)

