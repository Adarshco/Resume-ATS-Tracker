import google.generativeai as genai

genai.configure(api_key="AIzaSyCAK7veu4k9hT88E0pUrSPbmILs0vPfLtI")

models = genai.list_models()
for model in models:
    print(model.name)