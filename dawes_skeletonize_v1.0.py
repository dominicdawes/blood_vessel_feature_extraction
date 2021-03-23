import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.filters import threshold_otsu
from skimage.morphology import medial_axis, skeletonize

# IMAGE PATH
path = 'bw_dataset\\test_05.jpg'


# function definition
def neighbours(x, y, image):
    "Return 8-neighbours of image point P1(x,y), in a clockwise order"
    img = image
    x_1, y_1, x1, y1 = x - 1, y - 1, x + 1, y + 1
    return [img[x_1][y], img[x_1][y1], img[x][y1], img[x1][y1],  # P2,P3,P4,P5
            img[x1][y], img[x1][y_1], img[x][y_1], img[x_1][y_1]]  # P6,P7,P8,P9


def skel_to_branchpoints(in_skel):
    """
    returns boolean np array of bifurcations/intersections x,y coordinates
    when given a skeletonized input
    depends on "from skan import skeleton_to_csgraph"
    Args:
        in_skel: np array; binary skeleton

    Returns:
        intersection_matrix: np array; boolean values where True = bifurcations/intersections
    """
    from skan import skeleton_to_csgraph
    _, _, degrees = skeleton_to_csgraph(in_skel)

    # consider all values larger than two connections as intersections
    intersection_matrix = degrees > 2

    # create a dict representing the number of connections vs non-connections
    unique, counts = np.unique(intersection_matrix, return_counts=True)
    intersect_dict = dict(zip(unique, counts))

    # returns the number of bifurcations/intersections as a dictionary
    print(f'intersection_matrix count: {intersect_dict}')

    # return boolean np array of bifurcations/intersections x,y coordinates
    return intersection_matrix


# read in file and show (rgb image)
img_original = cv2.imread(path)

# image must converted to grayscale
img_grayscale = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

# Convert gray images to binary images using Otsu's method
otsu_threshold = threshold_otsu(img_grayscale)
bw_original = img_grayscale > otsu_threshold

# skimage package method skeletonize
skel = skeletonize(bw_original)  # needs binary image

# bifurcation locations from 2D skeleton
intersections = skel_to_branchpoints(skel)

# Display the results
fig, ax = plt.subplots(2, 2)

# original
ax[0, 0].imshow(img_grayscale, cmap=plt.cm.gray)
ax[0, 0].set_title('Original grayscale image')
ax[0, 0].axis('off')

# skeleton
ax[0, 1].imshow(skel, cmap=plt.cm.gray)
ax[0, 1].set_title('skeletonize')
ax[0, 1].axis('off')

# bifurcations
ax[1, 0].imshow(intersections)
ax[1, 0].set_title('intersections')
ax[1, 0].axis('off')
-0
plt.show()
