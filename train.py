import csv
import os

def main():
    lines = retrieveData()
    theta = train(lines)
    saveTheta(theta)

def retrieveData():
    if not os.path.exists('./data.csv'):
        exit(1)
    if not os.access('./data.csv', os.R_OK):
        exit(1)
    with open('./data.csv', 'r') as file:
        lines = file.read().split('\n')
        values = [line.split(',') for line in lines if parseHeader(line)]
    return values

def saveTheta(theta):
    with open('./theta.predict', 'w') as file:
        file.write(str(theta[0]))
        file.write('\n')
        file.write(str(theta[1]))

def train(lines):
    tmpTheta0, tmpTheta1 = getTheta()
    for i in range (0, 10000):
        tmpTheta0 -= 0.001 * 1 / len(lines) * sum([estimatePrice(float(line[0]), tmpTheta0, tmpTheta1)- float(line[1]) for line in lines])
        tmpTheta1 -= 0.001 * 1 / len(lines) * sum([(estimatePrice(float(line[0]), tmpTheta0, tmpTheta1) - float(line[1])) * float(line[0]) for line in lines])
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

def getTheta():
    if not os.path.exists('./theta.predict'):
        return 0.0, 0.0
    if not os.access('./theta.predict', os.R_OK):
        exit(1)
    with open('./theta.predict', 'r') as file:
        theta = file.read().split('\n')
    return float(theta[0]), float(theta[1])

main()