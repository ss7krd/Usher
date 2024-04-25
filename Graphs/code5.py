# Import libraries
import matplotlib
import numpy as np
import random
import matplotlib.pyplot as plt
# import numpy as np
# extra for mac
matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 48})

fig = plt.figure()
ax = fig.add_subplot(111)

# Creating dataset
np.random.seed(10)

#list of prev values:
# (205, 210, 10)(229, 237, 10)
# (253, 256, 10)(283, 288, 10)
# (52, 56, 10)(58, 60, 10)
# (180, 184, 10)(192, 194, 10)
# (135, 139, 10)(144, 146, 10)
# (100, 102, 10)(107, 111, 10)#baad
# (205, 210, 10)(219, 225, 10)
# (253, 256, 10)(270, 276, 10)
# (52, 56, 10)(56, 62, 10)
# (180, 184, 10)(187, 189, 10)
# (135, 139, 10)(140, 142, 10)
# (100, 102, 10)(104, 108, 10)#baad
# previous grouping: (LSTM, GRU, BN); (Conv1D, Conv2D, Conv3D)

# data_1 = np.random.normal(100, 10, 200)
data_1 = np.random.uniform(135, 139, 10)
# data_2 = np.random.normal(90, 20, 200)
data_2 = np.random.uniform(140, 142, 10)
# data_3 = np.random.normal(80, 30, 200)
# data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2]
 
# fig = plt.figure(figsize =(10, 7))
 
# Creating axes instance
# ax = fig.add_axes([0, 0, 1, 1])
ax.set_ylabel("Per-batch latency\n(micro second)")
ax.set_xlabel("Operators")
ax.set_xticklabels(["GEMM", "GEMM+conv3D"])
# Creating plot
ax.boxplot(data)

box = ax.get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax.set_position([box.x0 + box.width*0.05, box.y0 + box.height*0.05, box.width, box.height*0.6])

# show plot
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

plt.show()