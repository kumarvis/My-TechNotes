# Deep Computer Vision Using Convolutional Neural Networks

**CNN Layers**
----------

Figure below shows CNN on RGB(3 channel) image.
![img_cnn_image](../images/ch14_cnn_filters.png)

In TensorFlow, each input image is typically represented as a 3D tensor of shape [height, width, channels]. A 
mini-batch is represented as a 4D tensor of shape \[mini-batch size, height, width, channels](NHWC).

### Pooling Layers
--------------

`global average pooling layer`, it works very differently: all it does is compute the mean of each entire feature map 
(it’s like an average pooling layer using a pooling kernel with the same spatial dimensions as the inputs). This means 
that it just outputs a single number per feature map and per instance. Although this is of course extremely destructive
(most of the information in the feature map is lost), it can be useful as the output layer, as we will see later in 
this chapter. To create such a layer, simply use the keras.layers.GlobalAvgPool2D class:
`global_avg_pool=keras.layers.GlobalAvgPool2D()`

Figure below is an example of **GlobalAvgPool2D** pooling layer output is the average of each layer.

![img_cnn_global_avg_2d](../images/ch14_global_average_pooling.png)

**CNN Architectures**
-----------------
#### <ins> GoogLeNet </ins>
![img_cnn_googlenet](../images/ch14_inception01.jpeg)

![img_cnn_googlenet](../images/ch14_inception01-1.jpeg)

![img_cnn_googlenet](../images/ch14_inception02.jpeg)

![img_cnn_googlenet](../images/ch14_inception03.jpeg)

![img_cnn_googlenet](../images/ch14_inception04.jpeg)

### <ins> ResNet: </ins>
![img_cnn_resnet](../images/ch14_resnet01.jpeg)

![img_cnn_resnet](../images/ch14_resnet02.jpeg)

1. *H(x) = F(x) + x* so even worst case if you don't learn anything i.e F(x) -> 0. There will be identiy function *x*.

2. The delta for the learning of residual part *F(x)* is not very high from one layer to other layer hence it is easy to learn the residual as compare to *H(x)*. `Reference:` [NPTEL CNN Architecture Part 4 (ResNet)](https://youtu.be/iBepeakXC08?t=340)

### <ins> Xception: </ins>

Another variant of the GoogLeNet architecture is worth noting: Xception 19 (which stands for Extreme Inception) was
proposed in 2016 by François Chollet (the author of Keras), and it significantly outperformed Inception-v3 on a huge
vision task (350 million images and 17,000 classes). Just like Inception-v4, it merges the ideas of GoogLeNet and 
ResNet, but it replaces the inception modules with a special type of layer called a depthwise separable convolution 
layer (or separable convolution layer for short 20 ).

Thus, it is composed of two parts: the first part applies a single spatial filter for each input feature map, 
then the second part looks exclusively for cross-channel patterns—it is just a regular convolutional layer with 1 ×
1 filters. Refer image below:

![img_cnn_xception_net](../images/ch14_xception_net.png)

***Since separable convolutional layers only have one spatial filter per input channel, you should avoid using them*** 
***after layers that have too few channels, such as the input layer (granted, that’s what Figure above represents,*** 
***but it is just for illustration purposes)****. For this reason, the Xception architecture starts with 2 regular convolutional
layers, but then the rest of the architecture uses only separable convolutions (34 in
all), plus a few max pooling layers and the usual final layers (a global average pooling
layer and a dense output layer).


### <ins> SENet: </ins>

The winning architecture in the ILSVRC 2017 challenge was the Squeeze-and-
Excitation Network (SENet). 22 This architecture extends existing architectures such as inception networks and ResNets, and boosts their performance. This allowed SENet
to win the competition with an astonishing 2.25% top-five error rate! The extended
versions of inception networks and ResNets are called SE-Inception and SE-ResNet,
respectively. The boost comes from the fact that a SENet adds a small neural network,
called an SE block, to every unit in the original architecture (i.e., every inception
module or every residual unit), as shown in Figure below:

![img_cnn_se_net](../images/ch14_se_net01.png)

 CNN network weights each of its channels equally when creating the output feature maps. SENets are all about changing this by adding a content aware mechanism to weight each channel adaptively. 

 #### HOW:

```python
def se_block(in_block, ch, ratio=16):
    x = GlobalAveragePooling2D()(in_block)
    x = Dense(ch//ratio, activation='relu')(x)
    x = Dense(ch, activation='sigmoid')(x)
    return multiply()([in_block, x])

```

1. The function is given an input convolutional block and the current number of channels it has.

2. We squeeze each channel to a single numeric value using 2D average pooling.

3. A dense layer followed by a ReLU function adds the necessary nonlinearity. It’s output channel complexity is also reduced by a certain ratio.

4. A dense layer followed by a Sigmoid activation gives each channel a smooth gating function.

5. At last, we weight each feature map of the convolutional block based on the result of our side network.(multiply step)

Refer below image for illustrative details:

![img_cnn_se_net](../images/ch14_se_net02.png)

![img_cnn_se_net](../images/ch14_se_net03.png)

For example, an SE block may learn that
mouths, noses, and eyes usually appear together in pictures: if you see a mouth and a
nose, you should expect to see eyes as well. So if the block sees a strong activation in the mouth and nose feature maps, but only mild activation in the eye feature map, it will boost the eye feature map **(more accurately, it will reduce irrelevant feature maps because no multiply scale factor can be more than 1.0 hence reduce the irrelevant fatures by multiplying a small scale factor)**. If the eyes were somewhat confused with something else, this feature map recalibration will help resolve the ambiguity.

### <ins> MobileNet V1: </ins>

MobileNetV1 from Google is reviewed. Depthwise Separable Convolution is used to reduce the model size and complexity. It is particularly useful for mobile and embedded vision applications. Image below illustrate concept of MobileNet architecture. 

![img_cnn_mobilenet](../images/ch14_mbilenetv101.png)

8 to 9 times less computation can be achieved, but with only small reduction in accuracy. **Below is the MobileNet Complete Architecture** Batch Normalization (BN) and ReLU are applied after each convolution.

![img_cnn_mobilenet](../images/ch14_mbilenetv102.png)

| ![img_cnn_mobilenet](../images/ch14_mbilenetv103.png) | 
|:--:| 
| **Standard Convolution (Left), Depthwise separable convolution (Right) With BN and ReLU** |

As is common in modern architectures, the convolution layers are followed by batch normalization. **The activation function used by MobileNet is ReLU6**. This is like the well-known ReLU but it prevents activations from becoming too big refer the equation below:

```python
y = min(max(0, x), 6)
```

| ![img_cnn_mobilenet](../images/ch14_mbilenetv104.png) | 
|:--:| 
| **Relu6: Max activation value than can be achieve is 6** |

### <ins> MobileNet V2: </ins>

MobileNetV2 builds upon the ideas from MobileNetV1, using depthwise separable convolution as efficient building blocks. However, V2 introduces two new features to the architecture: 1) Linear bottlenecks between the layers, and 2) Shortcut connections between the bottlenecks1. The basic structure is shown below.

