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

# Plot accuracy vs threshold accuracy
plt.figure(figsize=(10, 6))
plt.plot(mnist_threshold_accuracy, mnist_accuracy, marker='o', label='MNIST')
plt.plot(cifar10_threshold_accuracy, cifar10_accuracy, marker='o', label='CIFAR10')
plt.plot(femnist_threshold_accuracy, femnist_accuracy, marker='o', label='FEMNIST')
plt.xlabel('Threshold Accuracy')
plt.ylabel('Accuracy (%)')
plt.title('Accuracy vs Threshold Accuracy')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('threshold_accuracy_accuracy.png')

# Plot loss vs threshold accuracy
plt.figure(figsize=(10, 6))
plt.plot(mnist_threshold_accuracy, mnist_loss, marker='o', label='MNIST')
plt.plot(cifar10_threshold_accuracy, cifar10_loss, marker='o', label='CIFAR10')
plt.plot(femnist_threshold_accuracy, femnist_loss, marker='o', label='FEMNIST')
plt.xlabel('Threshold Accuracy')
plt.ylabel('Loss')
plt.title('Loss vs Threshold Accuracy')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('threshold_accuracy_loss.png')

# Plot time vs threshold accuracy
plt.figure(figsize=(10, 6))
plt.plot(mnist_threshold_accuracy, mnist_time, marker='o', label='MNIST')
plt.plot(cifar10_threshold_accuracy, cifar10_time, marker='o', label='CIFAR10')
plt.plot(femnist_threshold_accuracy, femnist_time, marker='o', label='FEMNIST')
plt.xlabel('Threshold Accuracy')
plt.ylabel('Time (sec)')
plt.title('Time vs Threshold Accuracy')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('threshold_accuracy_time.png')
