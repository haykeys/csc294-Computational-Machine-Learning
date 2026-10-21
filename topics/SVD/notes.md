## SVD (Singular Value Decomposition)

### Notes

- Also for dimension reduction 
    - Difference from PCA is that SVD works on almost every matrix (can be performed on sparse data)
    - but a sense of importance on each variable is based on the span of variable
- goal of SVD is to find the matrices $U$, $S$, and $V$, such that $D = USV^t$. 
    - decompose $D$ into 3 smaller representations of our data

$$D = m \times n$$
$$U = m \times m$$
$$S = m \times n$$
$$V = n \times n$$

- we use the pieces of matrix decomposition to perform a dimension reduction (just like PCA)
- doesn't require preprocessing of data

### Implementation

```python
U, S, Vt = np.linalg.svd(justnum,full_matrices=True)
```