# Image Augmentation

<!-- MarkdownTOC -->

- Image Data Preparation
- Image Augmentation using imgaug
    - Multiple Augmentations
- Image Data Preparation
- Image Data Augmentation
- Keras Examples
- Image Data Pipeline
- References

<!-- /MarkdownTOC -->

## Image Data Preparation

When training vision models, it is common to resize images to a lower dimension ((224 x 224), (299 x 299), etc.) to allow mini-batch learning and also to keep up the compute limitations. 

We generally make use of image resizing methods like bilinear interpolation for this step and the resized images do not lose much of their perceptual character to the human eyes.

In “Learning to Resize Images for Computer Vision Tasks,” Talebi et al. show that if we try to optimize the perceptual quality of the images for the vision models rather than the human eyes, their performance can further be improved.

**For a given image resolution and a model, how to best resize the given images?**

As shown in the paper, this idea helps to consistently improve the performance of the common vision models (pre-trained on ImageNet-1k) such as DenseNet-121, ResNet-50, MobileNetV2, and EfficientNets. 

In the example, we will implement the learnable image resizing module as proposed in the paper and demonstrate that on the Cats and Dogs dataset using the DenseNet-121 architecture.


---------


## Image Augmentation using imgaug

The term image augmentation refers to twchniques used to increase the amount of data by adding slightly modified copies of existing data or creating  synthetic data from existing data.

In ML, data augmentations are used to reduce overfitting data during  training.

Image augmentation generates modified training data using existing image instances which boosts model performance, especially on small datasets and in cases of class imbalance.

In short, we make new versions of our images that are based on the originals but include intentional flaws.

Creating complex augmentation functions from scratch can be a difficult undertaking for programmers which is where the library `imgaug` can help.

Here we will create three augmentations that are commonly used in model training.

1. Brightness Augmentation

HSV (Hue, Saturation, Value) is a colour space developed by A. R. Smith in 1978 based on intuitive colour properties, often known as the Hexcone Model. This model’s colour parameters are hue (H), saturation (S), and lightness (V).

We can adjust the V value of the image:

```py
aug = iaa.imgcorruptlike.Brightness(severity=3)
fig = plt.figure(figsize=(17, 17))
for n, images in enumerate(image[0:3]):
    fig.add_subplot(2, 3, n+1)
    blur_image = aug(image=cv2.imread(images))
    plt.imshow(blur_image[:, :, ::-1])
    plt.title('Dog: {}'.format(n))
    plt.show()
```

2. Blurness Augmentation

Blurriness is obtained by calculating and analysing the Fast Fourier Transform. 

The Fourier transform identifies the frequencies present in the image. 

If there are not many high frequencies, the image will be fuzzy. 

It is up to you to define the terms ‘low’ and ‘high.’

We can apply different blur methods of the image:

```py
aug = iaa.imgcorruptlike.MotionBlur(severity=5)
fig = plt.figure(figsize=(20, 20))
for n, images in enumerate(image[0:3]):
    fig.add_subplot(2, 3, n+1)
    blur_image = aug(image=cv2.resize(cv2.imread(images), (750, 1000), interpolation = cv2.INTER_AREA))
    plt.imshow(blur_image[:, :, ::-1])
    plt.title('Dog: {}'.format(n))
    plt.show()
```

3. Gaussian Noise

Gaussian noise is a sort of noise with a Gaussian distribution such as the white noise typically observed which has a random value and is in impulses.

We can add different noise methods to the image:

```py
aug = iaa.imgcorruptlike.GaussianNoise(severity=5)
fig = plt.figure(figsize=(20, 20))
for n, images in enumerate(image[0:3]):
    fig.add_subplot(2, 3, n+1)
    blur_image = aug(image=cv2.resize(cv2.imread(images), (750, 1000), interpolation = cv2.INTER_AREA))
    plt.imshow(blur_image[:, :, ::-1])
    plt.title('Dog: {}'.format(n))
    plt.show()
```

4. Saturation Augmentation

Saturation augmentation is similar to hue augmentation in that it adjusts the image’s vibrancy. 

A grayscale image is entirely desaturated, a partially desaturated image has muted colours, and a positive saturation pushes hues closer to the primary colours.

When colors in an image differ, adjusting the saturation of an image can help the model perform better.

We can control the saturation level on the image:

