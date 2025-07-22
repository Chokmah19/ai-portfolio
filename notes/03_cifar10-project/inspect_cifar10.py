# 1. 匯入套件
# 機器學習的核心運算框架
import torch           # 用來做張量運算、堆疊、統計
# 取得 CIFAR-10 資料集
from torchvision import datasets, transforms
# 統計資料時方便計數
from collections import Counter
# 繪圖工具，畫長條圖或其他圖形
import matplotlib.pyplot as plt
# 產生隨機數，用來抽樣或打亂順序
import random

transform = transforms.ToTensor()
train_data = datasets.CIFAR10(root='data/', train=True, download=True, transform=transform)

# 確認 train_data 存在
print("train_data type:", type(train_data))
print("樣本總數:", len(train_data))

#統計類別分佈
# Step 1：先準備一個空的 list，用來收集所有 label
labels = []

# Step 2：使用 for 迴圈，一筆一筆從 train_data 中取出 label
# 注意：train_data[i] 會回傳 (image, label) 兩個元素
for i in range(len(train_data)):
    img, label = train_data[i]      # 取出第 i 筆資料的影像和標籤
    labels.append(label)            # 把標籤放入 labels 清單中

# Step 3：從 collections 載入 Counter，統計每個 label 出現的次數
from collections import Counter
label_counts = Counter(labels)

# Step 4：印出結果，確認每個類別是否各有 5000 張訓練圖
print(label_counts)  # e.g. Counter({0: 5000, 1: 5000, ..., 9: 5000})


#計算像素統計量
# 讀取所有影像 tensor 並堆疊
# 做法：
# (1) 先從 train_data 中取出所有影像 tensor
# (2) 使用 torch.stack 合併成一個大 tensor

# Step 1. 用 list comprehension 讀取影像
#    train_data[i][0] 回傳第 i 筆資料的影像 tensor (C, H, W)
all_imgs_list = [train_data[i][0] for i in range(len(train_data))]

# Step 2. 用 torch.stack 在第 0 維度合併
#    結果維度為 (N, C, H, W)，N 為樣本數
all_imgs = torch.stack(all_imgs_list, dim=0)

# Step 3. 印出最小值與最大值，確保在 [0,1] 範圍內
print("Min, Max:", all_imgs.min().item(), all_imgs.max().item())

# Step 4. 計算每個顏色通道的平均值和標準差
#    dim=[0,2,3] 表示對樣本維度、長度維度、寬度維度做聚合
mean = all_imgs.mean(dim=[0,2,3])
std  = all_imgs.std(dim=[0,2,3])
print("Channel Means:", mean.tolist())
print("Channel Stds :", std.tolist())

#繪製長條圖
# Step 1. 確認 label_counts 是什麼型別
print(label_counts)
print(type(label_counts))

# Step 2. 將 counter 轉成兩個 list
# plt.bar(x, height) 要的：
# x：一維、可迭代（list/tuple/ndarray），代表每個 bar 的 x 座標（或分類名稱）。
# height：一維、可迭代，代表每個 bar 的高度。
xs = list(label_counts.keys())
ys = list(label_counts.values())
plt.bar(xs, ys)
plt.xticks(xs, rotation=45)   # 明確指定 x 刻度、並可旋轉
plt.xlabel("Class Index")
plt.ylabel("Number of Samples")
plt.title("CIFAR-10 Class Distribution")
plt.tight_layout()            # 類似排版微調
plt.show()