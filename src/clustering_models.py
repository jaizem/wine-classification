from sklearn.cluster import KMeans, AgglomerativeClustering

def train_kmeans(X, n_clusters=3):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    model.fit(X)
    labels = model.predict(X)
    return model, labels

def train_agglomerative(X, n_clusters=3, linkage="ward"):
    model = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    labels = model.fit_predict(X)
    return model, labels