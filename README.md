# FT_LINEAR_REGRESSION

This project will be your first steps into AI and Machine Learning. You're going to start with a simple, basic machine learning algorithm. You will have to create a program that predicts the price of a car by using a linear function train with a gradient descent algorithm. 

## LANGUAGE

In this project, you are free to use whatever language you want.
You are also free to use any libraries you want as long as they do not do all the work
for you. For example, the use of Python’s numpy.polyfit is considered cheating.

You should use a language that allows you to easily visualize your
data : it will be very helpful for debugging.

- Python

## SELECTED LIBRARIES

- math
- csv
- os

## FIRST PROGRAM

Linear function.

The first program will be used to predict the price of a car for a given mileage.
When you launch the program, it should prompt you for a mileage, and then give
you back the estimated price for that mileage. The program will use the following
hypothesis to predict the price :

estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)

Before running the training program, theta0 and theta1 will be set to 0.

## SECOND PROGRAM

Regression linear.

The second program will be used to train your model. It will read your dataset file
and perform a linear regression on the data.
Once the linear regression has completed, you will save the variables theta0 and
theta1 for use in the first program.
You will be using the following formulas :

tmpθ0 = learningRate ∗ 1/m m−1∑i=0(estimateP rice(mileage[i]) − price[i])

tmpθ1 = learningRate ∗ 1/m m−1∑i=0(estimatePrice(mileage[i]) − price[i]) ∗ mileage[i])

I let you guess what m is :)
Note that the estimatePrice is the same as in our first program, but here it uses
your temporary, most recently computed theta0 and theta1.
Also, don’t forget to simultaneously update theta0 and theta1

learningRate is a manual value.

m is the number of line in data file.

### GLOBAL INFORMATION

θ (theta) is an unknown number.
θ = 0 (basic stat)
The downward gradient is the method for prediction training.

Gradient descent algorithm is the entire algorithm.

### FIRST PROGRAM INFORMATION

Just a linear function.

### SECOND PROGRAM INFORMATION

Using the symbol ∑, we vary i from the bottom number to the top number, and we add the values ​​obtained at each step.

Exemple:

3
∑i                 ->     0 + 1 + 2 + 3 = 6
i=0
