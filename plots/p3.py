import matplotlib.pyplot as plt
import numpy as np

# Data for MNIST dataset
mnist_clients = [4, 8, 12, 16, 20]
mnist_time_no_defence = [200, 346, 510, 733, 972]
mnist_time_guardfl = [375, 426, 800, 761, 998]

# Data for CIFAR10 dataset
cifar_clients = [4, 8, 12, 16, 20]
cifar_time_no_defence = [200, 320, 373, 860, 2066]
cifar_time_guardfl = [257, 850, 1145, 534, 1232]

femnist_clients = [4, 8, 12, 16, 20]
femnist_time_no_defence = [196,332,514,787,983]
femnist_time_guardfl = [394,543,711, 831, 1078]

# Plotting the time for each dataset
plt.figure(figsize=(10, 6))

plt.plot(mnist_clients, mnist_time_no_defence, marker='o', linestyle='dotted', label='MNIST - No Defence',color = '#FF5733')
plt.plot(mnist_clients, mnist_time_guardfl, marker='o', linestyle='-', label='MNIST - GuardFL', color = '#FF5733')

plt.plot(cifar_clients, cifar_time_no_defence, marker='o', linestyle='dotted', label='CIFAR10 - No Defence', color = '#33FF57')
plt.plot(cifar_clients, cifar_time_guardfl, marker='o', linestyle='-', label='CIFAR10 - GuardFL' , color = '#33FF57')

plt.plot(femnist_clients, femnist_time_no_defence, marker='o', linestyle='dotted', label='FEMNIST - No Defence', color = '#3377FF')
plt.plot(femnist_clients, femnist_time_guardfl, marker='o', linestyle='-', label='FEMNIST - GuardFL', color = '#3377FF')
plt.xlabel('Number of Clients')
plt.ylabel('Time (sec)')
plt.title('Time vs Number of Clients for Different Datasets')
plt.legend()
plt.grid(True)
plt.xticks(np.arange(0, 21, 2))
plt.tight_layout()

plt.show()
plt.savefig('num_of_client_Time.png')