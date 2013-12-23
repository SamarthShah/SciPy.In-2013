from SimpleCV import Image
img = Image('ahmedabad.jpg')

cropImg = img.crop(50, 5, 200, 200)
cropImg.show()
raw_input()

