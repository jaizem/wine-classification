from sklearn.metrics import silhouette_score, davies_bouldin_score
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering

def silhouette_score_eval(X, labels):
    return silhouette_score(X, labels)

def davies_bouldin_eval(X, labels):
    return davies_bouldin_score(X, labels)



def silhouette_vs_k(X, k_range=range(2, 11), plot=True):
    """
    Calculate silhouette scores for KMeans and Agglomerative clustering 
    over a range of cluster counts.
    
    Returns:
        dict with keys 'kmeans' and 'agg' containing lists of scores.
    """
    silhouette_scores = {"kmeans": [], "agg": []}
    
    for k in k_range:
        # KMeans
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        k_labels = kmeans.predict(X)
        silhouette_scores["kmeans"].append(silhouette_score(X, k_labels))
        
        # Agglomerative
        agg = AgglomerativeClustering(n_clusters=k, linkage="ward")
        agg_labels = agg.fit_predict(X)
        silhouette_scores["agg"].append(silhouette_score(X, agg_labels))
    
    if plot:
        plt.figure()
        plt.plot(k_range, silhouette_scores["kmeans"], label="KMeans", color="blue")
        plt.plot(k_range, silhouette_scores["agg"], label="Agglomerative", color="red")
        plt.xlabel("Number of clusters (k)")
        plt.ylabel("Silhouette Score")
        plt.title("Silhouette Score vs. Number of Clusters")
        plt.legend()
        plt.grid(True)
        plt.show()
    
    return silhouette_scores