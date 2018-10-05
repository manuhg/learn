## Manu Hegde

#### Batch 7

#### Convolution

A convolution is a process in which a function or a kernel extracts a specific pattern from given input space (may contain one or more channels). Mathematically, a convolution is a similarity function over two input functions. This can be related to kernel and input channel being input functions and output channel being a result of similarity of input channel to kernel. Meaning, a kernel looks for a specific pattern and hence same or similar patterns are extracted as a function of similarity.  In case of successive convolutions, output of one convolution is input of the next. In a sequential arrangement of convolutions, the receptive fields increase linearly if the convolution is not 1x1. This is operation is a foundation for creating a CNN (Convulsional Neural Network). 

We may, in lay man terms say that a convolution is decompressing the given output.

![convolution](/home/manu/dev/learn/ml/eip/convolution.jpeg)



#### Filters/Kernels

A Filter or a Kernel is a mathematical mask that detects or extracts a particular pattern or ones that are very similar to it,  from the input channel during a convolution. It may be considered as a benchmark, patterns closely similar to which are extracted. When the kernel performs a convolution over an input channel it produces one output channel. A kernel usually makes the output channel smaller by resolution than the input channel, but by doing so increases the receptive field.  A 1x1 kernel is an exception where the input and output channels have the same resolution. Kernels can be of various sizes but a 3x3 kernel is used very extensively.

#### Epochs

Epoch in neural networks is one forward propagation and  one backward propagation on every input sample in the entire training dataset. The key factor here is the back propagation which will tune the CNN (Convulsional Neural Networks). A backpropagation can only happen after a forward propagation hence they are performed sequentially. With every backpropagation, the error of the network's output decreases. 

Due to memory constraints of GPU, inputs are taken in small batches, hence more epochs can lead to different subsets considered as a batch.  Also there is a practice of changing learning rate with every few epochs. Both of these factors can help increase the accuracy of the network very significantly. However making too many epochs can lead to overfitting and lead to poor performance on a previously unknown input case.

Usually 10 epochs are done. 

#### 1x1 convolution

A convolution performed is 1x1 when a 1x1 kernel is used. yields output channel of same size as the input channel, in case of 2D input space. In case of higher dimension (ex: 3D) input space, it reduces the number of dimensions to 1. Hence this is used for dimensionality reduction. It is often used to reduce the number of channels without affecting the receptive field, thus reducing the number of computations. However a 1x1 convolution can still perform pattern detection/extraction as well. It plays a crucial role in the modern CNNs. It is simple yet very powerful.

#### 3x3 convolution

A convolution performed is 3x3 when a 3x3 kernel is used. A 3x3 convolution yields an output that is smaller than the input by 2 units in each dimension. For example if input channel is 32x32, a 3x3 convolution will produce a 30x30 output channel.  This kernel is used extensively since it is small in terms of computation and all other larger kernels can be expressed as sequential combination of 3x3 convolutions. Hardwares are often optimized for a 3x3 convolutional kernel. 

For example if we perform a 9x9 convolution over a channel of resolution 9x9 the output is 1x1. This may also be obtained by using a 3x3 kernel as follows.

| input | kernel | output |
| ----- | ------ | ------ |
| 9x9   | 3x3    | 7x7    |
| 7x7   | 3x3    | 5x5    |
| 5x5   | 3x3    | 3x3    |
| 3x3   | 3x3    | 1x1    |

 

#### Feature Maps

#### Feature Engineering (older computer vision concept)

#### Activation Function

#### How to create an account on GitHub and upload a sample project

#### Receptive Field.

#### 10 examples of use of [MathJax ](https://support.typora.io/Markdown-Reference/#math-blocks) in Markdown

