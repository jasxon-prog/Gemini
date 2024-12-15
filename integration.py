import google.generativeai as genai

API_KEY = 'AIzaSyCAc5Mm1EpkKeMBU_4QNBMw9Nt9x7oyY9c'

def make_conversetion(text: str):
    genai.configure(api_key="AIzaSyCAc5Mm1EpkKeMBU_4QNBMw9Nt9x7oyY9c")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(text)
    return response.text

#print(make_conversetion('Give me about Uzbekistan'))