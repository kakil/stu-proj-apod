import requests
import dotenv
import os
import streamlit as st


# HTTP Request
# GET https://api.nasa.gov/planetary/apod
# https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
# Response: Dict: copyright, date, explanation, hdurl, media_type,
# service_version, title, url (image url)

dotenv.load_dotenv()


def get_json():
    api_key = os.getenv("NASA_API_KEY")
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    response = requests.get(url)

    # returns the json response
    return response.json()
    # print(type(json))
    # print(json)
    #
    # title = json.get("title")
    # description = json.get("explanation")
    # image_url = json.get("url")
    # print(title)
    # print(description)
    # print(image_url)


def get_image(url):
    response = requests.get(url)
    with open("apod.jpg", "wb") as file:
        file.write(response.content)


json = get_json()
title = json.get("title")
get_image(json.get("url"))
description = json.get("explanation")

st.header(title)
st.image("apod.jpg")
st.write(description)




