from preprocess import hashes, labels
from sklearn.cluster import KMeans
import pickle


# train test split
X_train, X_test, y_train, y_test = train_test_split(hashes, labels, test_size=0.25)

# k means model
model = KMeans(n_clusters=2)

# raw data transformed to k means cluster model space
hashes_transformed = model.transform(hashes)
labels_transformed = model.transform(labels)

# train on data
model.fit(X_train)

# save the model so we don't have to retrain every FUCKING time
with open("kmeans_model.obj","wb") as filehandler
	pickle.dump(model, filehandler)
