import math
import csv
import os

def main():
    retrieveTheta()

def retrieveTheta():
    with os.open('./theta.predict', 'r') as file:
        content = file.read()