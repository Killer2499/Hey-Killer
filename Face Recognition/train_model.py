from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import argparse
import pickle

ap=argparse.ArgumentParser()
ap.add_argument("-e","--embeddings",required=True,
	help="Path to the serialized db of facial embeddings")
ap.add_argument("-r","--recognizer",required=True,
	help="Path to output model trained to recognize faces")
ap.add_argument("-l","--le",required=True,
	help="Path to output Label Encoder")
args=vars(ap.parse_args())

#Loading face embeddings
print("[INFO] Loading Face Embeddings...")
data=pickle.loads(open(args['embeddings'],'rb').read())

#Encode the labels
print("[INFO] Encoding Labels...")
le=LabelEncoder()
labels=le.fit_transform(data['names'])

#Train the model to accept embeddings and produce actual face recognition
print("[INFO] Training Model...")
recognizer=SVC(C=1.0,kernel="linear",probability=True)
recognizer.fit(data['embeddings'],labels)

#Writing the actual face recogition model to disk
f=open(args['recognizer'],'wb')
f.write(pickle.dumps(recognizer))
f.close()

#writing label encoder to disk
f=open(args['le'],'wb')
f.write(pickle.dumps(le))
f.close()