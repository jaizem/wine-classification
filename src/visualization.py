import matplotlib.pyplot as plt
import seaborn as sbn
from sklearn.decomposition import PCA
import pandas as pd

def plot_elbow(K, inertia):
    plt.plot(K, inertia)
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Inertia")
    plt.grid(True)
    plt.show()

def plot_pca_clusters(X_scaled, labels, title="Cluster Visualization PCA"):
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    plt.figure()
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels)
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_heatmap(loadings, columns):
    sbn.heatmap(loadings, annot=True, cmap="coolwarm", xticklabels=columns,
                yticklabels=[f"PC{i+1}" for i in range(loadings.shape[0])])
    
def silhouette_plot(X_scaled, labels):
    """Plot silhouette scores for each sample."""
    from sklearn.metrics import silhouette_samples
    import numpy as np

    sil_vals = silhouette_samples(X_scaled, labels)
    y_lower = 10
    plt.figure(figsize=(8, 5))

    for i in range(len(set(labels))):
        ith_silhouette_vals = sil_vals[labels == i]
        ith_silhouette_vals.sort()
        size_cluster_i = ith_silhouette_vals.shape[0]
        y_upper = y_lower + size_cluster_i

        plt.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            ith_silhouette_vals,
            alpha=0.7
        )
        plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10

    plt.xlabel("Silhouette coefficient values")
    plt.ylabel("Cluster label")
    plt.title("Silhouette Plot")
    plt.axvline(np.mean(sil_vals), color="red", linestyle="--")
    plt.show()

def pca_transform_and_plot(X_scaled, n_components=3, plot=True):
    """
    Perform PCA on scaled data and optionally plot heatmap of feature importance.
    
    Args:
        X_scaled: numpy array or DataFrame of scaled features
        n_components: number of PCA components
        plot: whether to plot the heatmap of loadings
        
    Returns:
        X_pca: numpy array of PCA-transformed data
        loadings: DataFrame of component loadings
    """
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    
    # Turn into DataFrame for easier plotting
    if hasattr(X_scaled, "columns"):  # if input is DataFrame
        columns = X_scaled.columns
    else:
        columns = [f"feature_{i}" for i in range(X_scaled.shape[1])]
    loadings = pd.DataFrame(pca.components_, columns=columns)
    
    if plot:
        plt.figure(figsize=(8, 4))
        sbn.heatmap(
            loadings,
            annot=True,
            cmap="coolwarm",
            xticklabels=columns,
            yticklabels=[f"PC{i+1}" for i in range(loadings.shape[0])],
        )
        plt.title("PCA Component Loadings")
        plt.show()
    
    return X_pca, loadings