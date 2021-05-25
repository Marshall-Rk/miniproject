#!/usr/bin/env python
import json
import requests
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__ == '__main__':
    speak("news of the day")
    url = "http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=801e203d43da4bfa95162024af770d44"
    news = requests.get(url).text
    news = json.loads(news)

    arts=news['articles']
    for articles in arts:
        speak(articles['title'])
        speak("now moving on towards the next news")



