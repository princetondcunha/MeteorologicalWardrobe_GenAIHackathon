'''Meteorological Wardrobe'''

import getweatherdata
import gptrecommendation
import imagegeneration

date = "November 17"
time = "12 AM"
activity = "Stargazing"

recommendation = gptrecommendation.getrecommendation(getweatherdata.getweather_next5days(44.65,-63.58),date,time,activity)
print("Recommendation: ", recommendation['outfit_recommendation'])
print("Recommendation Illustration: ", imagegeneration.generateimage(recommendation))