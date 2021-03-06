from sklearn.cluster import KMeans
import pandas as pd
import pickle

filehandler = open("normal_hashes.obj",'rb')
normal_hashes_df = pickle.load(filehandler)
filehandler.close()

filehandler = open("malware_hashes.obj",'rb')
malware_hashes_df = pickle.load(filehandler)
filehandler.close()

# concatenate
hashes = pd.concat(normal_hashes_df, malware_hashes_df)

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
