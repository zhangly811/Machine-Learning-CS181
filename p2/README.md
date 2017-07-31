## Practical 2: Classifying Malicious Software

In this practical, we classified executable files collected from people?s computers (over a period of several days) into any of 14 known malware classes, or determine that the executables are not malware. We trained on ~2000 executables of known provenance, and validated on ~1000 executables. We explored classification models such as logistic regression, LDA/QDA, Decision Trees, Random Forests, and SVMs. We also explored priors and balancing the weights of our training data to account for the class imbalances, as some forms of malware were rare.   
Overall, random forest had the best mean accuracy(0.87) compared to the other methods under the same condition.
