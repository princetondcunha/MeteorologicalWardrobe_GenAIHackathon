import streamlit as st
import requests
from openai import OpenAI
import json


# Function to fetch data from an API

def getlatlon(city, countrycode):
    '''Get Latitude & Longitude'''
    prompt_message = f"Give me the latitude and longitude for {city}, {countrycode} with two digit after the point in json format"
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt_message,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return response.choices[0].message.content

# Streamlit app layout
def main():
    st.title("City Information App")

    # Input fields

    city = st.text_input("Enter city name")
    country_code = st.selectbox("Select country code", ["US", "CA", "UK", "AU", "DE", "FR", "JP"])
    five_days_data_checked = st.checkbox("For five days suggestion")
    #latitude_longtitude = json.loads(getlatlon(city, country_code))


    # Button to fetch data
    if st.button("Show Data"):
        if city and country_code:
            if not five_days_data_checked:
                data = getweather_today('-79.416', "43.7")
                output_data = Generate_desc(data)
                st.write(output_data[0])
                first_data = output_data[0]
                url = Generate_image(next(iter(first_data.items())))
                st.image(url, caption="Image from URL")
                #st.write(data)  # Display raw data as an example
                # You can add more code here to display pictures and formatted data
            else:
                data = getweather_next7days('-79.416', "43.7")
                #st.write(data)
                output_data = Generate_desc(data)
                first_data = output_data[0]
                url = Generate_image(next(iter(first_data.items())))
                st.write(output_data[0])
                st.image(url, caption="Image from URL")
        else:
            st.error("Please fill in all fields")





if __name__ == "_main_":
    main()