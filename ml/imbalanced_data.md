# Imbalanced Classification

<!-- MarkdownTOC -->

- Imbalanced Classification Problems
- Causes of Class Imbalance
- Challenge of Imbalanced Classification
- How to Handle Imbalanced Classes?
    - Can You Collect More Data?
    - Try Changing Your Performance Metric
    - Try Different Algorithms
    - Try a Different Perspective
    - Accuracy Paradox
- Handle Imbalanced Classification without Rebalancing
    - Reasons not to balance your imbalanced data
    - Conclusion
- Examples of Imbalanced Classification
- Naive Classifier
- Keras Imbalanced Classification
- References

<!-- /MarkdownTOC -->

An imbalanced classification problem is a problem that involves predicting a class label where the distribution of class labels in the training dataset is skewed (there are many more examples for one class than the other classes). 

Many real-world classification problems have an imbalanced class distribution, so it is important for ML engineers to be familiar with working with these types of problems.

Imbalanced classification poses a challenge for predictive modeling since most of ML algorithms used for classification were designed with the assumption of an equal number of examples for each class which results in models that have poor predictive performance, specifically for the minority class. 

This is a problem because the minority class is usually more important, so the problem is more sensitive to classification errors for the minority class than the majority class.

These types of problems often require the use of specialized performance metrics and learning algorithms as the standard metrics and methods are unreliable or fail completely.

Given measurements of a flower (observation), we may predict the likelihood (probability) of the flower being an example of each of twenty different species of flower.

The number of classes for a predictive modeling problem is typically fixed when the problem is framed and the number of classes usually does not change.

A classification predictive modeling problem may have two class labels  caled _binary classification_ or the problem may have more than two classes such as three, 10, or even hundreds of classes called _multi-class classification_ problems.

- Binary Classification Problem: A classification predictive modeling problem where all examples belong to one of two classes.

- Multiclass Classification Problem: A classification predictive modeling problem where all examples belong to one of three or more classes.

A training dataset is a number of examples from the domain that include both the input data (measurements) and the output data (class label).

Depending on the complexity of the problem and the types of models we choose, we may need tens, hundreds, thousands, or even millions of exampled from the domain to constitute a training dataset.

The training dataset is used to better understand the input data to help best prepare it for modeling to:

- Evaluate a suite of different modeling algorithms

- Tune the hyperparameters of a chosen model

- Train a final model on all available data that we can use to make predictions for new samples from the problem domain



## Imbalanced Classification Problems

The number of examples that belong to each class may be referred to as the _class distribution_.

NOTE: The tern _unbalanced_ refers to a class distribution that was balanced and is now no longer balanced whereas _imbalanced_ refers to a class distribution that is inherently not balanced.

There are other less general names that may be used to describe these types of classification problems:

- Rare event prediction
- Extreme event prediction
- Severe class imbalance

It is common to describe the imbalance of classes in a dataset in terms of a _ratio_. 

For example, an imbalanced binary classification problem with an imbalance of 1 to 100 (1:100) means that for every one example in one class, there are 100 examples in the other class.

Another way to describe the imbalance of classes in a dataset is to summarize the class distribution as percentages of the training dataset. 

For example, an imbalanced multiclass classification problem may have 80 percent examples in the first class, 18 percent in the second class, and 2 percent in a third class.


## Causes of Class Imbalance

The imbalance of the class distribution in an imbalanced classification predictive modeling problem may have many causes.

There are two main groups of causes for the imbalance we may want to consider: data sampling and properties of the domain.

It is possible that the imbalance in the examples across the classes is caused by the way the examples were collected or sampled from the problem domain which might involve biases introduced during data collection and errors made during data collection.

- Biased Sampling
- Measurement Error

The imbalance may also be a property of the problem domain.

For example, the natural occurrence or presence of one class may dominate other classes which may be because the process that generates observations in one class is more expensive in time, cost, computation, or other resources. 

Thus, it is often infeasible or intractable to simply collect more samples from the domain to improve the class distribution. Instead, a model is required to learn the difference between the classes.



## Challenge of Imbalanced Classification

The imbalance of the class distribution will vary across problems.

A classification problem may be a little skewed such as a slight imbalance. 

- Slight Imbalance: An imbalanced classification problem where the distribution of examples is uneven by a small amount in the training dataset (4:6).

- Severe Imbalance: An imbalanced classification problem where the distribution of examples is uneven by a large amount in the training dataset (1:100 or more).

Most of the contemporary works in class imbalance concentrate on imbalance ratios ranging from 1:4 up to 1:100. 

In real-life applications such as fraud detection or cheminformatics, we may deal with problems with an imbalance ratio ranging from 1:1000 up to 1:5000.

A slight imbalance is often not a concern and the problem can often be treated as a normal classification predictive modeling problem. 

