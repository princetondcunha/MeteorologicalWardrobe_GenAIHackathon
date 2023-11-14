'''Process Input'''

import json
import os
from openai import OpenAI
import dotenv

dotenv.load_dotenv()
openai_apikey=os.environ.get('OPENAI_APIKEY')

client = OpenAI(api_key=openai_apikey)

def getcoords(location):
    '''Get Coordinates from GPT'''
    system_message = "You are a helpful assistant. When the user gives you a location"
    system_message+= "you should tell the latitude and longitude for that location."
    system_message+= "The Latitude and Longitude must contain max of 2 decimal points."
    system_message+= "The result must be in json"
    system_message+= '''JSON Format should be {"lat": "float","lon":"float"}'''

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": f"{location}",
            }

        ],
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        temperature=0.1
    )

    data = json.loads(chat_completion.choices[0].message.content)
    return data