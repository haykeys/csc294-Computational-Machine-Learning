### Linear Regression (Supervised)

```python
from sklearn import linear_model

# Set up the particulars for the linear regression
lm2 = linear_model.LinearRegression()

# Fit the linear regression to the data
model2 = lm2.fit(input2,output2)

# Extract the coefficients
m2 = lm2.coef_[0]
b2 = lm2.intercept_
```