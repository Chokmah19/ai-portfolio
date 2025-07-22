# explore_cifar10.py

# 1. 匯入套件
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import random

# 2. 下載並轉換設定
transform = transforms.ToTensor()
train_data = datasets.CIFAR10(
    root='data/',
    train=True,
    download=False,
    transform=transform
)

# 3. 簡單檢查
print(f"樣本總數：{len(train_data)}")
print(f"類別清單：{train_data.classes}")

## 隨機顯示 CIFAR-10 樣本
# 4. 隨機顯示 8 張樣本圖片
fig, axes = plt.subplots(2, 4, figsize=(8, 4))
for ax in axes.flatten():
    idx = random.randint(0, len(train_data) - 1)   # 取得隨機索引
    img, lbl = train_data[idx]                     # 讀取影像與標籤
    ax.imshow(img.permute(1, 2, 0))                # 將 (C, H, W) 轉為 (H, W, C) 顯示
    ax.set_title(train_data.classes[lbl])          # 標題顯示類別名稱
    ax.axis('off')
plt.tight_layout()
plt.show()
