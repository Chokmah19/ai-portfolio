# 🔍 資料管線處理 & 資料前處理：清理與標準化

## 🎯 學習目標
- 熟悉從原始資料到清理後資料的整個流程
- 撰寫可重複使用的預處理函式庫

## 💡 學習概念
- 資料管線（Pipeline）：了解何謂資料管線、如何用函式或類別串起各步驟
    - 資料管線（Pipeline）其實就是一組「有順序、可以重複使用」的資料處理步驟集合。結構化流程，並且具可維護性、可複現性。
- 缺值處理 & 標準化：dropna() vs. fillna()、Z‑score／Min‑Max scaling
- 程式碼模組化：封裝清理與轉換步驟成函式／模組

## 📌 步驟紀錄

1. 多欄位缺值填補(在此實作使用平均值填補)
2. 標準化
   1. Fit > 指定要標準化的欄位清單
   2. Transform > 原始值減去平均，再除以標準差，每個欄位就會變成平均 0、標準差 1 的分佈
   3. 建立一個小類別 MyScaler
3. 整合到preprocessing.py

## 🧠 心得筆記
- 缺值填補必須在標準化之前，不然NaN會讓平均值與標準差的計算出現問題
    - 測試資料不乾淨，或是舊版程式沒被載入都可能導致標準差!=1，實作中有遇到相同狀況，花了很多時間除錯跟加入檢查機制
- Pandas 的 .std() 預設是 **樣本標準差（ddof=1）**
- 每次改 preprocessing.py 後，最好都要重啟 Kernel，確保 Notebook 拿到最新程式碼。

## ✅ 實作成果
- 資料管線：以 sklearn.pipeline.Pipeline 為參考，手動實作簡易版
- 清理步驟：示範對多欄位同時填補，並用 StandardScaler 做標準化
- 整合程式碼：最後整理成 preprocessing.py，並在 Jupyter notebook (data_pipeline_and_preprocessing.ipynb) 測試