![img_cnn_mobilenet](../images/ch14_mbilenetv105.png)

This time there are three convolutional layers in the block. The last two are the ones we already know: a depthwise convolution that filters the inputs, followed by a 1×1 pointwise convolution layer. However, this 1×1 layer now has a different job.
The projection layer — it projects data with a high number of dimensions (channels) into a tensor with a much lower number of dimensions. 

For example, if there is a tensor with 24 channels going into a block, the expansion layer first converts this into a new tensor with 24 * 6 = 144 channels. Next, the depthwise convolution applies its filters to that 144-channel tensor. And finally, the projection layer projects the 144 filtered channels back to a smaller number, say 24 again. Refer figure below.

![img_cnn_mobilenet](../images/ch14_mbilenetv106.png)

<ins>Motivation for these changes:</ins> Think of the low-dimensional data that flows between the blocks as being a compressed version of the real data. In order to run filters over this data, we need to uncompress it first. That’s what happens inside each block:

![img_cnn_mobilenet](../images/ch14_mbilenetv107.png)

The expansion layer acts as an decompressor (like unzip) that first restores the data to its full form, then the depthwise layer performs whatever filtering is important at this stage of the network, and finally the projection layer compresses the data to make it small again.

The trick that makes this all work, of course, is that the expansions and projections are done using convolutional layers with learnable parameters, and so the model is able to learn how to best (de)compress the data at each stage in the network.

<ins>Comparison of the Versions:</ins> Let’s compare MobileNet V1 to V2, starting with the sizes of the models in terms of learned parameters and required amount of computation:

Version | MAC(millions) | Parameters(millions)
------------ | ------------- | ---------------
MobileNet V1 | 569 | 4.24  
MobileNet V2 | 300 | 3.47  

“MACs” are multiply-accumulate operations. This measures how many calculations are needed to perform inference on a single 224×224 RGB image. (The larger the image, the more MACs are needed.)

#### <ins>References:</ins>

