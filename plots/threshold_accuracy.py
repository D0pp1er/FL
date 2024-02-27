import matplotlib.pyplot as plt

# Data from the table
mnist_threshold_accuracy = [0.00125, 0.005, 0.01, 0.025, 0.03]
mnist_accuracy = [97.79, 97.69, 97.77, 97.75, 97.68]
mnist_loss = [732.82, 772.79, 731.64, 727.20, 761.25]
mnist_time = [795.33, 759.65, 830.66, 823.88, 791.82]

cifar10_threshold_accuracy = [0.00125, 0.005, 0.01, 0.025, 0.03]
cifar10_accuracy = [52.91, 54.30, 50.72, 40.45, 41.00]
cifar10_loss = [13092.65, 12833.09, 13590.82, 17211.53, 16692.79]
cifar10_time = [545.81, 544.72, 657.20, 685.04, 685.62]

femnist_threshold_accuracy = [0.00125, 0.005, 0.01, 0.025, 0.03]
femnist_accuracy = [85.30, 85.53, 85.25, 85.47, 85.30]
femnist_loss = [4119.65, 4099.86, 4199.04, 4102.08, 4170.79]
femnist_time = [788.17, 798.57, 824.53, 768.40, 801.87]

# Plotting
fig = plt.figure(figsize=(18, 5))

# Accuracy vs Threshold Accuracy
ax1 = fig.add_subplot(1, 3, 1)
ax1.plot(mnist_threshold_accuracy, mnist_accuracy, marker='o', label='MNIST')
ax1.plot(cifar10_threshold_accuracy, cifar10_accuracy, marker='o', label='CIFAR10')
ax1.plot(femnist_threshold_accuracy, femnist_accuracy, marker='o', label='FEMNIST')
ax1.set_xlabel('Threshold Accuracy')
ax1.set_ylabel('Accuracy (%)')
# ax1.set_title('Accuracy vs Threshold Accuracy')
ax1.text(0.5, -0.2, '(a) Accuracy vs Threshold Accuracy', ha='center', va='center', transform=ax1.transAxes)
ax1.legend()
ax1.grid(True)

# Loss vs Threshold Accuracy
ax2 = fig.add_subplot(1, 3, 2)
ax2.plot(mnist_threshold_accuracy, mnist_loss, marker='o', label='MNIST')
ax2.plot(cifar10_threshold_accuracy, cifar10_loss, marker='o', label='CIFAR10')
ax2.plot(femnist_threshold_accuracy, femnist_loss, marker='o', label='FEMNIST')
ax2.set_xlabel('Threshold Accuracy')
ax2.set_ylabel('Loss')
# ax2.set_title('Loss vs Threshold Accuracy')
ax2.text(0.5, -0.2, '(b) Loss vs Threshold Accuracy', ha='center', va='center', transform=ax2.transAxes)
ax2.legend()
ax2.grid(True)

# Time vs Threshold Accuracy
ax3 = fig.add_subplot(1, 3, 3)
ax3.plot(mnist_threshold_accuracy, mnist_time, marker='o', label='MNIST')
ax3.plot(cifar10_threshold_accuracy, cifar10_time, marker='o', label='CIFAR10')
ax3.plot(femnist_threshold_accuracy, femnist_time, marker='o', label='FEMNIST')
ax3.set_xlabel('Threshold Accuracy')
ax3.set_ylabel('Time (sec)')
# ax3.set_title('Time vs Threshold Accuracy')
ax3.text(0.5, -0.2, '(c) Time vs Threshold Accuracy', ha='center', va='center', transform=ax3.transAxes)
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.savefig('threshold_accuracy.png')
plt.show()