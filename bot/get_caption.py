from google import genai

def get_caption(prompt):
    # TODO Add api key
    client = genai.Client(api_key='api_key')

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    res =  response.text
    return res