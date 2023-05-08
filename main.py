import cv2
from fingerflow.extractor import Extractor

extractor = Extractor("./CoarseNet.h5", "./FineNet.h5", "ClassifyNet_6_classes.h5", "./CoreNet.weights")

imageName = input("Enter image name (without extension): ") + ".tif"

image = cv2.imread(imageName)

extracted_minutiae = extractor.extract_minutiae(image)

minutiae = extracted_minutiae['minutiae']

for index, minutia in minutiae.iterrows():
    print("\n ==== ", index, " ==== \n", minutia)
    imageRGB = cv2.imread(imageName, cv2.IMREAD_COLOR)
    cv2.circle(imageRGB, (int(minutia['x']), int(minutia['y'])), radius=5, color=(0, 0, 255), thickness=-1)
    cv2.imshow('image', imageRGB)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
