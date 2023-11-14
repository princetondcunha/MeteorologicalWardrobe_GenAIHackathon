'''Meteorological Wardrobe'''

import getweatherdata
import gptrecommendation
import imagegeneration
import processinput

date = "November 17"
time = "12 AM"
activity = "Stargazing"
location = "Halifax"

coords = processinput.getcoords(location)

recommendation = gptrecommendation.getrecommendation(getweatherdata.getweather_next5days(coords['lat'],coords['lon']),date,time,activity)
print("Recommendation: ", recommendation['outfit_recommendation'])
#print("Recommendation Illustration: ", imagegeneration.generateimage(recommendation))