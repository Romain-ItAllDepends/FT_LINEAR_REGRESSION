import os

def main():
	print("Compare your training data with the same data, but during prediction generation. (Use test.sh to easily generate predictions.)")
	data = retrieveData()
	prediction = retrievePrediction()
	evaluate(data, prediction)

def evaluate(data, prediction):
	dataDict = {m: p for m, p in data} # Creation of a dictionary (like map in c++)

	totalError = 0
	count = 0

	for m, pricePred in prediction:
		if m in dataDict:
			priceData = dataDict[m]

			totalError += abs(pricePred - priceData) / priceData
			count += 1
	if count == 0:
		print("No data to compare!")
		return 0
	accuracy = (1 - totalError / count) * 100

	print("Accuracy:", accuracy, "%")

def retrievePrediction():
	if not os.path.exists('./result.predict'):
		exit(1)
	if not os.access('./result.predict', os.R_OK):
		exit(1)
	with open('./result.predict', 'r') as file:
		lines = file.read().strip().split('\n')
		file = parseFile(lines)
		if not file:
			print("The prediction file is empty or contains alphanumeric characters!")
			exit(0)
	return file

def retrieveData():
	if not os.path.exists('./data.csv'):
		exit(1)
	if not os.access('./data.csv', os.R_OK):
		exit(1)
	with open('./data.csv', 'r') as file:
		lines = file.read().strip().split('\n')
		file = parseFile(lines)
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
