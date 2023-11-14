'''Meteorological Wardrobe'''

import getweatherdata
import gptrecommendation

print(gptrecommendation.getrecommendation(getweatherdata.getweather_next5days(44.65,-63.58),"November 15","9 AM","hiking"))


