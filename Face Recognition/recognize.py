import numpy as np 
import argparse
import imutils
import pickle
import cv2
import os

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,
	help="Path to Image File")
ap.add_argument("-d","--detector",required=True,
	help="Path to Open CV's deep learning face detector")
ap.add_argument("-m","--encoding_model",required=True,
	help="path to Open CV's deep learning face encoding model")
ap.add_argument("-r","--recognizer",required=True,
	help="path to model trained to recognize Faces")
ap.add_argument("-l","--le",required=True,
	help="path to label encoder")
ap.add_argument("-c","--confidence",type=float,default=0.5,
	help="minimum probability to filter weak detections")
args=vars(ap.parse_args())

#Load our serialized face detector from disk
print("[INFO] Loading Face Detector")
protoPath = os.path.sep.join([args["detector"],'deploy.prototxt'])
modelPath = os.path.sep.join([args["detector"],'res10_300x300_ssd_iter_140000.caffemodel'])
detector=cv2.dnn.readNetFromCaffe(protoPath,modelPath)

#Load our serialized face embedder from disk
print("[INFO] Loading Face Embedder")
embedder=cv2.dnn.readNetFromTorch(args["encoding_model"])

#Load face recognition model along with the label encoder
recognizer=pickle.loads(open(args['recognizer'],'rb').read())
le=pickle.loads(open(args['le'],'rb').read())

#Load the image,resize to width =600px and grab dimensions
image=cv2.imread(args['image'])
image=imutils.resize(image,width=600)
(h,w)=image.shape[:2]

#Construct a blob from Image
imageBlob = cv2.dnn.blobFromImage(cv2.resize(image,(300,300)),1.0,(300,300),(104.0,177.0,123.0),swapRB=False,crop=False)

#Applying opencv's dl model to detect face

detector.setInput(imageBlob)
detections=detector.forward()

#Loop over detections
for i in range(0,detections.shape[2]):

	confidence=detections[0,0,i,2]

	if confidence>args['confidence']:

		box=detections[0,0,i,3:7]*np.array([w,h,w,h])
		(startX,startY,endX,endY)=box.astype('int')

		face=image[startY:endY,startX:endX]
		(fH,fW)=face.shape[:2]

		if fW<20 and fH<20:
			continue

		faceBlob=cv2.dnn.blobFromImage(face,1.0/255,(96,96),(0,0,0),swapRB=True,crop=False)
		embedder.setInput(faceBlob)
		vec=embedder.forward()

		#Predicting to recognize
		preds=recognizer.predict_proba(vec)[0]
		j=np.argmax(preds)
		proba=preds[j]
		name=le.classes_[j]

		#Drawing bounding box
		text="{}".format(name)
		y=startY-10 if startY-10>10 else startY+10
		cv2.rectangle(image,(startX,startY),(endX,endY),(0,0,255),3)
		cv2.putText(image,text,(startX,y),cv2.FONT_HERSHEY_SIMPLEX,0.45,(0,0,255),2)
#Output
cv2.imshow("Image",image)
cv2.waitKey(0)
