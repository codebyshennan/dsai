# Hierarchical Clustering

**After this lesson:** you can explain the core ideas in “Hierarchical Clustering” and reproduce the examples here in your own notebook or environment.

## Overview

**Agglomerative** clustering: linkage criteria, dendrograms, and choosing a cut.

## Helpful video

StatQuest overview of K-means clustering.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4b5d3muPQmA" title="K-means Clustering, Clearly Explained" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Quick Reference

```mermaid
graph TD
    subgraph AGG["Agglomerative (bottom-up)"]
        A1["Start: each point\nis its own cluster"]
        A1 --> A2["Merge two closest\nclusters at each step"]
        A2 --> A3["Repeat until\none cluster remains"]
        A3 --> A4["Cut dendrogram at\ndesired level → k clusters"]
    end
    subgraph LINK["Linkage criteria (how to measure 'closest')"]
        L1["Ward\nMinimise within-cluster variance\n(most common; spherical clusters)"]
        L2["Complete\nMax distance between points\n(compact, even clusters)"]
        L3["Average\nMean pairwise distance\n(compromise)"]
        L4["Single\nMin distance (chaining effect)"]
    end
    A2 --> LINK
    subgraph DEND["Reading the dendrogram"]
        D1["Height of merge = distance\nLong vertical lines → natural gap"]
        D1 --> D2["Horizontal cut = chosen k\nCount branches below cut"]
    end
    A4 --> DEND
```

> **Figure (add screenshot or diagram):** A dendrogram with a horizontal dashed line showing where to cut to obtain 3 clusters, with the three resulting cluster branches coloured differently.

Hierarchical clustering is ideal when:
- You want to explore multiple cluster levels
- The natural cluster hierarchy matters
- You don't know the number of clusters in advance

```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Basic usage
clustering = AgglomerativeClustering(n_clusters=3)
labels = clustering.fit_predict(X)

# For dendrogram
Z = linkage(X, method='ward')
dendrogram(Z)
```

For the complete tutorial, see [Clustering Guide](clustering.md).
