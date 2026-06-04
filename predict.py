import os
import sys

restart = False

def main():
    parseParameter()
    theta = retrieveTheta()
    mileage = input("What is the vehicle's mileage?\n") # Input str segfault
    res = estimatePrice(theta, mileage)
    savePredictions(res, mileage)
    if restart:
        main()
    else:
        exit(0)
    quit = input("Would you like to quit? (y/n)\n")
    if quit == 'y':
        exit(0)
    
    
def parseParameter():
    global restart
    if len(sys.argv) > 1 and sys.argv[1] == '-r':
        restart = True

def retrieveTheta():
    if not os.path.exists('./theta.predict'):
        return 0.0, 0.0
    if not os.access('./theta.predict', os.R_OK):
        exit(1)
    with open('./theta.predict', 'r') as file:
        theta = file.read().split('\n')
    return float(theta[0]), float(theta[1])

def estimatePrice(theta, mileage):
    res = int(theta[0] + (theta[1] * float(mileage)))
    print(res)
    return res

def savePredictions(res, mileage):
    with open('./result.predict', 'a') as file:
        file.write(f"\n{mileage},{res}")

main()