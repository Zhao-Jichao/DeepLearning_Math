# 目标函数：Loss = W1**2 + W2**2
# 梯度偏导：ParDer_W1 = 2*W1，ParDer_W2 = 2*W2
# 初始值：W1 = 2，W2 = 3
# Loss = W1**2 + W2**2

learning_rate = 0.1

W1 = 3
W2 = 2

for i in range(10):
    # 求取梯度
    ParDer_W1 = 2*W1
    ParDer_W2 = 2*W2
    # 学习
    W1 = W1 - learning_rate*ParDer_W1
    W2 = W2 - learning_rate*ParDer_W2
    # 计算损失函数
    Loss = W1**2 + W2**2
    # 显示计算结果
    print("W1: ", W1)
    print("W2: ", W2)
    print("Loss: ", Loss)
    print("i: ", i+1)

