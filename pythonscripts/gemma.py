from groq import Groq

client = Groq(api_key="<GROQ_API_KEY>")

f = open("release_notes.md", "r+")   
data = f.read()

completion = client.chat.completions.create(
    model="gemma2-9b-it",
    messages=[
        {
            "role": "user",
            "content": "You're a helpful assistant specialized in generating descriptive release notes. Analyze the list of changes between 2 releases which I am going to provide you.  Provide a brief overview of the release highlighting major changes. List each change with a short, clear description. Categorize changes into different headings, for example:- New Features, Improvements, Bug Fixes etc. Maintin a professional yet approachable tone. Do not make any conclusion about how a commit will influence a project if you don't know. Use clear, non-technical language where possible. Use bullet points for individual changes and subheadings for different categories. Always write the date in Month Day Year format. These are the list of changes:\n" + data
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

text = ""
for chunk in completion:
    text += chunk.choices[0].delta.content or ""

f.write("\n"+ text) 
f.close()
