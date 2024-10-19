
# Neural Style Transfer with PyTorch



## Overview
Neural Style Transfer is a technique used to manipulate and transform images by applying the style of one image to the content of another. This project uses a pre-trained VGG19 model to extract both style and content features from images, using them to iteratively update the input image to blend the content and style.



This project involves a dataset of reptiles and amphibians and uses a pretrained model for classification. The results are showcased through a web application built with Flask.

## Installation

### Prerequisites

Python 3.7 or higher
PyTorch
PIL (Pillow)
Matplotlib


## Cloning the repository


## Usage

### Prepare Content and Style Images

Place your content and style images in a folder or use publicly available datasets (e.g., Kaggle).

### Run the Neural Style Transfer Script

Modify the file paths for your content and style images in the script as necessary. For example:

### python

```style_img = image_loader("path_to_your_style_image.jpg")```
```content_img = image_loader("path_to_your_content_image.jpg")```


### Run the script:



python neural_style_transfer.py

The script will perform 300 iterations by default, but you can modify this in the num_steps variable.

###  View the Output

After the script runs, the output image will be displayed using matplotlib. You can save it manually from the displayed image.

## Methodology
1. Loading Images: Images are loaded and preprocessed using PyTorch’s torchvision.transforms
2. Model: A pre-trained VGG19 network is used to extract content and style features. Only specific layers of the network are used:
Content is derived from deeper layers (conv_4).
Style is derived from multiple layers (conv_1, conv_2, conv_3, etc.).
3. Loss Functions:
  *  Content Loss: Mean Squared Error (MSE) between the content image and the input image's content.
  *  Style Loss: MSE between the Gram matrix of the style features of the style image and the input image.
4. Optimization: The input image is iteratively updated using the LBFGS optimizer to minimize the combined loss function.
5. Output: After optimization, the image is saved or displayed using matplotlib.


