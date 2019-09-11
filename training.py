import mnist_loader as mn
import network

# constants 
img_size = 28
output_size = 10

# variables
epochs = 100
minibatch_size = 2000
learning_rate = 1.0

training_data, validation_data, test_data = mn.load_data_wrapper()

net = network.Network([img_size*img_size, 200, 200, output_size])

net.SGD(training_data, 
        epochs, 
        minibatch_size, 
        learning_rate, 
        monitor_evaluation_accuracy=True, 
        evaluation_data=test_data)