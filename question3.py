__author__ = 'Ciaran'

from math import *

def getDistanceBetweenAirports(airportCode1, airportCode2):

    Dublin = [53.42133, -6.270075, "DUB"]
    Heathrow = [51.4775, -0.461389, "LHR"]
    JohnFKennedy = [40.639751, -73.778925, "JFK"]
    Aalborg = [57.092789, 9.849164, "AAL"]
    CharlesDGaulle =[49.012779, 2.55, "CDG"]
    SydneyIntl = [-33.946111, 151.177222, "SYD"]
    airports = [Dublin, Heathrow, JohnFKennedy, Aalborg, CharlesDGaulle, SydneyIntl]

    for x in range(0, len(airports)):
        ap1 = airports[x]
        if airportCode1 == ap1[2]:
            airportA = airports[x]
        ap2 = airports[x]
        if airportCode2 == ap2[2]:
            airportB = airports[x]

    lat = airportA[0]
    long = airportA[1]
    lat2 = airportB[0]
    long2 = airportB[1]

    latAngle = 90 - lat
    lat2Angle = 90 - lat2

    latrad = latAngle * (2*pi)/360
    longrad = long * (2*pi)/360
    lat2rad = lat2Angle * (2*pi)/360
    long2rad = long2 * (2*pi)/360

    distance = acos(sin(latrad) * sin(lat2rad) * cos(longrad-long2rad) + (cos(latrad) * cos(lat2rad))) * 6371
    return distance

def main():

    airportCode1 = input("Enter first airport code:").upper()
    airportCode2 = input("Enter second airport code:").upper()

    print("The distance between", airportCode1, "and", airportCode2, "is", int(getDistanceBetweenAirports(airportCode1, airportCode2)))

main()