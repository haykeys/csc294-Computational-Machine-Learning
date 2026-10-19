## k-means

Clustering approach; unsupervised
- have model and data but no outputs

### Steps
1. Initialize clusters' centers
    - place $k$ centers (random) or choose $k$ of data points (example code below)

    ```python
    centers = df.sample(2, random_state = 1)
    ```
2. Assign each data point to closest center
    - for each point in data...

    1. Calculate distance to all the centers

    ```python
    distance.cdist(data, centers, 'euclidean')
    ```

    2. Find minimum value of all the distances

    ```python
    np.argmin(dists)
    ```

    3. Assign center with smallest distance to data point

    ```python
    for c in range(iter):
        subset = []
        for i in range(len(data)):
            if clusters[i] == c:
                subset.append(data[i])
            centers_np[c] = np.mean(subset, axis=0)
    ```

    ### Implementing with sklearn

    Import block

    ```python
    import pandas as pd
    import numpy as np

    import matplotlib.pyplot as plt
    import seaborn as sns

    from sklearn.cluster import KMeans
    ```

    ```python
    X = df[['feature1', 'feature2']]

    km = KMeans(n_clusters=3, n_init=10, random_state=1)

    df['cluster'] = km.fit_predict(X)

    # Extract the results
    centers = km.cluster_centers_ 
    wcss = km.inertia_
    ```

    Plot the clusters and their centers:

    ```python
    plt.scatter(X['feature1'], X['feature2'], c=df['cluster'])
    plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=200)
    plt.xlabel('feature1')
    plt.ylabel('feature2')
    plt.show()
    ```

    Choosing $k$ (elbow method): plot WCSS for several values of $k$ and pick the $k$ where the curve stops dropping sharply.

    ```python
    ks = range(1, 11)
    wcss_list = []
    for k in ks:
        km = KMeans(n_clusters=k, n_init=10, random_state=1).fit(X)
        wcss_list.append(km.inertia_)

    plt.plot(ks, wcss_list, marker='o')
    plt.xlabel('k')
    plt.ylabel('WCSS')
    plt.show()
    ```


    ### Determining Goodness
    - Within Cluster Sum of Squares (WCSS)
        - how tight is each cluster?
        - compares each point to its own center
        - decreases as $k$ increases


    - Cluster Separation
        - how far apart the clusters are
        - compares points in one cluster to points in another
        - decreases usually as $k$ increases (because clusters get crowded together)