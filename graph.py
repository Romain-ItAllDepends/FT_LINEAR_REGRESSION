import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import os

def main():
	data = retrieveData()
	prediction = retrievePrediction()
	thetaX, thetaY = retrieveTheta()
	thetaY = thetaX / abs(thetaY)

	x = [price for price, mileage in data]
	y = [mileage for price, mileage in data]
	w = [price for price, mileage in prediction]
	z = [mileage for price, mileage in prediction]

	plt.title("Predictions graphic")

	plt.scatter(x, y, label="Data")
	plt.scatter(w, z, marker='^', label="Prediction")
	plt.plot([thetaY, 0], [0, thetaX], color='green', label="Regression line")

	ax = plt.gca() # Disable scientific notation for coordinates
	ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
	ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))

	plt.ylabel("Price")
	plt.xlabel("Mileage")
	plt.xlim(0, max(x))
	plt.ylim(0, max(y))

	plt.legend()
	plt.grid()
	plt.show()

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

def retrieveTheta():
	if not os.path.exists('./theta.predict'):
		return 0.0, 0.0
	if not os.access('./theta.predict', os.R_OK):
		exit(1)
	with open('./theta.predict', 'r') as file:
		theta = file.read().split('\n')
	return float(theta[0]), float(theta[1])

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