```py
aug = iaa.imgcorruptlike.Saturate(severity=3)
fig = plt.figure(figsize=(20, 20))
for n, images in enumerate(image[0:3]):
    fig.add_subplot(2, 3, n+1)
    blur_image = aug(image=cv2.resize(cv2.imread(images), (750, 1000), interpolation = cv2.INTER_AREA))
    plt.imshow(blur_image[:, :, ::-1])
    plt.title('Dog: {}'.format(n))
    plt.show()
```

5. Rotation

A random rotation of the source picture clockwise or counterclockwise by a specified amount of degrees alters the item's location in the frame.

Random rotation can help you enhance your model without collecting and labelling additional data.

We can control the rotation level on the image:

```py
aug = iaa.Affine(rotate=(-45, 45))
fig = plt.figure(figsize=(20, 20))
for n, images in enumerate(image[0:3]):
    fig.add_subplot(2, 3, n+1)
    blur_image = aug(image=cv2.resize(cv2.imread(images), (750, 1000), interpolation = cv2.INTER_AREA))
    plt.imshow(blur_image[:, :, ::-1])
    plt.title('Dog: {}'.format(n))
    plt.show()
```


### Multiple Augmentations

We can perform multiple augmentations on a single batch of images. 

Here we do the following:

- We apply the Crop augmentation to crop the single image from each side anywhere between 0 to 16px which is randomly chosen.

- We apply Gaussian Noise and Motion Blur with a severity value of 5. 

```py
aug = iaa.Sequential([
    iaa.Crop(px=(0, 16)),
    iaa.imgcorruptlike.GaussianNoise(severity=5),
    iaa.imgcorruptlike.MotionBlur(severity=5)
])

fig = plt.figure(figsize=(20, 20))
for n, images in enumerate(image[0:3]):
    fig.add_subplot(2, 3, n+1)
    blur_image = aug(image=cv2.resize(cv2.imread(images), (750, 1000), interpolation = cv2.INTER_AREA))
    plt.imshow(blur_image[:, :, ::-1])
    plt.title('Dog: {}'.format(n))
    plt.show()
```


## Image Data Preparation

[How to Manually Scale Image Pixel Data for Deep Learning](https://machinelearningmastery.com/how-to-manually-scale-image-pixel-data-for-deep-learning/)

[How to Normalize, Center, and Standardize Images in Keras](https://machinelearningmastery.com/how-to-normalize-center-and-standardize-images-with-the-imagedatagenerator-in-keras/)

[How to Evaluate Pixel Scaling Methods for Image Classification](https://machinelearningmastery.com/how-to-evaluate-pixel-scaling-methods-for-image-classification/)


## Image Data Augmentation

[Image Processing and Data Augmentation Techniques for Computer Vision](https://towardsdatascience.com/image-processing-techniques-for-computer-vision-11f92f511e21)

[Data Augmentation Compilation with Python and OpenCV](https://towardsdatascience.com/data-paugmentation-compilation-with-python-and-opencv-b76b1cd500e0)


[5 Image Augmentation Techniques Using imgAug](https://betterprogramming.pub/5-common-image-augmentations-for-machine-learning-c6b5a03ebf38)

[5 Useful Image Manipulation Techniques Using Python OpenCV](https://betterprogramming.pub/5-useful-image-manipulation-techniques-using-python-opencv-505492d077ef)


[How to Configure and Use Image Data Augmentation using Keras ImageDataGenerator](https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks/)


[Introduction to Test-Time Data Augmentation](https://machinelearningmastery.com/how-to-use-test-time-augmentation-to-improve-model-performance-for-image-classification/)



## Keras Examples

[3D image classification from CT scans](https://keras.io/examples/vision/3D_image_classification/)

[Learning to Resize in Computer Vision](https://keras.io/examples/vision/learnable_resizer/)




## Image Data Pipeline

[Time to Choose TensorFlow Data over ImageDataGenerator](https://towardsdatascience.com/time-to-choose-tensorflow-data-over-imagedatagenerator-215e594f2435)

We can build better and faster image pipelines using `tf.data`. 

While training a neural network, it is quite common to use `ImageDataGenerator` class to generate batches of tensor image data with real-time data augmentation, but the `tf.data` API can be used to build a faster input data pipeline with reusable pieces.



## References

[Learning to Resize in Computer Vision](https://keras.io/examples/vision/learnable_resizer/)

[5 Image Augmentation Techniques Using imgAug](https://betterprogramming.pub/5-common-image-augmentations-for-machine-learning-c6b5a03ebf38)

[How to Load Large Datasets From Directories](https://machinelearningmastery.com/how-to-load-large-datasets-from-directories-for-deep-learning-with-keras/)

