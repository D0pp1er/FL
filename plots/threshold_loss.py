import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = {
    'FEMNIST': {
        'Threshold Loss': [100, 300, 500, 700, 900],
        'Accuracy': [85.09, 85.16, 85.42, 85.13, 85.51],
        'Loss': [4200.16, 4191.28, 4116.85, 4192.22, 4101.01],
        'Time (sec)': [775.06, 771, 793.12, 799.38, 796.92]
    },
    'CIFAR10': {
        'Threshold Loss': [100, 300, 500, 700, 900],
        'Accuracy': [49.91, 54.55, 51.54, 52.37, 50.47],
        'Loss': [13791.58, 12757.58, 13494.62, 13137.00, 13657.09],
        'Time (sec)': [630.72, 543.96, 589.91, 592.31, 644.38]
    },
    'MNIST': {
        'Threshold Loss': [100, 300, 500, 700, 900],
        'Accuracy': [97.75, 97.80, 97.79, 97.73, 97.74],
        'Loss': [741.19, 738.20, 724.44, 756.01, 741.37],
        'Time (sec)': [861.00, 761.73, 815.00, 791.28, 786.92]
    }
}

# # Plotting accuracy vs threshold loss
# plt.figure(figsize=(10, 6))
# for dataset, values in data.items():
#     plt.plot(values['Threshold Loss'], values['Accuracy'], marker='o', label=dataset)
# plt.xlabel('Threshold Loss')
# plt.ylabel('Accuracy')
# plt.title('Accuracy vs Threshold Loss')
# plt.legend()
# plt.grid(True)
# plt.show()
# plt.savefig('threshold_loss_Accuracy.png')

# # Plotting loss vs threshold loss
# plt.figure(figsize=(10, 6))
# for dataset, values in data.items():
#     plt.plot(values['Threshold Loss'], values['Loss'], marker='o', label=dataset)
# plt.xlabel('Threshold Loss')
# plt.ylabel('Loss')
# plt.title('Loss vs Threshold Loss')
# plt.legend()
# plt.grid(True)
# plt.show()
# plt.savefig('threshold_loss_Loss.png')

# # Plotting time vs threshold loss
# plt.figure(figsize=(10, 6))
# for dataset, values in data.items():
#     plt.plot(values['Threshold Loss'], values['Time (sec)'], marker='o', label=dataset)
# plt.xlabel('Threshold Loss')
# plt.ylabel('Time (sec)')
# plt.title('Time vs Threshold Loss')
# plt.legend()
# plt.grid(True)
# plt.show()
# plt.savefig('threshold_loss_Time.png')
# Plotting
fig = plt.figure(figsize=(18, 5))

# Accuracy vs Threshold Loss
ax1 = fig.add_subplot(1, 3, 1)
for dataset, values in data.items():
    ax1.plot(values['Threshold Loss'], values['Accuracy'], marker='o', label=dataset)
ax1.set_xlabel('Threshold Loss')
ax1.set_ylabel('Accuracy')
ax1.legend()
ax1.grid(True)
# fig.text(0.5/3, 0, 'Accuracy vs Threshold Loss', ha='center', va='center')
ax1.text(0.5, -0.2, '(a) Accuracy vs Threshold Loss', ha='center', va='center', transform=ax1.transAxes)

# Loss vs Threshold Loss
ax2 = fig.add_subplot(1, 3, 2)
for dataset, values in data.items():
    ax2.plot(values['Threshold Loss'], values['Loss'], marker='o', label=dataset)
ax2.set_xlabel('Threshold Loss')
ax2.set_ylabel('Loss')
ax2.legend()
ax2.grid(True)
# fig.text(1.5/3, 0, 'Loss vs Threshold Loss', ha='center', va='center')
ax2.text(0.5, -0.2, '(b) Loss vs Threshold Loss', ha='center', va='center', transform=ax2.transAxes)

# Time vs Threshold Loss
ax3 = fig.add_subplot(1, 3, 3)
for dataset, values in data.items():
    ax3.plot(values['Threshold Loss'], values['Time (sec)'], marker='o', label=dataset)
ax3.set_xlabel('Threshold Loss')
ax3.set_ylabel('Time (sec)')
ax3.legend()
ax3.grid(True)
# fig.text(2.5/3, 0, 'Time vs Threshold Loss', ha='center', va='center')
ax3.text(0.5, -0.2, '(c) Time vs Threshold Loss', ha='center', va='center', transform=ax3.transAxes)

plt.tight_layout()
plt.savefig('threshold_loss.png')
plt.show()
