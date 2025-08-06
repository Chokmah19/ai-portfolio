# 模型架構草圖（Model Design）

本檔案說明本專案的主要模型架構與元件設計，採用簡潔、模組化的方式呈現，方便後續逐步開發與測試。架構以 LSTM 為主，搭配詞向量嵌入（Embedding Layer），後續可依進度再進一步優化或替換為 BERT。

---

## 📌 模型流程概觀

以下為簡化的模型處理流程：
```
輸入文字（單筆或多筆）
↓
文本前處理（清洗、分詞、去除停用詞）
↓
詞嵌入（Embedding Layer：Word2Vec / GloVe / TensorFlow 內建）
↓
LSTM 模型（或後續改為 Transformer）
↓
Dense 層輸出分類結果（正向 / 負向）＋ 信心分數
```
---

## 🧩 模組說明表格

| 模組名稱           | 功能簡述 |
|--------------------|----------|
| 📥 輸入層（Input） | 接收單筆輸入文字或上傳的文字檔（CSV / TXT） |
| 🧹 文本前處理       | 分詞、轉小寫、去除符號與停用詞等清洗動作 |
| 🧠 詞嵌入（Embedding）| 將每個詞轉為向量，讓模型能理解語意。使用 TensorFlow 內建 Embedding 層，後續可換 Word2Vec/GloVe |
| 🔁 LSTM 模型        | 利用循環神經網路學習詞序與情緒模式（雙向 LSTM 可選） |
| 🎯 輸出層（Output） | 輸出二分類結果：正向／負向，並顯示信心分數（例如 87%） |

---

## ⚙️ 模型結構預計草圖（簡化版）

以下是預計使用的 Keras 模型結構（文字示意，程式會在 `04_model_building.ipynb` 撰寫）：

```python
model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=128, input_length=MAX_LEN))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))

---

## 🧩 模組說明表格

| 模組名稱           | 功能簡述 |
|--------------------|----------|
| 📥 輸入層（Input） | 接收單筆輸入文字或上傳的文字檔（CSV / TXT） |
| 🧹 文本前處理       | 分詞、轉小寫、去除符號與停用詞等清洗動作 |
| 🧠 詞嵌入（Embedding）| 將每個詞轉為向量，讓模型能理解語意。使用 TensorFlow 內建 Embedding 層，後續可換 Word2Vec/GloVe |
| 🔁 LSTM 模型        | 利用循環神經網路學習詞序與情緒模式（雙向 LSTM 可選） |
| 🎯 輸出層（Output） | 輸出二分類結果：正向／負向，並顯示信心分數（例如 87%） |

---

## ⚙️ 模型結構預計草圖（簡化版）

以下是預計使用的 Keras 模型結構（文字示意，程式會在 `04_model_building.ipynb` 撰寫）：

```python
model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=128, input_length=MAX_LEN))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))

- input_dim=10000: 詞彙表大小
- output_dim=128: 向量維度（詞嵌入後的維度）
- input_length: 單句長度上限（MAX_LEN）
- LSTM(64): LSTM 隱藏層維度
- Dense(1, activation='sigmoid'): 輸出為一個數值（機率）
