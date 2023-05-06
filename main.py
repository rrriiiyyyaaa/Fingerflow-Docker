import cv2
import numpy as np
from fingerflow.extractor import Extractor

extractor = Extractor("CoarseNet.h5", "FineNet.h5", "ClassifyNet_6_classes.h5", "CoreNet.weights")

image = cv2.imread(input("Enter filename"))

extracted_minutiae = extractor.extract_minutiae(image)