1. [MobileNet version 2](https://machinethink.net/blog/mobilenet-v2/)
2. [MobileNet: Paper Review and Model Architecture](https://medium.com/@rockyxu399/mobilenet-paper-review-and-model-architecture-7963c22ea528)

**Object Detection and Segmentation**
---------------------------------

### 1. <mark> Fast and Faster R-CNN </mark>

![img_cnn_frcnn_net](../images/ch14_frcnn01.jpeg)

![img_cnn_frcnn_net](../images/ch14_frcnn02.jpeg)

![img_cnn_frcnn_net](../images/ch14_frcnn03.jpeg)

![img_cnn_frcnn_net](../images/ch14_frcnn04.jpeg)

![img_cnn_frcnn_net](../images/ch14_frcnn05.jpeg)

![img_cnn_frcnn_net](../images/ch14_frcnn06.jpeg)

#### <ins>References:</ins>

1. [Deep learning for all at Manas lab IIT Mandi](https://youtu.be/CKVuTe4nHgI?list=PLKvX2d3IUq58z6Ogtqm_Ni3TNdL3w2r5P)

2. [Understanding Region of Interest — (RoI Pooling)](https://towardsdatascience.com/understanding-region-of-interest-part-1-roi-pooling-e4f5dd65bb44)

3. [Understanding Region of Interest — (RoI Align and RoI Warp)](https://towardsdatascience.com/understanding-region-of-interest-part-2-roi-align-and-roi-warp-f795196fc193)

4. [Faster R-CNN (object detection) implemented by Keras](https://towardsdatascience.com/faster-r-cnn-object-detection-implemented-by-keras-for-custom-data-from-googles-open-images-125f62b9141a)

5. [Faster R-CNN (object detection) implemented by Keras Git Link](https://github.com/RockyXu66/Faster_RCNN_for_Open_Images_Dataset_Keras)

### 2. <mark> Mask R-CNN </mark>

Mask R-CNN is a state-of-the-art model for instance segmentation. It extends Faster R-CNN, the model used for object detection, by adding a parallel branch for predicting segmentation masks.

![img_cnn_mask-rcnn_net](../images/ch14_mas-rcnn01.png)

![img_cnn_mask-rcnn_net](../images/ch14_mas-rcnn02.png)

![img_cnn_mask-rcnn_net](../images/ch14_mas-rcnn03.png)

![img_cnn_mask-rcnn_net](../images/ch14_mas-rcnn04.png)

#### <ins>References:</ins>

1. [Mask R-CNN](https://cseweb.ucsd.edu/classes/sp18/cse252C-a/CSE252C_20180509.pdf)

2. [Quick intro to Instance segmentation: Mask R-CNN](https://kharshit.github.io/blog/2019/08/23/quick-intro-to-instance-segmentation)

### 3. <mark> YOLO V1, V2 and V3 </mark>

![img_yolo](../images/ch14_yolo01.jpeg)

![img_yolo](../images/ch14_yolo02.jpeg)

![img_yolo](../images/ch14_yolo03.jpeg)

![img_yolo](../images/ch14_yolo04.jpeg)

![img_yolo](../images/ch14_yolo05.jpeg)

![img_yolo](../images/ch14_yolo06.jpeg)

![img_yolo](../images/ch14_yolo07.jpeg)

![img_yolo](../images/ch14_yolo08.jpeg)

![img_yolo](../images/ch14_yolo09.jpeg)

![img_yolo](../images/ch14_yolo10.jpeg)

![img_yolo](../images/ch14_yolo11.jpeg)

![img_yolo](../images/ch14_yolo12.jpeg)

#### <ins> Benchmarking </ins>

Netwrok architecture of Darknet-53 is better than ResNet-101 but 1.5 times faster and is as accurate as ResNet-152 but 2x times faster refer figure below.

![img_yolo](../images/ch14_yolov3_benchmark.jpeg)

<ins>Detector</ins> comparison: YOLO v3 performs at par with other state of art detectors like RetinaNet, while being considerably faster, at COCO mAP 50 benchmark. It is also better than SSD and it’s variants. Here’s a comparison of performances right from the paper.

![img_yolo](../images/ch14_yolov3_benchmark01.jpeg)

In benchmarks, where this number is higher (say, COCO 75), the boxes need to be aligned more perfectly to be not rejected by the evaluation metric. Here is where YOLO is outdone by RetinaNet.

![img_yolo](../images/ch14_yolov3_benchmark02.jpeg)

Coco 50 and Coco 75 implies Coco dataset with IoU = 0.5 and 0.75.

#### <ins>References:</ins>

1. [YOLO, YOLOv2 and YOLOv3: All You want to know](https://medium.com/@amrokamal_47691/yolo-yolov2-and-yolov3-all-you-want-to-know-7e3e92dc4899)

2. [Real-time Object Detection with YOLO, YOLOv2 and now YOLOv3](https://medium.com/@jonathan_hui/real-time-object-detection-with-yolo-yolov2-28b1b93e2088)

3. [What’s new in YOLO v3?](https://towardsdatascience.com/yolo-v3-object-detection-53fb7d3bfe6b)







