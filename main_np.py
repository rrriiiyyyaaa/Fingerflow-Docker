import cv2
# from fingerflow.extractor import Extractor

# extractor = Extractor("./CoarseNet.h5", "./FineNet.h5", "ClassifyNet_6_classes.h5", "./CoreNet.weights")

imageName = input("Enter image name (without extension): ") + ".tif"

# image = cv2.imread(imageName)

# extracted_minutiae = extractor.extract_minutiae(image)

# minutiae = extracted_minutiae['minutiae']
import json
# store minutiae in json file
# with open(imageName + ".json", 'w') as f:
    # json.dump(minutiae.to_dict(orient='records'), f, indent=4)

# load from json file
with open(imageName + ".json", 'r') as f:
    minutiae = json.load(f)

# for index, minutia in enumerate(minutiae):
#     print("\n ==== ", index, " ==== \n", minutia)
    
#     cv2.circle(imageRGB, (int(minutia['x']), int(minutia['y'])), radius=5, color=(0, 0, 255), thickness=-1)
#     cv2.imshow('image', imageRGB)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

import numpy as np
def minutia_plot(img, mv):
    # Square parameters
    square_size = 5
    square_color = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
                    (255, 255, 0), (0, 255, 255), (255, 0, 255)]

    # Line parameters
    line_length = 10
    line_thickness = 2
    # line_color = (0, 0, 255)
    ## if the image is grayscale convert it to RGB
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    for i in mv:
        y,x,o,q,t = i.values()
        x=int(x)
        y=int(y)
        t=int(t)
        # if t>1:
            # continue
        # print(str(round(q,2)))
        # cv2.circle(img, (i.locY, i.locX), 5, (0, 0, 255), -1)
        cv2.rectangle(img, (y - square_size , x - square_size  ),
              (y + square_size, x  + square_size), square_color[t], 1)
        # display q above the rectangle
        cv2.putText(img, f"{int(q*100):2d}", (y - square_size, x - square_size - 4),
                    cv2.FONT_HERSHEY_PLAIN , 0.5, square_color[t], 1)
        line_endpoint_x = int(y + line_length * np.cos(o))
        line_endpoint_y = int(x  + line_length * np.sin(o))
        cv2.line(img, (y, x ), (line_endpoint_x, line_endpoint_y),
                 square_color[int(t)], line_thickness)
    return img

imageRGB = cv2.imread(imageName, cv2.IMREAD_COLOR)
# cv2.imshow('minutiae', minutia_plot(imageRGB, minutiae))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imwrite(imageName + "_minutiae.png", imageRGB)