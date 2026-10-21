# CSC294 — Computational Machine Learning Portfolio

## Topics

| # | Topic | Contents |
|---|-------|--------|
| 01 | [k-means](topics/k-means/) | [notes](topics/k-means/notes.md) |
| 02 | [PCA](topics/PCA/) | subtopics |
| 03 | [SVD](topics/SVD/) | subtopics |
| 04 | [kNN](topics/kNN/) | subtopics |
| 05 | [Linear Regression](topics/linear-regression/) | [notes](topics/linear-regression/notes.md) |
| 06 | [Gradient Descent](topics/gradient-descent/) | [notes](topics/gradient-descent/notes.md) |

## Import Block

```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
```

## Summary Table

<table>
<thead>
<tr>
<th>Method/Algorithm</th>
    <th>Type</th>
    <th>Inputs</th>
    <th>Numbers set/involved</th>
</tr>
</thead>
<tbody>
    
<tr>
<th>kNN</th>
    <td>supervised</td>
    <td>$k$ (number of labeled neighbors consulted)</td>
    <td>labels for the rest of the data </td>
</tr>

<tr>
<th>k-means</th>
    <td>unsupervised</td>
    <td>$k$ (number of clusters), unlabeled data</td>
    <td>cluster assignment for each point and the $k$ centroids, chosen to minimize WCSS</td>
</tr>
<tr>
<th>PCA</th>
    <td>unsupervised</td>
    <td>number of components to keep (or a target % of variance explained), centered data</td>
    <td>principal component directions, variance explained by each component, and each point's scores (coordinates along the components)</td>
</tr>
<tr>
<th>SVD</th>
    <td>unsupervised</td>
    <td>data matrix $X$ ($n \times d$); optionally a rank $r$ for truncated SVD</td>
    <td>$X = U \Sigma V^\top$: singular values (diagonal of $\Sigma$), left singular vectors $U$, right singular vectors $V$</td>
</tr>
<tr>
<th>Spectral Clustering</th>
    <td>unsupervised</td>
    <td> </td>
    <td> </td>
</tr>
<tr>
<th>Regression</th>
    <td>Supervised</td>
    <td> </td>
    <td> </td>
</tr>
</tbody>
</table>
