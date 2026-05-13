import sys
import csv
import os

minMileage, minPrice = 0, 0
maxMileage, maxPrice = 0, 0
adaptiveLearningRate = False

def main():
    parseParameter()
    lines = retrieveData()
    normedData = normalize(lines)
    theta = train(normedData[0], normedData[1])
    theta = denormalize(theta)
    saveTheta(theta)

def parseParameter():
    global adaptiveLearningRate
    if len(sys.argv) > 1 and sys.argv[1] == '-lr':
        adaptiveLearningRate = True

def retrieveData():
    if not os.path.exists('./data.csv'):
        exit(1)
    if not os.access('./data.csv', os.R_OK):
        exit(1)
    with open('./data.csv', 'r') as file:
        lines = file.read().split('\n')
        values = [line.split(',') for line in lines if parseHeader(line)]
        values = [[int(x), int(y)] for x, y in values]
    return values

def saveTheta(theta):
    with open('./theta.predict', 'w') as file:
        file.write(str(theta[0]))
        file.write('\n')
        file.write(str(theta[1]))

def minValues(list):
    minMileage = list[0][0]
    minPrice = list[0][1]
    for i in range (0, len(list)):
        if list[i][0] < minMileage:
            minMileage = list[i][0]
        if list[i][1] < minPrice:
            minPrice = list[i][1]
    return minMileage, minPrice

def maxValues(list):
    maxMileage = 0
    maxPrice = 0
    for i in range(0, len(list)):
        if list[i][0] > maxMileage:
            maxMileage = list[i][0]
        if list[i][1] > maxPrice:
            maxPrice = list[i][1]
    return maxMileage, maxPrice

def normalize(list):
    global minMileage, maxMileage, minPrice, maxPrice
    minMileage, minPrice = minValues(list)
    maxMileage, maxPrice = maxValues(list)

    normedMileage = [(x[0] - minMileage) / (maxMileage - minMileage) for x in list]
    normedPrice = [(x[1] - minPrice) / (maxPrice - minPrice) for x in list]

    return normedMileage, normedPrice

def denormalize(theta):
    global minMileage, maxMileage, minPrice, maxPrice

    theta1_real = theta[1] * (maxPrice - minPrice) / (maxMileage - minMileage)
    theta0_real = theta[0] * (maxPrice - minPrice) + minPrice - theta1_real * minMileage

    return theta0_real, theta1_real

def train(mileage, price):
    tmpTheta0, tmpTheta1 = 0.0, 0.0
    length = len(mileage)
    lr = 0.1

    for i in range (0, 100000):
        if adaptiveLearningRate: # Need global
            lr = 0.1 / (1 + 0.0001 * i)
        correction0 = lr * 1 / length * sum([estimatePrice(m, tmpTheta0, tmpTheta1) - p for m, p in zip(mileage, price)])
        correction1 = lr * 1 / length * sum([(estimatePrice(m, tmpTheta0, tmpTheta1) - p) * m for m, p in zip(mileage, price)])
        tmpTheta0 -= correction0
        tmpTheta1 -= correction1
    return tmpTheta0, tmpTheta1

def estimatePrice(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

def parseHeader(line):
    if len(line) == 0:
        return False
    for c in line:
        if c.isalpha():
            return False
    return True

main()