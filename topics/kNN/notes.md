## kNN (k-Nearest Neighbors)

### Notes
- Supervised learning!!
    - for **classification** — what our unlabeled data belongs to within existing classes
- $k$ = number of labeled neighbors you "consult"

### Steps with sklearn implementation

Import Block
```python
from sklearn.neighbors import KNeighborsClassifier
```

1. Define kNN based on $k$

```python
kNN = KNeighborsClassifier(n_neighbors=2)
```

2. Fit the kNN to labeled data
```python
kNN.fit(label_data, pt_labels)
```

3. Run kNN — assign labels to unlabeled data
```python
all_labels = kNN.predict(mystery)
```

### Decision Boundaries
- line where the model's prediction switches from one class to another
    - i.e. for $k=7$, kNN finds the 7 nearest labeled points and takes a majority vote. The decision boundary falls where that vote flips