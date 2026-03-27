# K-means Clustering

**After this lesson:** you can explain the core ideas in “K-means Clustering” and reproduce the examples here in your own notebook or environment.

> **Note**: This content has been consolidated into the main clustering guide for a better learning experience.

K-means clustering is covered comprehensively in:

**[Clustering: Finding Natural Groups in Data](clustering.md)**

This guide includes:
- How K-means works
- Step-by-step implementation
- Elbow method for choosing k
- Practical examples and visualizations
- Best practices and common pitfalls

---

## Helpful video

StatQuest overview of K-means clustering.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4b5d3muPQmA" title="K-means Clustering, Clearly Explained" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Quick Reference

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
