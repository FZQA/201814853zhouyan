#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 15:00:36 2019

@author: fzqa
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.cluster import SpectralClustering
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture
from sklearn import metrics

#processing data
data=[] # all data [{}]
for line in open("Tweets.txt","r"):
    line=line[:-1]
    dict=eval(line)
    data.append(dict)
#print(data[0]['text'])
    
test_data=[] #text 
labels_true=[] #cluster
for i in data:
    test_data.append(i['text'])
    labels_true.append(i['cluster'])
#print(test_data,labels_true)
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(test_data)
#print(X)
print(max(labels_true)) #110



#Kmeans--------------------------------------------------------------------
km_cluster = KMeans(n_clusters=110, max_iter=300, n_init=40, init='k-means++',n_jobs=-1)
result = km_cluster.fit_predict(X)
print("Kmeans Predicting result: ", result)
NMI_kmeans=metrics.adjusted_mutual_info_score(labels_true, result) 
print("NMI_kmeans=",NMI_kmeans) 

#Affinity propagation-------------------------------------------------------
labels = AffinityPropagation().fit_predict(X)
print(labels)
NMI_Aff=metrics.adjusted_mutual_info_score(labels_true, labels) 
print("NMI_Affinitypropagation=",NMI_Aff) 

#Mean-shift----------------------------------------------------------------
labels = MeanShift(bandwidth=0.9, bin_seeding=True).fit_predict(X.toarray())
print(labels)
NMI_Mean_shift=metrics.adjusted_mutual_info_score(labels_true, labels) 
print("NMI_Mean_shift=",NMI_Mean_shift) 

#Spectral clustering--------------------------------------------------------
sc = SpectralClustering( n_clusters=110)
labels=sc.fit_predict(X)
print(labels)
NMI_Spectral_clustering=metrics.adjusted_mutual_info_score(labels_true, labels) 
print("NMI_Spectral_clustering=",NMI_Spectral_clustering) 


#Ward hierarchical clustering-----------------------------------------------
labels = AgglomerativeClustering(n_clusters=110, linkage='ward').fit_predict( X.toarray())
print(labels)
NMI_Ward_hierarchical=metrics.adjusted_mutual_info_score(labels_true, labels) 
print("NMI_Ward_hierarchical=",NMI_Ward_hierarchical) 


#Agglomerative clustering---------------------------------------------------
labels = AgglomerativeClustering(n_clusters=110).fit_predict( X.toarray())
print(labels)
NMI_Agglomerative=metrics.adjusted_mutual_info_score(labels_true, labels) 
print("NMI_Agglomerative=",NMI_Agglomerative) 


#DBSCAN--------------------------------------------------------------------
labels = DBSCAN(eps=1.13).fit_predict(X)
print(labels)
NMI_DBSCAN=metrics.adjusted_mutual_info_score(labels_true, labels) 
print("NMI_DBSCAN=",NMI_DBSCAN) 

#Gaussian mixtures---------------------------------------------------------000000000000
gssm = GaussianMixture(n_components=110,  covariance_type='tied',random_state=0, max_iter=100).fit(X.toarray())
print(gssm.labels_)
NMI_GaussianMixture=metrics.adjusted_mutual_info_score(labels_true, gssm.labels_) 
print("NMI_GaussianMixture=",NMI_GaussianMixture) 


