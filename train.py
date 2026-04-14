import math
import csv
import os

def main():
    lines = retrieveData()
    theta = train(lines)
    print(theta)

def retrieveData():
    if not os.path.exists('./data.csv'):
        exit(1)
    if not os.access('./data.csv', os.R_OK):
        exit(1)
    with open('./data.csv', 'r') as file:
        lines = file.read().split('\n')
        values = [line.split(',') for line in lines]
    return values

def train(lines):
    tmpTheta0 = 0.001 * 1 / len(lines) * [estimatePrice(line[0]) - price[1] for line in lines]
    tmpTheta1 = 0.001 * 1 / len(lines) * [estimatePrice(line[0]) - price[1] for line in lines]

main()