# MNIST-Classifier

Project for the Neural Networks course, where we worked on parameter optimization of an MLP network developed by [Michael Nielsen](https://github.com/MichalDanielDobrzanski/DeepLearningPython35) based on the feedforward algorithm.

## Description

To improve the accuracy rate (by 92.66% in the base project provided by Michael), we made changes to the number of epochs, minibatch_size and learning_rate parameters. To further analyze the training performance as well as the individual performance of each of the training classes, we have modified the 'network.py' file by inserting a plot function responsible for generating the overall performance and performance graphs by class.

A total of 14 tests were performed, with specific variations of the mentioned parameters. If you would like to understand step by step how we arrived at our final result of 97.91% total accuracy, the 'analysis_report.pdf' file contains the description of each test as well as our observations regarding the results obtained in each.

## Conclusion

Following our tests, we concluded that the addition of more intermediate layers allows the network to have a smoother convergence, with the individual accuracy of each class experiencing fewer abrupt variations. We also realized that we were able to achieve this convergence using a low (1.0) learning rate and a batch size of 0.2% of the total dataset. These conclusions apply specifically to the problem under analysis and may have different results depending on the problem to be addressed.

![Accuracies per neuron](https://raw.githubusercontent.com/luccafranca/MNIST-Classifier/master/images/Accuracies_per_neuron/test14.png?token=AFQQUSZ63IKIBHN5VSEHYYC5QIUIS)

![Result Accuracies](https://raw.githubusercontent.com/luccafranca/MNIST-Classifier/master/images/Result_accuracies/test14.png?token=AFQQUS2J2FNWSS2XQ3UVNKC5QIUQO)


## Authors

- [Jacqueline Alves](https://github.com/jacquealvesb) - jacque.alves.b@gmail.com
- [Lucca França](https://github.com/luccafgf) - lfgf@cin.ufpe.br
