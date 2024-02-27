# import matplotlib.pyplot as plt
# import numpy as np

# # Data for MNIST dataset
# mnist_clients = [4, 8, 12, 16, 20]
# mnist_loss_no_defence = [21654.68, 21204.41, 21631.60, 20784.74, 21469.05]
# mnist_loss_guardfl = [755.90, 745.75, 716.75, 724.20, 753.06]

# # Data for CIFAR10 dataset
# cifar_clients = [4, 8, 12, 16, 20]
# cifar_loss_no_defence = [5402261, 5297439, 7501376, 4704870, 6377244]
# cifar_loss_guardfl = [13169, 13024, 13288, 12676, 13461]

# # Plotting the loss for each dataset
# plt.figure(figsize=(10, 6))

# plt.plot(mnist_clients, mnist_loss_no_defence, marker='o', linestyle='dotted', label='MNIST - No Defence', color = '#FF5733')
# plt.plot(mnist_clients, mnist_loss_guardfl, marker='o', linestyle='-', label='MNIST - GuardFL', color = '#FF5733')

# plt.plot(cifar_clients, cifar_loss_no_defence, marker='o', linestyle='dotted', label='CIFAR10 - No Defence', color = '#33FF57')
# plt.plot(cifar_clients, cifar_loss_guardfl, marker='o', linestyle='-', label='CIFAR10 - GuardFL', color = '#33FF57')

# plt.xlabel('Number of Clients')
# plt.ylabel('Loss')
# plt.title('Loss vs Number of Clients for Different Datasets')
# plt.legend()
# plt.grid(True)
# plt.xticks(np.arange(0, 21, 2))
# plt.tight_layout()

# plt.show()
# plt.savefig('Loss.png')

import matplotlib.pyplot as plt
import numpy as np

# Data for MNIST dataset
mnist_clients = [4, 8, 12, 16, 20]
mnist_loss_no_defence = [21654.68, 21204.41, 21631.60, 20784.74, 21469.05]
mnist_loss_guardfl = [755.90, 745.75, 716.75, 724.20, 753.06]

# Data for CIFAR10 dataset
cifar_clients = [4, 8, 12, 16, 20]
cifar_loss_no_defence = [5402261, 5297439, 7501376, 4704870, 6377244]
cifar_loss_guardfl = [13169, 13024, 13288, 12676, 13461]

# Plotting the loss for each dataset
plt.figure(figsize=(10, 6))

plt.plot(mnist_clients, mnist_loss_no_defence, marker='o', linestyle='dotted', label='MNIST - No Defence', color = '#FF5733')
plt.plot(mnist_clients, mnist_loss_guardfl, marker='o', linestyle='-', label='MNIST - GuardFL', color = '#FF5733')

plt.plot(cifar_clients, cifar_loss_no_defence, marker='o', linestyle='dotted', label='CIFAR10 - No Defence', color = '#33FF57')
plt.plot(cifar_clients, cifar_loss_guardfl, marker='o', linestyle='-', label='CIFAR10 - GuardFL', color = '#33FF57')

plt.xlabel('Number of Clients')
plt.ylabel('Loss')
plt.title('Loss vs Number of Clients for Different Datasets')
plt.legend()
plt.grid(True)
plt.xticks(np.arange(0, 21, 2))
plt.tight_layout()

plt.savefig('num_of_client_Loss.png')
plt.show()