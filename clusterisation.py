from matplotlib import markers
import numpy as np
from sklearn.cluster import AffinityPropagation, KMeans, MeanShift, estimate_bandwidth, AgglomerativeClustering, DBSCAN
from sklearn.datasets import make_blobs
from itertools import cycle
import matplotlib.colors as colors_
from random import randint


class Clusterisation:
    def __init__(self, matrix, n_clusters ):
        self.X = matrix
        self.num_of_clusters = n_clusters

    def kmeans(self, plt):
        plt.subplot(231)
        kmeans = KMeans(n_clusters=self.num_of_clusters).fit(self.X)
        centers = kmeans.cluster_centers_
        y_pred = kmeans.fit_predict(self.X)
        plt.scatter(self.X[:, 0], self.X[:, 1], marker='.', c=y_pred, cmap='rainbow')
        plt.scatter(centers[:, 0], centers[:, 1], c="b", s=50)
        plt.title("K-Means")


    def afprop(self, plt):
        plt.subplot(232)
        ap = AffinityPropagation(damping=0.95, random_state=0).fit(self.X)
        centers = ap.cluster_centers_
        cluster_centers_indices = ap.cluster_centers_indices_
        labels = ap.labels_
        n_clusters_ = len(cluster_centers_indices)
        ##y_pred = ap.fit_predict(self.X)
       
        ##lines
        for i in range(n_clusters_):
            class_members = labels == i
            col_ = '#%06X' % randint(0, 0xFFFFFF)
            cluster_center = self.X[cluster_centers_indices[i]]
            plt.scatter(self.X[class_members, 0], self.X[class_members, 1], c = col_, marker='.')
            
            for x in self.X[class_members]:
                plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], c = col_)
            plt.plot(
                cluster_center[0],
                cluster_center[1],
                "o",
                markerfacecolor=col_,
                markeredgecolor="k",
                markersize=12,
                )
        
        plt.title("AffinityPropagation")


    def mean_shift(self, plt):
        plt.subplot(233)
        bandwidth = estimate_bandwidth(self.X, quantile=0.06)
        print(bandwidth)
        ms = MeanShift(bandwidth=bandwidth, max_iter=600, bin_seeding=True).fit(self.X)
        labels = ms.labels_
        cluster_centers = ms.cluster_centers_
        labels_unique = np.unique(labels)
        n_clusters_ = len(labels_unique)
        print(n_clusters_)       

        for k in range(n_clusters_):
            my_members = labels == k
            col = '#%06X' % randint(0, 0xFFFFFF)
            cluster_center = cluster_centers[k]
      
            plt.plot(self.X[my_members, 0], self.X[my_members, 1], ".", c = col)
            plt.plot(
                cluster_center[0],
                cluster_center[1],
                "o",
                markerfacecolor=col,
                markeredgecolor="k",
                markersize=12,
            )
        plt.title("Means shift")

    def agglomerative_clustering(self, plt):
        plt.subplot(234)
        ac = AgglomerativeClustering(n_clusters=self.num_of_clusters).fit(self.X)
        y_pred = ac.fit_predict(self.X)      
        plt.scatter(self.X[:, 0], self.X[:, 1], marker='.', c=y_pred, cmap='rainbow' )
        plt.title("Agglomerative clustering")
        
    
    def dbscan(self, plt):
        plt.subplot(235)
        db = DBSCAN(eps=20000, min_samples=5).fit(self.X)
        labels = db.labels_
        print(self.X)
        plt.scatter(self.X[:, 0], self.X[:, 1], marker='.', c=labels, cmap='rainbow')
        plt.title('DBSCAN')
