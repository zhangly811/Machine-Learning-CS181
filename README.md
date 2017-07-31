# Machine-Learning-CS181
CS181 is a Machine Learning course offerred at Harvard SEAS. I completed 4 group projects in this course, which involves solving regression, classification, or problems using supervised and unsupervised methods.

## Practical 1: Predicting the Efficiency of Organic Photovoltaics
This project is part of Harvard Clean Energy Project aiming at finding a good organic photovoltaic molecules to replace silicon semiconductors in solar cells. Our goal is to build a regression model that predicts the energy of each molecule based on features extracted from chemical formula. We trained several regression models on 10,000 molecules, and validated the performance using R-square on the validation set. Out of the several models we trained, random forest achieved the best performance with R-square 0.93 on the validation set.

## Practical 2: Classifying Malicious Software
In this practical, we classified executable files collected from people?s computers (over a period of several days) into any of 14 known malware classes, or determine that the executables are not malware. We trained on ~2000 executables of known provenance, and validated on ~1000 executables. We explored classification models such as logistic regression, LDA/QDA, Decision Trees, Random Forests, and SVMs. We also explored priors and balancing the weights of our training data to account for the class imbalances, as some forms of malware were rare.   
Overall, random forest had the best mean accuracy(0.87) compared to the other methods under the same condition.

## Practical 3: Preferences in Streaming Music
For this practical, we were tasked with predicting people?s tastes in music. Specifically, we tried to predict the number of times (a non-negative integer) different users listened to tracks of different artists over a span of time. We had some basic self-reported demographic information about many, but not all, of the users, such as sex, age, and location. We also had the name of the artist and their MusicBrainz1 ID, if available. There were about 233,000 users and 2,000 artists. The training set had over 4.1M user/artist pairs and the test set is of a similar size. Our objective is to predict how many times a user will listen to a new artist.   
In this practical, we classified executable files collected from people’s computers (over a period of several days) into any of 14 known malware classes, or determine that the executables are not malware. We trained on ~2000 executables of known provenance, and validated on ~1000 executables. We explored classification models such as logistic regression, LDA/QDA, Decision Trees, Random Forests, and SVMs. We also explored priors and balancing the weights of our training data to account for the class imbalances, as some forms of malware were rare.   
Overall, random forest had the best mean accuracy(0.87) compared to the other methods under the same condition.

## Practical 3: Preferences in Streaming Music
For this practical, we were tasked with predicting people’s tastes in music. Specifically, we tried to predict the number of times (a non-negative integer) different users listened to tracks of different artists over a span of time. We had some basic self-reported demographic information about many, but not all, of the users, such as sex, age, and location. We also had the name of the artist and their MusicBrainz1 ID, if available. There were about 233,000 users and 2,000 artists. The training set had over 4.1M user/artist pairs and the test set is of a similar size. Our objective is to predict how many times a user will listen to a new artist.   
We first did feature engineering on both artists and users. Then we trained models on a sub-popluaiton of the training data, such as Bayesian Network, Matrix factorization and Completion, and Generalized linear mixed model. Instead of training on individuals, we also tried clustering users using K-means, the idea behind which was that predicting plays by individual's information may overfit the data. Our best model was Generalized linear mixed model with mean absolute error (MAE) 135.8. 

## Practical 4: Reinforcement Learning
This practical focuses on using reinforcement learning method to develop an agent to play the game Swingy Monkey, a game similar to Flappy Bird. The agent can make the monkey jump to a new vine, or swing down the current vine he is holding, in order to pass the tree trunks coming from both the top and the bottom of the screen. Positive re- ward is given when the monkey successfully passes tree trunks without hitting them, and different negative rewards are given when the monkey falls off the bottom of the screen, jumps off the top, or hit a tree trunk. A better agent is defined as an agent that can achieve higher average score and max score within a certain number of game iterations. Our goal is to train a good agent through various reinforcement learning method (SARSA and Q- learning), and compare their performance with different policy and hyper-parameters on discretized space.
