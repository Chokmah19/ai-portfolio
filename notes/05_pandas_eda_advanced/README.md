# 🔍 Advanced Pandas EDA

## 🎯 學習目標
- 練習多重聚合與自訂函式  
- 探索時間序列資料（重採樣、移動平均）  
- 熟悉交叉表／樞紐分析  
- 為後續視覺化做好資料準備  

## 💡 學習概念
- **GroupBy 深入**  
    - 多重聚合 (.agg())  
    - 自訂聚合函式（lambda 或定義 function）  
- **時間序列操作**  
    - pd.to_datetime()
    - resample()
    - rolling() 移動平均  
- **交叉表 & Pivot Table**  
    - pd.pivot_table() 
    - 線上或離線統計檢定前的資料整理

## 📌 步驟紀錄

1. 資料預覽與檢查
2. GroupBy 多重聚合
3. pivot_table 樞紐分析
4. 時間序列重取樣與移動平均

## 🧠 心得筆記
- 在練習Pandas的時候，除了可在本機 Jupyter Notebook 練習，也能在 Kaggle Notebook，按需求選擇，個人是在本機練習，然後發現 VS Code有套件(seaborn)內建 titanic 資料集，可以節省我下載再匯入的時間，方便很多，因此記錄下來
    - pip install seaborn > 安裝語法


## ✅ 實作成果
- 分組後同時做多種統計（如均值、中位數、標準差）
- 使用 pivot_table 對類別與數值欄位做快速交叉分析