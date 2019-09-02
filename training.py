import mnist_loader as mn
import network

training_data, validation_data, test_data = mn.load_data_wrapper()

net = network.Network([784, 30, 20, 10])

net.SGD(training_data, 30, 50, 3.0, monitor_evaluation_accuracy=True, evaluation_data=test_data)