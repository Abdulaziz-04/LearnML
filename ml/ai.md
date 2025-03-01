# AI Notes

<!-- MarkdownTOC -->

- Bias vs Variance Tradeoff
- Machine Learning
  - Analyze the Data
  - Process the data
  - Transform the data
- Artificial Intelligence
  - How to Choose the Right AI Algorithm
  - Artificial Intelligence Tutorial : All you need to know about AI
- Deep Learning
  - Challenges
  - Applications
- Machine Learning for Humans
- Neural Networks and Deep Learning
- Deep learning applications
- Reinforcement Learning
- Gradient descent
- What is online learning?
- References

<!-- /MarkdownTOC -->

**Occam’s Razor:** 

- Prefer the simplest hypothesis consistent with the data.

- The simplest solution is always the best

- The simplest model that correctly fits the data is the most consistent.

**bootstrap** means to randomly draw (with replacement) rows from the training dataset.


**No Free Lunch Theorem:** Any two algorithms are equivalent when their performance is averaged across all possible problems. 

Thus, a general-purpose universal optimization strategy is theoretically impossible and the only way one strategy can outperform another is if it is specialized to the specific problem under consideration. 


## Bias vs Variance Tradeoff

The bias-variance trade-off will help us understand the concepts of models over-fitting and under-fitting to training data.



## Machine Learning

How to choose the right machine learning algorithm?)

1. Categorize the problem

Categorize by the input: 

- If it is a labeled data, it id a supervised learning problem. 

- If it is unlabeled data with the purpose of finding structure, it is an unsupervised learning problem. 

- If the solution implies to optimize an objective function by interacting with an environment, it is a reinforcement learning problem.

Categorize by output: 

- If the output of the model is a number, it is a regression problem. 

- If the output of the model is a class, it is a classification problem. 

- If the output of the model is a set of input groups, it is a clustering problem.

2. Understand the Data

The process of understanding the data plays a key role in the process of choosing the right algorithm for the right problem. 

Some algorithms can work with smaller sample sets while others require tons and tons of samples. 

Certain algorithms work with categorical data while others like to work with numerical input.

### Analyze the Data

There are two important tasks: 

- descriptive statistics
- visualization and plots

### Process the data

The components of data processing include pre-processing, profiling, and cleansing which often involve pulling together data from multiple sources.

### Transform the data

The idea of transforming data from a raw state to a state suitable for modeling is where feature engineering comes in. 

Feature engineering is the process of transforming raw data into features that better represent the underlying problem to improve model accuracy on unseen data.

3. Find the available algorithms

The next milestone is to identify the algorithms that are applicable that can be implemented in a reasonable time. 

Some of the elements affecting the choice of a model are:

- The accuracy of the model.
- The interpretability of the model.
- The complexity of the model.
- The scalability of the model.

- How long does it take to build, train, and test the model?

- How long does it take to make predictions using the model?

- Does the model meet the business goal?

4. Implement the machine learning algorithms.

Create an ML pipeline that compares the performance of each algorithm on the dataset using a set of evaluation criteria. 

5. Optimize hyperparameters. 

There are three main options for optimizing hyperparameters: grid search, random search, and Bayesian optimization.


[Choosing the right estimator](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)


------


## Artificial Intelligence

Artificial Intelligence = A technique which enables machines to mimic human behavior.

Machine Learning = A subset of AI which uses statistical methods to enable machines to improve with experience.

Deep Learning = A subset of ML which makes the computation of multi-layer neural networks feasible.


### How to Choose the Right AI Algorithm

