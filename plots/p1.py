import matplotlib.pyplot as plt
import numpy as np

# Data for MNIST dataset
mnist_clients = [4, 8, 12, 16, 20]
mnist_acc_no_defence = [20.98, 22.01, 23.25, 27.01, 28.78]
mnist_acc_guardfl = [97.69, 97.68, 97.81, 97.79, 97.68]

# Data for CIFAR10 dataset
cifar_clients = [4, 8, 12, 16, 20]
cifar_acc_no_defence = [44.97, 43.26, 43.52, 43.23, 44.99]
cifar_acc_guardfl = [52.34, 53.68, 52.43, 54.64, 51.88]

# Data for FEMNIST dataset
femnist_clients = [4, 8, 12, 16, 20]
femnist_acc_no_defence = [36.78,47.31,40.67,41.19,42.33]
femnist_acc_guardfl = [85.0566667, 84.7733333, 85.1911111, 85.1541667, 84.99]

# Plotting the accuracy for each dataset
plt.figure(figsize=(10, 6))

plt.plot(mnist_clients, mnist_acc_no_defence, marker='o', linestyle='dotted', label='MNIST - No Defence', color = '#FF5733' )
plt.plot(mnist_clients, mnist_acc_guardfl, marker='o', linestyle='-', label='MNIST - GuardFL', color = '#FF5733')

plt.plot(cifar_clients, cifar_acc_no_defence, marker='o', linestyle='dotted', label='CIFAR10 - No Defence' , color = '#33FF57')
plt.plot(cifar_clients, cifar_acc_guardfl, marker='o', linestyle='-', label='CIFAR10 - GuardFL' , color = '#33FF57')

plt.plot(femnist_clients, femnist_acc_guardfl, marker='o', linestyle='-', label='FEMNIST - GuardFL' , color = '#5733FF')
plt.plot(femnist_clients, femnist_acc_no_defence, marker='o', linestyle='dotted', label='FEMNIST - No Defence' , color = '#5733FF')

plt.xlabel('Number of Clients')
plt.ylabel('Accuracy (%)')
plt.title('Accuracy vs Number of Clients for Different Datasets')
plt.legend()
plt.grid(True)
plt.xticks(np.arange(0, 21, 2))
plt.ylim(0, 100)
plt.tight_layout()

plt.show()
plt.savefig('num_of_client_Accuracy.png')
