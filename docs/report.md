# Wine Varietal Classification Using Clustering

## Cluster Segmentation
The cluster assignments from KMeans and agglomerative clustering show low agreement. KMeans produced distinct, well-separated clusters with hard boundaries. Only Cluster 0 showed notable overlap between the two methods, with 45 samples assigned identically. Using 'ward' linkage was the best result across all four agglomerative linkage strategies tested, with 'single' linkage as a close second—again showing similar labeling for Cluster 0. In contrast, only 2 samples were jointly labeled as Cluster 1, and none for Cluster 2.

Analyzing the scatter plot for agglomerative clustering, the clusters are extremely elongated and show extensive overlap. The clusters are highly inaccurate with this method. This suggests that agglomerative clustering is not well suited for this dataset in comparison to KMeans.

## Silhouette Scores
The silhouette plot groups silhouette scores by cluster, showing the distribution and density of scores within each one. A red dashed line indicates the average silhouette score across all samples. Each data point has a silhouette coefficient ranging from -1 to 1, where negative values suggest incorrect cluster assignment, values near 0 indicate samples on a decision boundary, and values close to 1 represent well-clustered samples.

For the wine dataset, KMeans clustering achieved an average silhouette score of 0.30, suggesting generally correct label assignments. Only one sample had a negative silhouette score, and only marginally so, at -0.01. In contrast, agglomerative clustering performed worse, with an average silhouette score of 0.25. Numerous samples had negative silhouette values, reflecting a higher rate of misclassified points. This aligns with the cross-tabulation results and further indicates that agglomerative clustering is less accurate for this dataset.

## Davies-Bouldin Scores: 
This metric measures the similarity between clusters, based on the ratio of intra-cluster distance to inter-cluster distance. Lower scores indicate better-defined, well-separated clusters.

For the wine dataset, the Davies-Bouldin score for KMeans clustering is 1.30, suggesting the clusters are slightly elongated and may have boundaries that come close to overlapping. This is consistent with the KMeans clustering scatter plot. Agglomerative clustering produced an even higher DB score of 1.51, indicating greater cluster overlap and poorly defined cluster shapes. Again, this is reflected in the corresponding agglomerative clustering scatter plot.

## PCA Analysis
Given that the dataset is composed of 3 varietals of wine, setting n_clusters=3 yields an optimal clustering outcome. PCA applied to the clustered data highlights the most influential features for distinguishing each class.

Class 3 shows high values for ash (both in ppm and alkalinity) and a negative weight for color intensity (-0.24). This indicates a mineral-rich, visually lighter wine—likely Grignolino, known for its higher ash content and pale appearance.

Class 2 is characterized by high alcohol content and strong color intensity, with negative weights on hue (-0.27) and OD280/OD315 (-0.20). These traits align with Barbera, a varietal known for deep color, higher alcohol, and lower tannin-related optical density.

Class 1 emphasizes total phenols (0.39) and flavonoids (0.42), while down-weighting nonflavonoid phenols (-0.29) and ash alkalinity (-0.28). This profile corresponds to Barolo, notable for its bold tannic structure and high phenolic content.

Overall, PCA-supported clustering not only validates the choice of n_clusters=3 but also captures the chemical signatures that differentiate the three varietals.