A severe imbalance of the classes can be challenging to model and may require the use of specialized techniques.

- Majority Class: The class (or classes) in an imbalanced classification predictive modeling problem that has many examples.

- Minority Class: The class in an imbalanced classification predictive modeling problem that has few examples.

The abundance of examples from the majority class (or classes) can swamp the minority class. 

Most machine learning algorithms for classification models are designed and demonstrated on problems that assume an equal distribution of classes which means that a naive application of a model may focus on learning the characteristics of the majority class  while neglecting the examples from the minority class. 

Imbalanced classification remains an open problem generally and practically must be identified and addressed specifically for each training dataset.


## How to Handle Imbalanced Classes?

Imbalanced data typically refers to a problem with classification problems where the classes are not represented equally.

1. Can You Collect More Data?
2. Try Changing Your Performance Metric
3. Try Different Algorithms
4. Try Penalized Models
5. Try a Different Perspective

6. Try Resampling Your Dataset
7. Try Generating Synthetic Samples
8. Try Getting Creative

### Can You Collect More Data?

Consider whether you are able to gather more data.

A larger dataset may expose a more balanced perspective of the classes.

More examples of the minor classes may be useful later for resampling the dataset.

### Try Changing Your Performance Metric

Accuracy is not the metric to use when working with an imbalanced dataset. since it can be misleading.

There are metrics that have been designed for imbalanced classes.

Consider the following performance measures that can give more insight into the accuracy of the model than traditional classification accuracy:

- Confusion Matrix: A breakdown of predictions into a table showing correct predictions (the diagonal) and the types of incorrect predictions made (what classes that incorrect predictions were assigned).

- Precision: A measure of a classifiers exactness.

- Recall: A measure of a classifiers completeness

- F1 Score (or F-score): A weighted average of precision and recall.

- ROC Curves: Similar to precision and recall, accuracy is divided into sensitivity and specificity and models can be chosen based on the balance thresholds of these values.

Also take a look at the following:

- Kappa (or Cohen’s kappa): Classification accuracy normalized by the imbalance of the classes in the data.

### Try Different Algorithms

Be sure to spot-check a variety of different types of algorithms on a given problem.

Decision trees often perform well on imbalanced datasets since the splitting rules that look at the class variable used in the creation of the trees can force both classes to be addressed.

You can also try a few popular decision tree algorithms: C4.5, C5.0, CART, and Random Forest.

In fact, I have had good success using an ensemble of Gradient Boosting, XGBoost, and Random Forest with imbalanced datasets. 

### Try a Different Perspective

There are fields of study dedicated to imbalanced datasets that have their own algorithms, measures, and terminology.

Thinking about your problem from these perspectives can sometimes provide some insight into your problem: anomaly detection and change detection.

**Anomaly detection** is the detection of rare events such as a machine malfunction indicated by its vibrations or malicious activity by a program indicated by a sequence of system calls. 

The events are rare compared to normal operation.

This shift in thinking considers the minor class as the outlier class which might help you think of new ways to separate and classify samples.

**Change detection** is similar to anomaly detection but rather than looking for an anomaly we are looking for a change or difference that might be a change in behavior of a user based on usage patterns or bank transactions.

### Accuracy Paradox

The _accuracy paradox_ is used to describe the situation in which your accuracy measure indicates that you have excellent accuracy (such as 90%) but the accuracy is only reflecting the underlying class distribution (majority class).

The accuracy paradox is very common because classification accuracy is often the first measure we use when evaluating models on classification problems.



## Handle Imbalanced Classification without Rebalancing

When building a ML classification model using data with more instances of one class than another, the initial default classifier is often unsatisfactory because it classifies almost every sample as the majority class. 

Many articles show you how you could use oversampling (SMOTE) or undersampling or simply class-based sample weighting to retrain the model on “rebalanced” data, but this is not always necessary. 

Here we show how much you can do _without_ balancing the data or retraining the model.

We can simply adjust the the _threshold_ for which we say “Class 1” when the model’s predicted probability of Class 1 is above it in two-class classification rather than naïvely using the default classification rule which chooses whichever class is predicted to be most probable (lthreshold of 0.5). 

We will see how this gives us the flexibility to make any desired trade-off between false positive and false negative classifications while avoiding problems created by rebalancing the data.

We will use the credit card fraud identification data set from Kaggle to illustrate. 

- Each row of the data set represents a credit card transaction with the target variable Class==0 indicating a legitimate transaction and Class==1 indicating that the transaction turned out to be a fraud. 

- There are 284,807 transactions, of which only 492 (0.173%) are frauds — very imbalanced.

We will use a gradient boosting classifier since these often provide good results. 

