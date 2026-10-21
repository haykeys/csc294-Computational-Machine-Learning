## PCA (Principal Component Analysis)

### Notes
- dimension of data = number of variables
    - **dimensional reduction**: check that the number of rows (observations) are not changing but the number of columns are decreasing
- find what's most important and throw everything else out
- PCA looks for the directions of greatest spread of our data
    - eigenvalues: how much spread?
    - eigenvectors: direction of spread?
- principal component is associated with the largest eigenvector
- **the goal is to lower the dimension**
    - we use eigenvalues to choose dimension
- Why reduce dimension? with more variablesk we start to lose the idea of close & far... (think of $k$-means which relies on distances — we reduce dimension to look at how close the points are, so that we can find groups and patterns)

### Requirements
- standardized data
    - need a covariance matrix (= how do differentvariables vary together; how the attributes of data work together or not)

### Standardized data?
- means that data is centered around 0
- "each variable is as important as every other variable"

$$Var_{std} = \frac{Var-Var_{mean}}{Var_{sd}}$$

### sklearn Implementation

```python
from sklearn.decomposition import PCA

pca_data = PCA(n_components=2)
pfit = pca_alg.fit(data_std)

print("Shape of the resulting components\n", pfit.components_.shape)
print("\n Actual components \n",pfit.components_)

pca_data = pca_alg.transform(data_std)
```

### .fit() vs .transform()

- `fit()`: transition matrix — "carries" our data from a higher dimension to the lower one
    - applies the PCA attributes to the data (but doesn't actually modify our dara)
- `transform()`: actually carry out the transformation