from SimpleCV import Camera, Display, Image
cam = Camera()
display = Display()
img = cam.getImage()
img.save(display)
img.save('/home/samarth/Desktop/SciPy.In 2013/SciPy.jpg')
raw_input()


