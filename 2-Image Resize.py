from SimpleCV import Image
img = Image('ahmedabad.jpg')
bigImg = img.resize(img.width * 2, img.height)
bigImg.show()
raw_input()
