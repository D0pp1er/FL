import matplotlib.pyplot as plt

# Data for CIFAR-10
m_clients = [0, 2, 3, 5, 7]
cifar10_no_defence_acc = [55.49, 44.63, 40.01, 37.51, 22.34]
cifar10_guardfl_acc = [54.59, 52.11, 53.26, 53.88, 52.54]
cifar10_no_defence_loss = [12483.83, 15554.12, 16079.47, 17545.64, 20059.63]
cifar10_guardfl_loss = [12591.33, 13359.57, 13083.07, 12941.17, 13114.85]
cifar10_no_defence_time = [661.72, 573.15, 577.51, 512.01, 482.52]
cifar10_guardfl_time = [1053.86, 788.14, 749.63, 568.68, 542.68]

# Data for MNIST
mnist_no_defence_acc = [97.97, 95.95, 94.55, 91.46, 78.39]
mnist_guardfl_acc = [97.92, 97.74, 97.75, 97.80, 97.65]
mnist_no_defence_loss = [679.52, 1859.90, 2523.96, 6223.53, 12096.59]
mnist_guardfl_loss = [681.86, 751.13, 726.45, 721.53, 770.84]
mnist_no_defence_time = [843.88, 795.28, 835.99, 799.37, 823.9]
mnist_guardfl_time = [1067.96, 1002.09, 757.71, 814.27, 747.57]

# Data for FEMNIST
femnist_no_defence_acc = [85.74, 81.43, 78.19, 72.47, 69.08]
femnist_guardfl_acc = [85.61, 85.00, 85.03, 85.04, 85.19]
femnist_no_defence_loss = [4022.01, 5567.63, 6570.20, 8372.58, 11325.76]
femnist_guardfl_loss = [4053.84, 4223.59, 4253.22, 4232.12, 4139.91]
femnist_no_defence_time = [836.69, 819.94, 833.4, 815.63, 762.24]
femnist_guardfl_time = [1048.79, 1006.58, 1002.92, 763.57, 837.13]

# Plotting
plt.figure(figsize=(18, 5))

# Accuracy vs Malicious Client
ax1 = plt.subplot(1, 3, 1)
plt.plot(m_clients, cifar10_no_defence_acc, label='CIFAR-10 (No Defence)', marker='o', linestyle='dotted', color = '#FF5733')
plt.plot(m_clients, cifar10_guardfl_acc, label='CIFAR-10 (GuardFL)', marker='o', color = '#FF5733')
plt.plot(m_clients, mnist_no_defence_acc, label='MNIST (No Defence)', marker='o', linestyle='dotted', color = '#33FF57')
plt.plot(m_clients, mnist_guardfl_acc, label='MNIST (GuardFL)', marker='o', color = '#33FF57')
plt.plot(m_clients, femnist_no_defence_acc, label='FEMNIST (No Defence)', marker='o', linestyle='dotted', color = '#441199')
plt.plot(m_clients, femnist_guardfl_acc, label='FEMNIST (GuardFL)', marker='o', color = '#441199')
ax1.text(0.5, -0.2, '(a) Accuracy vs Malicious Client', ha='center', va='center', transform=ax1.transAxes)
plt.xlabel('Number of Malicious Clients')
plt.ylabel('Accuracy')
plt.legend()

# Loss vs Malicious Client
ax2 = plt.subplot(1, 3, 2)
plt.plot(m_clients, cifar10_no_defence_loss, label='CIFAR-10 (No Defence)', marker='o',linestyle='dotted', color = '#FF5733')
plt.plot(m_clients, cifar10_guardfl_loss, label='CIFAR-10 (GuardFL)', marker='o',color = '#FF5733')
plt.plot(m_clients, mnist_no_defence_loss, label='MNIST (No Defence)', marker='o',linestyle='dotted', color = '#33FF57')
plt.plot(m_clients, mnist_guardfl_loss, label='MNIST (GuardFL)', marker='o',color = '#33FF57')
plt.plot(m_clients, femnist_no_defence_loss, label='FEMNIST (No Defence)', marker='o',linestyle='dotted', color = '#441199')
plt.plot(m_clients, femnist_guardfl_loss, label='FEMNIST (GuardFL)', marker='o',color = '#441199')
ax2.text(0.5, -0.2, '(b) Loss vs Malicious Client', ha='center', va='center', transform=ax2.transAxes)
plt.xlabel('Number of Malicious Clients')
plt.ylabel('Loss')
plt.legend()

# Time vs Malicious Client
ax3 = plt.subplot(1, 3, 3)
plt.plot(m_clients, cifar10_no_defence_time, label='CIFAR-10 (No Defence)', marker='o', linestyle='dotted', color = '#FF5733')
plt.plot(m_clients, cifar10_guardfl_time, label='CIFAR-10 (GuardFL)', marker='o', color = '#FF5733')
plt.plot(m_clients, mnist_no_defence_time, label='MNIST (No Defence)', marker='o', linestyle='dotted', color = '#33FF57')
plt.plot(m_clients, mnist_guardfl_time, label='MNIST (GuardFL)', marker='o', color = '#33FF57')
plt.plot(m_clients, femnist_no_defence_time, label='FEMNIST (No Defence)', marker='o', linestyle='dotted', color = '#441199')
plt.plot(m_clients, femnist_guardfl_time, label='FEMNIST (GuardFL)', marker='o', color = '#441199')
ax3.text(0.5, -0.2, '(c) Time vs Malicious Client', ha='center', va='center', transform=ax3.transAxes)
plt.xlabel('Number of Malicious Clients')
plt.ylabel('Time (seconds)')
plt.legend()

plt.tight_layout()
plt.show()
plt.savefig('malicious_client.png')
