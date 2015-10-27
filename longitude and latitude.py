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
    lat = float(input("Enter latitude of first point:"))
    long = float(input("Enter longitude of first point:"))
    lat2 = float(input("Enter latitude of second point:"))
    long2 = float(input("Enter longitude of second point:"))
    print(int(findDist(lat, long, lat2, long2)))

main()