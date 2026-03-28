# K-means Clustering

**After this lesson:** you can explain the core ideas in “K-means Clustering” and reproduce the examples here in your own notebook or environment.

## Overview

**K-means**: Lloyd's algorithm, centroids, when spherical clusters are a reasonable assumption, and common failure modes.

## Helpful video

StatQuest overview of K-means clustering.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4b5d3muPQmA" title="K-means Clustering, Clearly Explained" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Quick Reference

```mermaid
graph TD
    INIT["1. Choose k\nInitialise k centroids\n(random or k-means++)"]
    INIT --> ASSIGN["2. Assign\nEach point → nearest centroid\n(Euclidean distance)"]
    ASSIGN --> UPDATE["3. Update\nRecompute centroid\nas cluster mean"]
    UPDATE --> CHECK{Centroids\nchanged?}
    CHECK -->|Yes| ASSIGN
    CHECK -->|No| DONE["Converged\nReturn labels + centroids"]

    subgraph LIMITS["Common failure modes"]
        F1["Sensitive to initialisation\nFix: k-means++ (sklearn default)"]
        F2["Assumes spherical clusters\nFix: DBSCAN or GMM for irregular shapes"]
        F3["Must specify k\nFix: Elbow / silhouette to choose k"]
        F4["Sensitive to scale\nFix: StandardScaler before fitting"]
    end
```

K-means is ideal when:
- You know the approximate number of clusters
- Clusters are roughly spherical
- Clusters have similar sizes

```python
from sklearn.cluster import KMeans

# Basic usage
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)
```

For the complete tutorial, see [Clustering Guide](clustering.md).
