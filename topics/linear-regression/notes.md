## Linear Regression

### Notes
- We try to guess the output value given a set of input variables (Supervised!)
    - $y=mx+b$

General Process of Supervised ML (with an example):
1. Decide task (prediction or classification) and select model/algorithm
    - prediction using simple linear regression
2. Fit algorithm/model using part of available data with given outputs
    - `performance = m * neuroticism + b`: used neuroticism score as input and performance score as output to determine $m$ and $b$
3. Check model against "new" data
    - make a prediction for a new person using only their input value (neuroticism score) and check output against the true performance score


### sklearn Implementation (Training)

```python
from sklearn import linear_model

input = data[["var"]].to_numpy()
output = data[["out"]].to_numpy()

# Set up the particulars for the linear regression
lm = linear_model.LinearRegression()

# Fit the linear regression to the data
model = lm2.fit(input2,output2)

# Extract the coefficients
m = lm.coef_[0]
b = lm.intercept_
```

### Visualization

```python
plt.scatter(input, output, s = 50)

# Plotting your particular model/guessing function, example:
x = np.linspace(np.min(input)-1, np.max(input)+2.5, 1000)

plt.plot(x, m*x+b, linestyle='dashed')
```

### Evaluating Model (Testing)

- Using `predict()` 

Example: Selected 2 employees to build model, check predictions for all employees

```python
test_inds = list(set(list(range(1000))) - set(inds2))

# Create the subset of all employees EXCEPT the two selected employees to build model
emp_testset = employee.iloc[test_inds,:]

neuro = emp_testset[["neuroticism"]].to_numpy()
perform = emp_testset[["performance"]].to_numpy()

predict2 = lm2.predict(neuro)
```
- Calculating error

```python
# Error for each individual person: 
error2_by_emp = np.abs(predict2 - perform)**2

# Add up all the errors for a notion of the total error: 
total_error2 = np.sum(error2_by_emp)

# Find the average of how off our predictions are:
average_mistake2 = total_error2/(1000-2)

# or... finding the average error directly:
average_mistake2 = np.mean(np.abs(predict2 - perform)**2)
```
- Compute training vs. testing error

```python
pred2 = lm2.predict(input2)

# Compute the average of the difference between the 
# predictions and the real output (ie. from the data)
te2 = np.mean(np.abs(pred2 - output2)**2)

# Repeat the above process for lm4 (model made with 4 employees, instead of 2):

pred4 = lm4.predict(input4)
te4 = np.mean(np.abs(pred4 - output4)**2)
```