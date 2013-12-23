from SimpleCV import Image
img = Image('ahmedabad.jpg')
imgBin = img.binarize()

imgBin.erode().show()
raw_input()