In fact, the new scikit-learn’s `HistGradientBoostingClassifier` class is much faster than the original `GradientBoostingClassifier` when the data set is relatively large like this one.

### Reasons not to balance your imbalanced data

One reason to avoid “balancing” your imbalanced training data is that such methods bias/distort the resulting trained model’s probability predictions such that these become miscalibrated (by systematically increasing the model’s predicted probabilities of the original minority class) and are reduced to being merely relative ordinal discriminant scores rather than being accurate predicted class probabilities in the original (“imbalanced”) train and test set and future unseen data. 

In the event that such rebalancing for training is truly needed, we would have to recalibrate the predicted probabilities to a dataset having the original/imbalanced class proportions. 

Alternatively, we could apply a correction to the predicted probabilities from the balanced model — see "Balancing is Unbalancing".

Another problem with balancing your data by oversampling (compared to class-dependent instance weighting which does not have this problem) is that it biases naïve cross-validation which can lead to excessive overfitting that is not detected in the cross-validation. 

In cross-validation, each time the data gets split into a “fold” subset, there may be instances in one fold that are duplicates of (or were generated from) instances in another fold. Thus, the folds are not truly independent as cross-validation assumes — there is data “bleed” or “leakage”. 

For example see "Cross-Validation for Imbalanced Datasets" which describes how you could re-implement cross-validation correctly for this situation. 

In scikit-learn, at least for the case of oversampling by instance duplication (not necessarily SMOTE), this can be worked around by using `model_selection.GroupKFold` for cross-validation which groups the instances according to a selected group identifier that has the same value for all duplicates of a given instance.

### Conclusion

Instead of naïvely or implicitly applying a default threshold of 0.5 or immediately re-training using re-balanced training data, we can try using the original model (trained on the original “imbalanced” data set) and simply plot the trade-off between false positives and false negatives to choose a threshold that may produce a desirable result.



## Examples of Imbalanced Classification

Many of the classification predictive modeling problems that we are interested in solving in practice are imbalanced.

Most of the examples are binary classification problems and the examples from the minority class are rare, extreme, abnormal, or unusual in some way.

Many of the domains are described as “detection" which highlights the desire to discover the minority class amongst the abundant examples of the majority class.

[Imbalanced Classification with the Fraudulent Credit Card Transactions Dataset](https://machinelearningmastery.com/imbalanced-classification-with-the-fraudulent-credit-card-transactions-dataset/)

[Multi-Class Imbalanced Classification](https://machinelearningmastery.com/multi-class-imbalanced-classification/)

[Classification with Imbalanced Data](https://towardsdatascience.com/classification-with-imbalanced-data-f13ccb0496b3)


## Naive Classifier

The performance of naive classification models provides a baseline for comparison with other models.

The majority class classifier achieves better accuracy than other naive classifier models such as random guessing and predicting a randomly selected observed class label.

Naive classifier strategies can be used on predictive modeling projects via the `DummyClassifier` class in the scikit-learn library.

[How to Develop and Evaluate Naive Classifier Strategies Using Probability](https://machinelearningmastery.com/how-to-develop-and-evaluate-naive-classifier-strategies-using-probability/)


## Keras Imbalanced Classification

[Imbalanced classification: credit card fraud detection](https://keras.io/examples/structured_data/imbalanced_classification/)

[Large-scale multi-label text classification](https://keras.io/examples/nlp/multi_label_classification/)

[Sample weights](https://keras.io/guides/training_with_built_in_methods/#sample-weights)


## References

[A Gentle Introduction to Imbalanced Classification](https://machinelearningmastery.com/what-is-imbalanced-classification/) 

[Step-By-Step Framework for Imbalanced Classification Projects](https://machinelearningmastery.com/framework-for-imbalanced-classification-projects/)

[8 Tactics to Combat Imbalanced Classes in Your Machine Learning Dataset](https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/)

[How To Deal With Imbalanced Classification Without Rebalancing the Data](https://www.kdnuggets.com/2021/09/imbalanced-classification-without-re-balancing-data.html)

[How to handle Multiclass Imbalanced Data? Not SMOTE](https://towardsdatascience.com/how-to-handle-multiclass-imbalanced-data-say-no-to-smote-e9a7f393c310)


[Standard Machine Learning Datasets for Imbalanced Classification](https://machinelearningmastery.com/standard-machine-learning-datasets-for-imbalanced-classification/)

[Fitting Linear Regression Models on Counts Based Data](https://towardsdatascience.com/fitting-linear-regression-models-on-counts-based-data-ba1f6c11b6e1)

[Discrete Probability Distributions for Machine Learning](https://machinelearningmastery.com/discrete-probability-distributions-for-machine-learning/)

[SMOTE for Imbalanced Classification with Python](https://machinelearningmastery.com/smote-oversampling-for-imbalanced-classification/)



