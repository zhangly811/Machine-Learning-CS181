## Practical 3: Preferences in Streaming Music

For this practical, we were tasked with predicting people?s tastes in music. Specifically, we tried to predict the number of times (a non-negative integer) different users listened to tracks of different artists over a span of time. We had some basic self-reported demographic information about many, but not all, of the users, such as sex, age, and location. We also had the name of the artist and their MusicBrainz1 ID, if available. There were about 233,000 users and 2,000 artists. The training set had over 4.1M user/artist pairs and the test set is of a similar size. Our objective is to predict how many times a user will listen to a new artist.   
In this practical, we classified executable files collected from people’s computers (over a period of several days) into any of 14 known malware classes, or determine that the executables are not malware. We trained on ~2000 executables of known provenance, and validated on ~1000 executables. We explored classification models such as logistic regression, LDA/QDA, Decision Trees, Random Forests, and SVMs. We also explored priors and balancing the weights of our training data to account for the class imbalances, as some forms of malware were rare.   
Overall, random forest had the best mean accuracy(0.87) compared to the other methods under the same condition.