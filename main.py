'''Meteorological Wardrobe'''

import getweatherdata
import gptrecommendation
import imagegeneration

date = "November 15"
time = "9 AM"
activity = "Camping"

recommendation = gptrecommendation.getrecommendation(getweatherdata.getweather_next5days(44.65,-63.58),date,time,activity)
print("Recommendation: ", recommendation['outfit_recommendation'])
print("Recommendation Illustration: ", imagegeneration.generateimage(recommendation))