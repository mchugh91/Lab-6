__author__ = 'Ciaran'

from math import *

def findDist(lat, long, lat2, long2):


    latAngle = 90 - lat
    lat2Angle = 90 - lat2

    latrad = latAngle * (2*pi)/360
    longrad = long * (2*pi)/360
    lat2rad = lat2Angle * (2*pi)/360
    long2rad = long2 * (2*pi)/360

    distance = acos(sin(latrad) * sin(lat2rad) * cos(longrad-long2rad) + (cos(latrad) * cos(lat2rad))) * 6371
    return distance


def main():

    Dublin = [53.42133, -6.270075, "DUB"]
    Heathrow = [51.4775, -0.461389, "LHR"]
    JohnFKennedy = [40.639751, -73.778925, "JFK"]
    Aalborg = [57.092789, 9.849164, "AAL"]
    CharlesDGaulle =[49.012779, 2.55, "CDG"]
    SydneyIntl = [-33.946111, 151.177222, "SYD"]
    airports = [Dublin, Heathrow, JohnFKennedy, Aalborg, CharlesDGaulle, SydneyIntl]

    for x in range(0, len(airports)):
        airportA = airports[x]
        for y in range(0, len(airports)):
            airportB = airports[y]
            print("The distance between", airportA[2], "and", airportB[2], "is",
                  int(findDist(airportA[0], airportA[1], airportB[0], airportB[1])))



main()