from preprocess import X
from sklearn.cluster import KMeans


# k means model
model = KMeans(n_clusters=2)

# raw data transformed to k means cluster model space
X_transformed = model.transform(X)

# train on data
model.fit(X)
