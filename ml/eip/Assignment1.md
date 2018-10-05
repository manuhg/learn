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

Feature maps is a collection of features detected by kernels in a given layer of CNN, arranged spatially according the the region they were detected. Feature maps hence tell us which feature was found where. Hence further going deep in a CNN, feature map from previous layer(s) can be used to detect more complex features. Say for example to detect an Face, 												input => lines => curves => 2D shapes like circle,etc => eyes/nose/ears => Face. As receptive field increases, smaller features can be combined to yield more meaningful features.



#### Feature Engineering (older computer vision concept)

Earlier, in computer vision use of neural networks was not prevalent. Hence the questions of what features to be extracted at what layer and what to ignore was decided solely by the human/researcher. This required the researchers to have significant domain knowledge and intricacies and pitfalls. Failing which would fail the model. Hence evaluating of features and their contribution in yielding a desired output was termed as Feature Engineering. This was very crucial since features are the most important things that define the success or failure of a model. We can hence in short say, Feature engineering is deciding features for a computer vision model, based on domain knowledge and human experience and evaluating their contribution.



#### Activation Function

Activation function is an idea derived from biology. In biology an activation potential defines the chances of a neuron firing to a specific stimulus. This can be quantified in a binary form or in a non linear form. Activation function is non linear, i.e output value is related to input value logically but not linearly. As shown in the figure below the product of inputs and weights are passed to the activation function to yield input.

Activation function is the key factor in a neural network since it introduces non linearity.

Activation function serves like a threshold function, the threshold or the decision boundary varies based on the accuracy of the model i.e more the accuracy, the decision boundary segregates output in more accurate fashion.

![Activation Function](/home/manu/dev/learn/ml/eip/activation-function.png)



#### How to create an account on GitHub and upload a sample project

GitHub is very popular open source platform to host projects (publicly or privately) and share code.

Steps to create an account and upload a sample project are as follows

i) Log on to https://github.com

ii) Enter a desired user name, your email id and a password ( not related to password of your email id ). It is recommended to keep a meaningful user name or at least avoid numbers . Click on Sign up for GitHub.

![Github Signup](/home/manu/dev/learn/ml/eip/github_signup.png)

iii) Chose a plan, i.e use a free plan if you do not need to have private repositories. However if you want private repositories and you can prove you are a university student, you can get unlimited free repositories for 2 years for free by applying [here](https://education.github.com/pack). Otherwise chose paid plan. If you are an enterprise/organization you may select to setup the same. Click on continue.

iv)  Answer the questions related to your experience with programming or you may choose to skip it. Click on submit or skip to go to next step. 

v) Verify your email. This is important to proceed further. This is done by clicking on the link sent to your email id from GitHub.

vi) You can now create a new project by clicking on create repository and fill the details like repository name etc.

vii) You can upload files via browser and then commit it or do it via command line. To do via command line on your computer do as follows, assuming git is already installed on your computer.

```bash
git clone https://github.com/username/repo.git
cd repo
echo "Hello github!">Readme.md # add files to be uploaded
git add -A   # add files to staging area
git commit -m "Added some files" #add very short summary or purpose of commit as a message
git push origin master # finally push the commit to origin, in this case github.com
```



#### Receptive Field

Receptive field is the portion of the original input image a kernel at a given layer can effectively see. i.e since CNN starts by detecting basic shapes and then build upon them to detect more complex features, initially kernels look at small patches. As we go deeper i.e more layer from input layer, kernel sees the "bigger picture".  Finally at the output layer, the receptive field is the whole input image. The concept of increasing receptive field progressively, helps in achieving the result in by taking a bottom up approach.

#### 10 examples of use of [MathJax](https://support.typora.io/Markdown-Reference/#math-blocks) in Markdown

$$
\mathbf{W} = \begin{bmatrix}
\mathbf{w}_1^0&\mathbf{w}_1^1& \mathbf{w}_1^2&\cdots & \mathbf{w}_1^n \\
\mathbf{w}_2^0&\mathbf{w}_2^1& \mathbf{w}_2^2&\cdots & \mathbf{w}_2^n \\
\vdots & \vdots & \vdots & \cdots & \vdots \\
\mathbf{w}_m^0&\mathbf{w}_m^1& \mathbf{w}_m^2&\cdots & \mathbf{w}_m^n \\
\end{bmatrix} 
\mathbf{X} = \begin{bmatrix}
1&\mathbf{x}_1^1& \mathbf{x}_1^2&\cdots & \mathbf{x}_1^n \\
1&\mathbf{x}_2^1& \mathbf{x}_2^2&\cdots & \mathbf{x}_2^n \\
\vdots & \vdots & \vdots & \cdots & \vdots \\
1&\mathbf{x}_m^1& \mathbf{x}_m^2&\cdots & \mathbf{x}_m^n \\
\end{bmatrix} 
\mathbf{b} = \begin{bmatrix} \mathbf{b}_0 \\\mathbf{b}_1 \\ \vdots \\ \mathbf{b}_n\\ \end{bmatrix} 
\\
\mathbf{z} = (W \times X) + b \\
\mathbf{a} = g(\mathbf{z})
\\
\mathbf{h(x)} = \theta_1x_1+\theta_2x_2+\theta_1x_1+\cdots+\theta_nx_n\\
\mathbf{J}=(y-h(x))^2\\
\mathbf{v} = u+at \\
\mathbf{S}=ut + \frac12 at^2 \\
\mathbf{e}=\sum_{n=0}^{\infty} \frac1{n!}=2.71828\\
\mu = {\frac{{\sum_{i=1}^{n}}x_i}N}\\
\sigma = \sqrt {\frac{{\sum_{i=1}^{n}}(x_i-\mu)^2}N}
$$

