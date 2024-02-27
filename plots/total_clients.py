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

# # Plotting the accuracy for each dataset
# plt.figure(figsize=(10, 6))

# plt.plot(mnist_clients, mnist_acc_no_defence, marker='o', linestyle='dotted', label='MNIST - No Defence', color = '#FF5733' )
# plt.plot(mnist_clients, mnist_acc_guardfl, marker='o', linestyle='-', label='MNIST - GuardFL', color = '#FF5733')

# plt.plot(cifar_clients, cifar_acc_no_defence, marker='o', linestyle='dotted', label='CIFAR10 - No Defence' , color = '#33FF57')
# plt.plot(cifar_clients, cifar_acc_guardfl, marker='o', linestyle='-', label='CIFAR10 - GuardFL' , color = '#33FF57')

# plt.plot(femnist_clients, femnist_acc_guardfl, marker='o', linestyle='-', label='FEMNIST - GuardFL' , color = '#5733FF')
# plt.plot(femnist_clients, femnist_acc_no_defence, marker='o', linestyle='dotted', label='FEMNIST - No Defence' , color = '#5733FF')

# plt.xlabel('Number of Clients')
# plt.ylabel('Accuracy (%)')
# plt.title('Accuracy vs Number of Clients for Different Datasets')
# plt.legend()
# plt.grid(True)
# plt.xticks(np.arange(0, 21, 2))
# plt.ylim(0, 100)
# plt.tight_layout()

# plt.show()
# plt.savefig('num_of_client_Accuracy.png')
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



# Data for MNIST dataset
mnist_clients = [4, 8, 12, 16, 20]
mnist_loss_no_defence = [21654.68, 21204.41, 21631.60, 20784.74, 21469.05]
mnist_loss_guardfl = [755.90, 745.75, 716.75, 724.20, 753.06]

# Data for CIFAR10 dataset
cifar_clients = [4, 8, 12, 16, 20]
cifar_loss_no_defence = [5402261, 5297439, 7501376, 4704870, 6377244]
cifar_loss_guardfl = [13169, 13024, 13288, 12676, 13461]

femnist_clients = [4, 8, 12, 16, 20]
femnist_loss_no_defence = [17115.91,14589.6,18252.17,16408.20,17068.91]
femnist_loss_guardfl = [4209.86,4287.48,4181.36,4167.67 ,4307.84]

# # Plotting the loss for each dataset
# plt.figure(figsize=(10, 6))

# plt.plot(mnist_clients, mnist_loss_no_defence, marker='o', linestyle='dotted', label='MNIST - No Defence', color = '#FF5733')
# plt.plot(mnist_clients, mnist_loss_guardfl, marker='o', linestyle='-', label='MNIST - GuardFL', color = '#FF5733')

# # plt.plot(cifar_clients, cifar_loss_no_defence, marker='o', linestyle='dotted', label='CIFAR10 - No Defence', color = '#33FF57')
# # plt.plot(cifar_clients, cifar_loss_guardfl, marker='o', linestyle='-', label='CIFAR10 - GuardFL', color = '#33FF57')

# plt.plot(femnist_clients, femnist_loss_no_defence, marker='o', linestyle='dotted', label='FEMNIST - No Defence', color = '#3377FF')
# plt.plot(femnist_clients, femnist_loss_guardfl, marker='o', linestyle='-', label='FEMNIST - GuardFL', color = '#3377FF')

# plt.xlabel('Number of Clients')
# plt.ylabel('Loss')
# plt.title('Loss vs Number of Clients for MNIST & FEMNIST')
# plt.legend()
# plt.grid(True)
# plt.xticks(np.arange(0, 21, 2))
# plt.tight_layout()

# plt.savefig('num_of_client_Loss.png')
# plt.show()

# plt.figure(figsize=(10, 6))
# plt.plot(cifar_clients, cifar_loss_no_defence, marker='o', linestyle='dotted', label='CIFAR10 - No Defence', color = '#33FF57')
# plt.plot(cifar_clients, cifar_loss_guardfl, marker='o', linestyle='-', label='CIFAR10 - GuardFL', color = '#33FF57')
# plt.xlabel('Number of Clients')
# plt.ylabel('Loss')
# plt.title('Loss vs Number of Clients for CIFAR10')
# plt.legend()
# plt.grid(True)
# plt.xticks(np.arange(0, 21, 2))
# plt.tight_layout()
# plt.show()
# plt.savefig('num_of_client_Loss_CIFAR10.png')


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

# # Plotting the time for each dataset
# plt.figure(figsize=(10, 6))

# plt.plot(mnist_clients, mnist_time_no_defence, marker='o', linestyle='dotted', label='MNIST - No Defence',color = '#FF5733')
# plt.plot(mnist_clients, mnist_time_guardfl, marker='o', linestyle='-', label='MNIST - GuardFL', color = '#FF5733')

# plt.plot(cifar_clients, cifar_time_no_defence, marker='o', linestyle='dotted', label='CIFAR10 - No Defence', color = '#33FF57')
# plt.plot(cifar_clients, cifar_time_guardfl, marker='o', linestyle='-', label='CIFAR10 - GuardFL' , color = '#33FF57')

