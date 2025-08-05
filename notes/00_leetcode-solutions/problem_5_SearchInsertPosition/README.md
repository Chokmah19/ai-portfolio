## Problem_5_SearchInsertPosition

## 🎯題目描述

- 給定一個**升序排列的整數陣列** nums ，和一個目標數字 target ，請找出目標值應該插入的位置，使得陣列仍然保持排序。
    - 如果 target 在陣列中，回傳它的索引位置
    - 如果不在，回傳它**應該插入的位置**

## 🧠解題思路

- 解法：**二分搜尋法**（Binary Search）變形，重點如下：
    - 如何設定搜尋範圍
    - 何時調整邊界
    - 找不到時應該插入哪裡  

🔧 初始邊界設定：
```python
left = 0
right = len(nums) - 1
```
🔄 搜尋邏輯：
- 每次取中間索引：mid = (left + right) // 2
- 比較 nums[mid] 和 target：
    - 相等：直接回傳 mid
    - target 比 nums[mid] 小 → 搜左邊：right = mid - 1
    - target 比 nums[mid] 大 → 搜右邊：left = mid + 1
- 若整個迴圈結束還找不到，目標值應該插入在 left 的位置
    - 為什麼回傳 left 而不是 right？ → 因為 left 最終會停在第一個「大於等於 target」的位置，就是要插入的位置。  
 
## 🗒️心得
   首次實作「二分搜尋法」的整體流程，也透過提問理解了以下觀念：
- left / right 的初始化邏輯
    - left = 0 → 代表目前搜尋的**左邊界**是從陣列的最左邊開始，也就是 index 0。
    - right = len(nums) - 1 → 設定**右邊界**為陣列的最後一個 index。
- 為什麼用 left <= right 作為 while 條件 → **確保所有可能的元素都被檢查到**，包含最後那個
- 為什麼最後回傳 left 才是插入位置 → 因為 left 最終會停在第一個「>= target」的位置，也就是插入點

   
