import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    data = retrieveData()
    prediction = retrievePrediction()

    fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    ax.set_title("Prediction graphic")
    ax.plot(np.arange(len(data)), data, 'd', label='data')
    ax.plot(np.arange(len(prediction)), prediction, 'd', label='prediction')
    ax.set_ylabel("Mileage")
    ax.set_xlabel("Price")
    ax.legend()
    plt.show()

def retrievePrediction():
    if not os.path.exists('./result.predict'):
        return 0.0, 0.0
    if not os.access('./result.predict', os.R_OK):
        exit(1)
    with open('./result.predict', 'r') as file:
        res = file.read().split('\n')
    return res

def retrieveData():
    if not os.path.exists('./data.csv'):
        exit(1)
    if not os.access('./data.csv', os.R_OK):
        exit(1)
    with open('./data.csv', 'r') as file:
        lines = file.read().split('\n')
        file = parseFile(lines)
        print(file)
        if not file:
            print("The data file is empty or contains alphanumeric characters!")
            exit(0)
    return file

def parseFile(file):
    fileParsed = []
    for line in file:
        try:
            x, y = line.split(',')
            fileParsed.append((int(x), int(y)))
        except:
            continue
    return fileParsed

main()