- [Artificial Intelligence Algorithms: All you need to know](https://www.edureka.co/blog/artificial-intelligence-algorithms)

- [A Comprehensive Guide To Artificial Intelligence With Python](https://www.edureka.co/blog/artificial-intelligence-with-python/)

- [AI vs Machine Learning vs Deep Learning](https://www.edureka.co/blog/ai-vs-machine-learning-vs-deep-learning/)


------


### [Artificial Intelligence Tutorial : All you need to know about AI](https://www.edureka.co/blog/artificial-intelligence-tutorial/)

- What is Artificial Intelligence?
- Importance of Artificial Intelligence
- Artificial Intelligence Applications
- Domains of Artificial Intelligence
- Different Job Profiles in AI
- Companies Hiring

------

K-Nearest Neighbors Algorithm in Python and Scikit-Learn (StackAbuse)
k-nearest neighbor algorithm in Python (GeeksforGeeks)

Building A Book Recommender System (DataScience+)


------


## Deep Learning

An _artificial neural network (ANN)_ is a computing system inspired by the biological neural networks that constitute animal brains. Such systems learn (progressively improve their ability) to do tasks by considering examples (generally without task-specific programming).

For example, in image recognition they might learn to identify images that contain cats by analyzing example images that have been manually labeled as "cat" or "no cat" and using the analytic results to identify cats in other images. They have found most use in applications difficult to express with a traditional computer algorithm using rule-based programming.

A _deep neural network (DNN)_ is an ANN with multiple layers between the input and output layers. The DNN finds the correct mathematical manipulation to turn the input into the output, whether it be a linear relationship or a non-linear relationship. The network moves through the layers calculating the probability of each output.

For example, a DNN that is trained to recognize dog breeds will go over the given image and calculate the probability that the dog in the image is a certain breed. The user can review the results and select which probabilities the network should display (above a certain threshold, etc.) and return the proposed label. Each mathematical manipulation as such is considered a layer, and complex DNN have many layers, hence the name "deep" networks.

In deep learning, a _convolutional neural network (CNN)_ is a class of deep neural networks that is usually used to analyze visual images. They are also known as shift invariant or space invariant artificial neural networks (SIANN) based on their shared-weights architecture and translation invariance characteristics. They have applications in image and video recognition, recommender systems, image classification, medical image analysis, natural language processing, and financial time series.

CNNs are regularized versions of _multilayer perceptrons_ which usually means fully connected networks -- each neuron in one layer is connected to all neurons in the next layer. However, the "fully-connectedness" of these networks makes them prone to overfitting data. Typical ways of regularization include adding some form of magnitude measurement of weights to the loss function. CNNs take a different approach towards regularization: they take advantage of the hierarchical pattern in data and assemble more complex patterns using smaller and simpler patterns. Therefore, on the scale of connectedness and complexity, CNNs are on the lower extreme.

### Challenges

As with ANNs, many issues can arise with naively trained DNNs. Two common issues are: overfitting and computation time.

DNNs are prone to overfitting because of the added layers of abstraction, which allow them to model rare dependencies in the training data. Regularization methods such as Ivakhnenko's unit pruning or weight decay or sparsity can be applied during training to combat overfitting. Alternatively dropout regularization randomly omits units from the hidden layers during training. This helps to exclude rare dependencies. Finally, data can be augmented via methods such as cropping and rotating such that smaller training sets can be increased in size to reduce the chances of overfitting.

DNNs must consider many training parameters, such as the size (number of layers and number of units per layer), the learning rate, and initial weights. Sweeping through the parameter space for optimal parameters may not be feasible due to the cost in time and computational resources. Various tricks, such as batching (computing the gradient on several training examples at once rather than individual examples) speed up computation. Large processing capabilities of many-core architectures (such as GPUs or the Intel Xeon Phi) have produced significant speedups in training, because of the suitability of such processing architectures for the matrix and vector computations

### Applications

- Automatic speech recognition
- Image recognition
- Visual art processing
- Natural language processing
- Drug discovery and toxicology
- Customer relationship management
- Recommendation systems
- Bioinformatics
- Medical Image Analysis
- Mobile advertising
- Image restoration
- Financial fraud detection
- Military


------


## [Machine Learning for Humans](https://medium.com/machine-learning-for-humans/why-machine-learning-matters-6164faf1df12)

**Artificial intelligence** is the study of agents that perceive the world around them, form plans, and make decisions to achieve their goals.

Many fields fall under the umbrella of AI such as: computer vision, robotics, machine learning, and natural language processing.

Machine learning is a subfield of artificial intelligence. The goal of ML is to enable computers to learn on their own. 

An ML algorithm enables a machine to identify patterns in observed data, build models that explain the world, and predict things without having explicit pre-programmed rules and models.

The technologies discussed above are examples of **artificial narrow intelligence (ANI)** which can effectively perform a narrowly defined task.

We are also continuing to make foundational advances towards human-level **artificial general intelligence (AGI)** or _strong AI_. 

The definition of AGI is an artificial intelligence that can successfully perform _any intellectual task_ that a human being can: learning, planning and decision-making under uncertainty, communicating in natural language, making jokes, manipulating people, trading stocks, or reprogramming itself.

------


## Neural Networks and Deep Learning

[Neural Networks and Deep Learning](https://medium.com/machine-learning-for-humans/neural-networks-deep-learning-cdad8aeae49b)

Some extensions and further concepts worth noting:

- Deep learning software packages. You will rarely need to implement all the parts of neural networks from scratch because of existing libraries and tools that make deep learning implementations easier. There are many of these: TensorFlow, Caffe, Torch, Theano, and more.

- **Convolutional neural networks (CNNs)** are designed specifically for taking images as input and are effective for computer vision tasks. They are also instrumental in deep reinforcement learning. CNNs are inspired by the way animal visual cortices work and they are the focus of the deep learning course we have been referencing throughout this article (Stanford’s CS231n).

- **Recurrent neural networks (RNNs)** have a kind of built-in memory and are well-suited for natural language problems. They are also important in reinforcement learning since they enable the agent to keep track of where things are and what happened historically even when those elements are not all visible at once. In fact, both RNNs and LSTMs are often used in the context of natural language problems.

- **Deep reinforcement learning** is one of the most exciting areas of deep learning research, at the heart of recent achievements in AI. We will dive deeper in Part 5, but essentially the goal is to apply all of the techniques in this post to the problem of teaching an agent to maximize reward. This can be applied in any context that can be gamified — from actual games like Counter Strike or Pacman, to self-driving cars, to trading stocks, to real life and the real world.


## Deep learning applications

Here are a few examples of the incredible things that deep learning can do:

- Facebook trained a neural network augmented by short-term memory to intelligently answer questions about the plot of "Lord of the Rings".

- Self-driving cars rely on deep learning for visual tasks like understanding road signs, detecting lanes, and recognizing obstacles.

- Predicting molecule bioactivity for drug discovery

- Face and object recognition for photo and video tagging

- Powering Google search results

- Natural language understanding and generation, e.g. Google Translate

- The Mars explorer robot Curiosity is autonomously selecting inspection-worthy soil targets based on visual examination


------


## Reinforcement Learning

Reinforcement learning is an artificial intelligence approach that focuses on the learning of the system through its interactions with the environment.

In reinforcement learning, the system’s parameters are adapted based on the feedback obtained from the environment which in turn provides feedback on the decisions made by the system. 

The following diagram shows a person making decisions in order to arrive at their destination.

One day you and decide to try a different route with a view to finding the shortest path. 

This dilemma of trying out new routes or sticking to the best-known route is an example of **exploration** versus **exploitation**:


## Gradient descent

Gradient descent is used in ML and DL to optimize the models in an iterative process by taking the gradient (derivative) of the _loss_ function. 

Gradient descent takes more computational resources to optimize, so SGD can be used which requires less computation power because it takes only one data point to optimize, but SGD requires a lot of iterations to reach the destination. 

Mini-batch gradient descent is the perfect balance between the above-spoken methods which takes fewer iterations than SGD to converge and less computation power than Gradient descent.


## What is online learning?

We define online learning as a training scenario in which the full dataset is never available to the model at the same time. 

The model is exposed to the portions of the dataset sequentially and expected to learn the full training task through such partial exposures. 

After being exposed to a certain portion of the dataset, the model is not allowed to re-visit this data later on. Otherwise, the model could simply loop over the dataset and perform a normal training procedure.


## References

[Do you know how to choose the right machine learning algorithm among 7 different types?](https://towardsdatascience.com/do-you-know-how-to-choose-the-right-machine-learning-algorithm-among-7-different-types-295d0b0c7f60)

[1] aima-python: Python code for Artificial Intelligence: A Modern Approach. Accessed: June 14, 2020. [Online]. Available: https://github.com/aimacode/aima-python, 0.17.3. 2020.

[2] S. Russell and P. Norvig, Artificial Intelligence: A Modern Approach, 3rd ed. Upper Saddle River, NJ, USA: Prentice Hall, 2010.


