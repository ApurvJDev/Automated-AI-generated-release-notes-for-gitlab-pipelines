import google.generativeai as genai

genai.configure(api_key="<GEMINI_API_KEY>")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

f = open("release_notes.md", "r+")   
data = f.read()

response = chat_session.send_message("You’re a helpful assistant specialized in generating descriptive release notes. Analyze the list of changes between 2 releases which I am going to provide you.  Provide a brief overview of the release highlighting major changes. List each change with a short, clear description. Categorize changes into different headings, for example:- New Features, Improvements, Bug Fixes etc. Maintin a professional yet approachable tone. Do not make any conclusion about how a commit will influence a project if you don't know. Use clear, non-technical language where possible. Use bullet points for individual changes and subheadings for different categories. Always write the date in Month Day Year format. These are the list of changes:\n "+ data)

f.write("\n"+response.text)

f.close()
