import os

def main():
    theta = retrieveTheta()
    mileage = input("What is the vehicle's mileage?\n")
    estimatePrice(theta, mileage)

def retrieveTheta():
    if not os.path.exists('./theta.predict'):
        return 0.0, 0.0
    if not os.access('./theta.predict', os.R_OK):
        exit(1)
    with open('./theta.predict', 'r') as file:
        theta = file.read().split('\n')
    return float(theta[0]), float(theta[1])

def estimatePrice(theta, mileage):
    res = theta[0] + (theta[1] * float(mileage))
    print(res)

main()