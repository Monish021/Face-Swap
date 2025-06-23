import numpy as np
import os
import glob
import cv2
import matplotlib.pyplot as plt

import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image
from insightface.model_zoo import get_model


app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0, det_size=(640, 640))

swapper = get_model('inswapper_128.onnx', download=False, download_zip=False)

import cv2
import matplotlib.pyplot as plt

def swap_celebrity_to_me(img1_fn, img2_fn, app, swapper, plot_before=True, plot_after=True):
    # Load the images
    prem_img = cv2.imread(img1_fn)
    my_img = cv2.imread(img2_fn)

    # Plot the original images
    if plot_before:
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))
        axs[0].imshow(prem_img[:, :, ::-1])
        axs[0].set_title("Prem")
        axs[0].axis('off')
        axs[1].imshow(my_img[:, :, ::-1])
        axs[1].set_title("You (Before Swap)")
        axs[1].axis('off')
        plt.show()

    # Get face objects
    celeb_face = app.get(prem_img)[0]
    my_face = app.get(my_img)[0]

    # Copy of your image to keep unaltered version if needed
    swapped_img = swapper.get(my_img, my_face, celeb_face, paste_back=True)

    # Plot result
    if plot_after:
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))
        axs[0].imshow(prem_img[:, :, ::-1])
        axs[0].set_title("Celebrity")
        axs[0].axis('off')
        axs[1].imshow(swapped_img[:, :, ::-1])
        axs[1].set_title("You (With Celebrity Face)")
        axs[1].axis('off')
        plt.show()

    return swapped_img

result_img = swap_celebrity_to_me("Dhiwa.jpg", "4.jpeg", app, swapper)
cv2.imwrite("my_face_with_celeb_4.jpg", result_img)
