import sys
import os

class Trainer:
	def __init__(self, adaptiveLearningRate):
		self.minMileage = 0
		self.maxMileage = 0
		self.minPrice = 0
		self.maxPrice = 0
		self.adaptiveLearningRate = adaptiveLearningRate

	def normalize(self, data):

		self.minMileage, self.minPrice = minValues(data)
		self.maxMileage, self.maxPrice = maxValues(data)

		normedMileage = [(x[0] - self.minMileage) / (self.maxMileage - self.minMileage) for x in data]
		normedPrice = [(x[1] - self.minPrice) / (self.maxPrice - self.minPrice) for x in data]

		return normedMileage, normedPrice

	def denormalize(self, theta):

		theta1Real = theta[1] * (self.maxPrice - self.minPrice) / (self.maxMileage - self.minMileage)
		theta0Real = theta[0] * (self.maxPrice - self.minPrice) + self.minPrice - theta1Real * self.minMileage

		return theta0Real, theta1Real

	def train(self, mileage, price):
		tmpTheta0, tmpTheta1 = 0.0, 0.0
		length = len(mileage)
		lr = 0.1

		for i in range (0, 100000):
			if self.adaptiveLearningRate:
				lr = 0.1 / (1 + 0.0001 * i)
			correction0 = lr * 1 / length * sum([estimatePrice(m, tmpTheta0, tmpTheta1) - p for m, p in zip(mileage, price)])
			correction1 = lr * 1 / length * sum([(estimatePrice(m, tmpTheta0, tmpTheta1) - p) * m for m, p in zip(mileage, price)])
			tmpTheta0 -= correction0
			tmpTheta1 -= correction1
		return tmpTheta0, tmpTheta1


def main():
	param = Trainer(parseParameter())

	lines = retrieveData()
	normedData = param.normalize(lines)
	theta = param.train(normedData[0], normedData[1])
	theta = param.denormalize(theta)
	saveTheta(theta)

def parseParameter():
	if len(sys.argv) > 1 and sys.argv[1] == '-lr':
		return True
	return False

def retrieveData():
	if not os.path.exists('./data.csv'):
		exit(1)
	if not os.access('./data.csv', os.R_OK):
		exit(1)
	with open('./data.csv', 'r') as file:
		lines = file.read().split('\n')
		file = parseFile(lines)
		if not file:
			print("The data file is empty or contains alphanumeric characters!")
			exit(0)
	return file

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

def estimatePrice(mileage, theta0, theta1):
	return theta0 + (theta1 * mileage)

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
