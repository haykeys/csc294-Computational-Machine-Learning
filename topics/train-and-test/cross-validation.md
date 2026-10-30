## Cross-Validation

### Training and Testing

only in **supervised** machine learning
(why? because in unsupervised, we don't have answers; don't know ground truth)

- **Underfitting**: when model not adequately fit to the training data — happens when high training error
- **Overfitting**: when model fit too perfectly to the training data; therefore, cannot be generalized (cannot make predictions to new data) — happens when training error is low and testing error is high

    - **training error**: how well the model fits the data it learned from
    - **testing error**: how well it predicts data it has never seen

**Bias/Variance trade off**

- Every simplification of data will have bias; the more simplistic the model, the more bias
- the more complicated the model, the slightest change in the data will cause huge changes in the model (variance)

### Cross-Validation

- Everything gets to be in testing data!
- We learn: How well would the model do on "new" (unseen) data?
    - true test error = computationally not feasible... we try to approximate this as closely as possible

**Steps:**

1. Choose model
2. Divide data into $k$ equal pieces
3. for $i$ in range($k$):
    - select the $i$ th piece of dataset to be test set, rest are training set
    - fit model on training set
    - compute error (i.e. MSE) = $i$ th test error
    - add $i$ th test error to list of test errors
4. Compute average of test errors (= Cross-Validated Error)

**Use Cases:**
- making decisions about hyperparameters (i.e. degree of polynomial)
- comparing 2 models

### Leave One Out Cross Validation (LOOCV)

- when $k$ = number of data points
- computationally expensive
- test = 1 data point, train = rest of the data

Pulling one data point out:

```python
test_data = mystery_np[i:i+1, :] # index trick

train_ind = list(set(range(n_data)).difference([i]))
train_data = mystery_np[train_ind, :]
```

Can also do:

```python
test_data = mystery_np[i, :].reshape(1, -1) # does the same thing as index trick
```

### Notes

Helper function used to compute MSE:
```python
def compute_mse(truth_vec, predict_vec):
    return np.mean((truth_vec - predict_vec)**2)
```