import google.generativeai as genai

API_KEY = "AIzaSyDr13fz8mNRLDTED7obgvuxKev3mi5zmzY"
genai.configure(api_key=API_KEY)

def check_grammar(text):
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt =  f"Check the grammar of the following sentence and correct any mistakes:\n\n{text}\n\nIf the grammar is correct, return 'Correct'. Otherwise, return the corrected sentence."

    response = model.generate_content(prompt)
    return response.text



def convert_to_casual(text):
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt =  f"Rewrite the following sentence in a casual tone:\n\n{text}\n\nProvide only the casual version."
    response = model.generate_content(prompt)
    return response.text

def convert_to_formal(text):
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"Convert this casual sentence into a formal sentence:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text
