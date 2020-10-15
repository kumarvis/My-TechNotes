# Loading and Preprocessing Data with TensorFlow

## Structure of TensorFlow data pipelines:

The structure of *tf.data* pipelines directly follows these best practices.

### Extract, Transform, Load(ETL): 
ETL is a common paradigm for data processing in
computer science. In computer vision, ETL pipelines in charge of feeding models with
training data usually look like this:

![img_data_pipeline](../images/ch13_datapipeline01.png)

**Extraction step:** This step is about exploring the data sources and extracting their content. These sources may be listed explicitly by a document, example: A CSV file containing the filenames for all the images, or implicitly with all the dataset's images
already stored in a specific folder. Basically where is the RAW Data? Output of this instance is ***Object of Datatype tf.data.Dataset***

**Transform step:** Parsing of extracted data samples into a common format. For
instance, this means parsing the bytes read from image files into a matrix representation (for instance, to decode JPEG or PNG bytes into image tensors). Other heavy transformations can be applied in this step, such as **cropping/scaling images to the same dimensions, or augmenting** them with various random operations.

**Load step** Once ready, the data is loaded into the target structure. For the training of machine learning methods, this means sending the batch samples into the device in charge of running the model, such as the selected GPU(s). The processed dataset can also be cached/saved somewhere for later use.

## Building an image data pipeline:

We assume we already have a list of filenames to jpeg images and a corresponding list of labels. We apply the following steps for training:

1. Create the dataset from slices of the filenames and labels(Extraction step).

```
    dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))
```

2. Repeat() method repeat(3) on the original dataset, and it
returns a new dataset that will repeat the items of the original dataset three times. Of
course, this will not copy all the data in memory three times. If you call this method
with no arguments, the new dataset will repeat the source dataset forever, so the code
that iterates over the dataset will have to decide when to stop.

```
    #Repeat dataset forever
    dataset = dataset.repeat()
```

3. Shuffle the data with a buffer_size [buffer_size reference](https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle/48096625#48096625)
which may be equal to the length of the dataset.

```
    dataset = dataset.shuffle(len(filenames))
```

4. Parse the images from filename to the pixel values. Use multiple threads to improve the speed of preprocessing.

```
dataset = dataset.map(parse_function, num_parallel_calls=4)
```

### The parse_function will do the similar activity like below:

1. read the content of the file
2. decode using jpeg/png format
3. convert to float values in [0, 1]
4. resize to size (64, 64)

```
def parse_function(filename, label):
    image_string = tf.read_file(filename)

    #Don't use tf.image.decode_image, or the output shape will be undefined
    #This is just pseudo code
    image = tf.image.decode_jpeg(image_string, channels=3)

    #This will convert to float values in [0, 1]
    image = tf.image.convert_image_dtype(image, tf.float32)

    image = tf.image.resize_images(image, [64, 64])
    return resized_image, label
```

5. (Optional for training) Data augmentation for the images. Use multiple threads to improve the speed of preprocessing

```
    dataset = dataset.map(train_preprocess, num_parallel_calls=4)
```

### The train_preprocess can be used during training to perform data augmentation

Example of augmentation:

1. Horizontally flip the image with probability 0.5
2. Apply random brightness and saturation

```
def train_preprocess(image, label):
    image = tf.image.random_flip_left_right(image)

    image = tf.image.random_brightness(image, max_delta=32.0 / 255.0)
    image = tf.image.random_saturation(image, lower=0.5, upper=1.5)

    #Make sure the image is still in [0, 1]
    image = tf.clip_by_value(image, 0.0, 1.0)

    return image, label
```

6. Batch the images

```
    dataset = dataset.batch(batch_size)
```

7. By calling prefetch(1) at the end, we are creating a dataset that will do its best to
always be one batch ahead to serve the model.

```
    dataset = dataset.prefetch(1)
```

**Steps from 2-7 falls under the TRANSFROM step.**

### References:

1. [Building a data pipeline](https://cs230.stanford.edu/blog/datapipeline/)

2. [How To Classify Images with TensorFlow - a Step-By-Step Tutorial](https://lambdalabs.com/blog/how-to-classify-images-with-tensorflow-a-step-by-step-tutorial/#inputter)

3. [Lambda Deep Learning Demos](https://github.com/lambdal/lambda-deep-learning-demo)

4. [HANDSON_COMPUTER_VISION_WITH_TENSORFLOW_2](https://github.com/PacktPublishing/Hands-On-Computer-Vision-with-TensorFlow-2)







