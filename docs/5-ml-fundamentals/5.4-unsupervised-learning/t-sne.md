# t-SNE (t-Distributed Stochastic Neighbor Embedding)

**After this lesson:** you can explain the core ideas in “t-SNE (t-Distributed Stochastic Neighbor Embedding)” and reproduce the examples here in your own notebook or environment.

## Overview

Focus on **t-SNE** mechanics and interpretation—neighbor preservation, not cluster sizes or distances between clusters.

## Helpful video

StatQuest overview of K-means clustering.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4b5d3muPQmA" title="K-means Clustering, Clearly Explained" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Quick Reference

```mermaid
graph TD
    subgraph TSNE["t-SNE mechanics"]
        T1["Compute pairwise\nSimilarities in high-D\n(Gaussian kernel → P_ij)"]
        T1 --> T2["Initialise 2D / 3D\nembedding randomly"]
        T2 --> T3["Compute similarities\nin low-D\n(Student-t kernel → Q_ij)"]
        T3 --> T4["Minimise KL divergence\nbetween P and Q\nvia gradient descent"]
        T4 --> T5["Repeat until\nconverged"]
    end
    subgraph PERP["Perplexity (key hyperparameter)"]
        PL["Low perplexity (5–15)\nFocus on very local neighbours\nFragmented clusters"]
        PH["High perplexity (30–50)\nMore global structure\nTypical default"]
    end
    subgraph LIMITS["What t-SNE CANNOT tell you"]
        N1["Cluster sizes are NOT meaningful\nArtifact of the algorithm"]
        N2["Distances BETWEEN clusters\nare NOT interpretable"]
        N3["Different runs → different layout\nalways set random_state"]
    end
    T5 --> LIMITS
    T2 --> PERP
```

t-SNE is ideal when:
- You need to visualize high-dimensional data
- Preserving local relationships matters
- You want to identify clusters visually
- Data has complex non-linear structure

```python
from sklearn.manifold import TSNE

# Basic usage
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_embedded = tsne.fit_transform(X)

# Visualize
plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=labels)
```

For the complete tutorial, see [t-SNE and UMAP Guide](tsne-umap.md).