# plt.plot(femnist_clients, femnist_time_no_defence, marker='o', linestyle='dotted', label='FEMNIST - No Defence', color = '#3377FF')
# plt.plot(femnist_clients, femnist_time_guardfl, marker='o', linestyle='-', label='FEMNIST - GuardFL', color = '#3377FF')
# plt.xlabel('Number of Clients')
# plt.ylabel('Time (sec)')
# plt.title('Time vs Number of Clients for Different Datasets')
# plt.legend()
# plt.grid(True)
# plt.xticks(np.arange(0, 21, 2))
# plt.tight_layout()

# plt.show()
# plt.savefig('num_of_client_Time.png')


fig, axs = plt.subplots(1, 4, figsize=(24, 6))  # 1 row, 4 columns

# Plotting the accuracy for each dataset
axs[0].plot(mnist_clients, mnist_acc_no_defence, marker='o', linestyle='dotted', label='MNIST - No Defence', color = '#FF5733' )
axs[0].plot(mnist_clients, mnist_acc_guardfl, marker='o', linestyle='-', label='MNIST - GuardFL', color = '#FF5733')
axs[0].plot(cifar_clients, cifar_acc_no_defence, marker='o', linestyle='dotted', label='CIFAR10 - No Defence' , color = '#33FF57')
axs[0].plot(cifar_clients, cifar_acc_guardfl, marker='o', linestyle='-', label='CIFAR10 - GuardFL' , color = '#33FF57')
axs[0].plot(femnist_clients, femnist_acc_guardfl, marker='o', linestyle='-', label='FEMNIST - GuardFL' , color = '#5733FF')
axs[0].plot(femnist_clients, femnist_acc_no_defence, marker='o', linestyle='dotted', label='FEMNIST - No Defence' , color = '#5733FF')
axs[0].set_xlabel('Number of Clients')
axs[0].set_ylabel('Accuracy (%)')
# axs[0].set_title('Accuracy vs Number of Clients for Different Datasets')
axs[0].text(0.5, -0.2, '(a) Accuracy vs Number of Clients', ha='center', va='center', transform=axs[0].transAxes)
axs[0].legend()
axs[0].grid(True)
axs[0].set_xticks(np.arange(0, 21, 2))
axs[0].set_ylim(0, 100)

# Plotting the loss for each dataset
axs[1].plot(mnist_clients, mnist_loss_no_defence, marker='o', linestyle='dotted', label='MNIST - No Defence', color = '#FF5733')
axs[1].plot(mnist_clients, mnist_loss_guardfl, marker='o', linestyle='-', label='MNIST - GuardFL', color = '#FF5733')
axs[1].plot(femnist_clients, femnist_loss_no_defence, marker='o', linestyle='dotted', label='FEMNIST - No Defence', color = '#3377FF')
axs[1].plot(femnist_clients, femnist_loss_guardfl, marker='o', linestyle='-', label='FEMNIST - GuardFL', color = '#3377FF')
axs[1].set_xlabel('Number of Clients')
axs[1].set_ylabel('Loss')
# axs[1].set_title('Loss vs Number of Clients for MNIST & FEMNIST')
axs[1].text(0.5, -0.2, '(b) Loss vs Number of Clients', ha='center', va='center', transform=axs[1].transAxes)
axs[1].legend()
axs[1].grid(True)
axs[1].set_xticks(np.arange(0, 21, 2))

# Plotting the loss for CIFAR10 dataset
axs[2].plot(cifar_clients, cifar_loss_no_defence, marker='o', linestyle='dotted', label='CIFAR10 - No Defence', color = '#33FF57')
axs[2].plot(cifar_clients, cifar_loss_guardfl, marker='o', linestyle='-', label='CIFAR10 - GuardFL', color = '#33FF57')
axs[2].set_xlabel('Number of Clients')
axs[2].set_ylabel('Loss')
# axs[2].set_title('Loss vs Number of Clients for CIFAR10')
axs[2].text(0.5, -0.2, '(c) Loss vs Number of Clients', ha='center', va='center', transform=axs[2].transAxes)
axs[2].legend()
axs[2].grid(True)
axs[2].set_xticks(np.arange(0, 21, 2))

# Plotting the time for each dataset
axs[3].plot(mnist_clients, mnist_time_no_defence, marker='o', linestyle='dotted', label='MNIST - No Defence',color = '#FF5733')
axs[3].plot(mnist_clients, mnist_time_guardfl, marker='o', linestyle='-', label='MNIST - GuardFL', color = '#FF5733')
axs[3].plot(cifar_clients, cifar_time_no_defence, marker='o', linestyle='dotted', label='CIFAR10 - No Defence', color = '#33FF57')
axs[3].plot(cifar_clients, cifar_time_guardfl, marker='o', linestyle='-', label='CIFAR10 - GuardFL' , color = '#33FF57')
axs[3].plot(femnist_clients, femnist_time_no_defence, marker='o', linestyle='dotted', label='FEMNIST - No Defence', color = '#3377FF')
axs[3].plot(femnist_clients, femnist_time_guardfl, marker='o', linestyle='-', label='FEMNIST - GuardFL', color = '#3377FF')
axs[3].set_xlabel('Number of Clients')
axs[3].set_ylabel('Time (sec)')
# axs[3].set_title('Time vs Number of Clients for Different Datasets')
axs[3].text(0.5, -0.2, '(d) Time vs Number of Clients', ha='center', va='center', transform=axs[3].transAxes)
axs[3].legend()
axs[3].grid(True)
axs[3].set_xticks(np.arange(0, 21, 2))

plt.tight_layout()
plt.show()
plt.savefig('num_of_client.png')