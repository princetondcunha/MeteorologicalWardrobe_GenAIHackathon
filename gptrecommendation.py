'''Get Recommendations from GPT'''

import json
import os
from openai import OpenAI
import dotenv

dotenv.load_dotenv()
openai_apikey=os.environ.get('OPENAI_APIKEY')

client = OpenAI(api_key=openai_apikey)

def getrecommendation(weather_data,date,time,activity):
    '''Get Recommendations from GPT'''
    system_message = "You are a helpful assistant, when the user gives you a weather data,"
    system_message+= f"you should tell them what to wear for the date {date}, {time} and activity - {activity}"
    system_message+= "based on the weather data they provided"
    system_message+= "The data user provided will be in json and the temperature is in kelvin."
    system_message+= "The result must be in json"
    system_message+= '''JSON Format should be {"weather_description": "string","outfit_recommendation":"string"}'''
    system_message+= "Never mention any temperature"

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": f"{weather_data}",
            }

        ],
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        temperature=0.1
    )

    data = json.loads(chat_completion.choices[0].message.content)
    return data
