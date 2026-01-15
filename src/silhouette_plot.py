from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
import numpy as np

def silhouette_plot(X_scaled, labels):
    # compute silhoutte coefficient for each sample
    sample_silhouette_values = silhouette_samples(X_scaled, labels)

    fig, ax = plt.subplots(figsize=(8,6))
    y_lower = 10

    # iterate through all clusters
    n_clusters= len(np.unique(labels))
    for i in range(n_clusters):
        # Select silhouette scores for cluster i
        ith_cluster_silhouette_values = sample_silhouette_values[labels == i]
        ith_cluster_silhouette_values.sort()

        size_i = len(ith_cluster_silhouette_values)
        y_upper = y_lower + size_i

        color = plt.cm.viridis(float(i) / 2)
        ax.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            ith_cluster_silhouette_values,
            facecolor=color,
            edgecolor=color,
            alpha=0.7,
        )

        # Label the cluster on the y-axis
        ax.text(-0.05, y_lower + 0.5 * size_i, str(i))
        y_lower = y_upper + 10  # space between clusters


    avg_silhouette = silhouette_score(X_scaled, labels)
    ax.axvline(x=avg_silhouette, color="red", linestyle="--", label='Average Silhouette')

    # Plot aesthetics
    ax.set_title("Silhouette Plot of Clusters")
    ax.set_xlabel("Silhouette Coefficient Values")
    ax.set_ylabel("Cluster Label")
    ax.set_xlim([-0.1, 1])
    ax.set_yticks([])
    ax.legend()
    ax.grid(True)

    plt.show()