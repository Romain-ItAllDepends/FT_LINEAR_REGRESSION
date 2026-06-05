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

- matplotlib (ticker, pyplot)
- math
- sys
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

Linear regression.

The second program will be used to train your model. It will read your dataset file
and perform a linear regression on the data.
Once the linear regression has completed, you will save the variables theta0 and
theta1 for use in the first program.
You will be using the following formulas :

<img width="718" height="132" alt="image" src="https://github.com/user-attachments/assets/0e775ddd-d9a1-4d56-9618-981f762eb8dc" />

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

normalize:

Set each value between 0 and 1 based on min and max value.

denormalize:

Denormalization is applied to return values to their original scale after training on normalized data.

Mean squared error:

The MSE is a measure of the quality of an estimator and used to optimize the model. As it is derived from the square of Euclidean distance, it is always a positive value that decreases as the error approaches zero. (This is the calculation given in the problem statement for the training program)

The goal is to minimize the error (MSE), ideally as close to 0 as possible.

### PARAMETERS

predict.py

-r ====> Restart until you send 'y' when you will quit.

train.py

-lr ====> Set adaptive learning rate (more precise)

graph.py

accuracy.py

It only works when using the same data as that used for training.

### PROGRAM OBJECTIVE

Predicting the price of a vehicle from its mileage using a linear regression model trained on a dataset containing mileage/price pairs.

### EXPLAINATION OF THE ALGORITHM

Train:

The data is first normalized to put them on a common scale: the minimum is reduced to 0, the maximum to 1, and the other values ​​are recalculated proportionally between these two limits.

Next, as requested in the subject, we use the Mean Squared Error (MSE), which allows us to measure the average error between the predicted values ​​and the actual values ​​of the model.

Since we have normalized the data, we need to denormalize our thetas to make them usable. To do this, we apply the inverse of the normalization transformation.

Predict:

To make a prediction, it is sufficient to use the linear function defined in the subject, applying the parameters θ obtained during the training phase.

