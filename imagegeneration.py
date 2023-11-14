'''Image Generation'''

import os
from openai import OpenAI
import dotenv

dotenv.load_dotenv()
openai_apikey=os.environ.get('OPENAI_APIKEY')

client = OpenAI(api_key=openai_apikey)

def generateimage(gptresponse):
    '''Generate Image'''
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Generate an animated character wearing the recommended clothes with background weather as per the data: {gptresponse}. Don't generate any text",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url