from SimpleCV import *
cam = Camera()
disp = Display(cam.getImage().size())
while disp.isNotDone():
	img = cam.getImage()
	# Look for a face
	faces = img.findHaarFeatures('/home/samarth/Desktop/SciPy.In 2013/face.xml')
	if faces is not None:
		# Get the largest face
		faces = faces.sortArea()
		bigFace = faces[-1]
	# Draw a green box around the face
		bigFace.draw()
		img.save(disp)
