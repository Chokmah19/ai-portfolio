# 🧹 03｜文字前處理與資料準備



## 🧩 1. clean_text 函式設計邏輯

為了讓模型能正確學習文字資料，我們建立了一個 `clean_text(text)` 函式，分別處理輸入文字中的雜訊、格式與無意義詞，步驟如下。

---

### 步驟說明：

1. 🧽 **移除非文字字元**  
   使用正則表達式 `re.sub(r"[^\w\s]", "", text)`  
   ➜ 清除標點符號、emoji、特殊符號，只保留字母、數字與空格  

2. 🔡 **統一成小寫**  
   使用 `.lower()` 方法  
   ➜ 避免 "Love" 與 "love" 被模型視為不同詞  

3. ✂️ **分詞（tokenization）**  
   使用 `.split()`  
   ➜ 把句子切成單字組成的清單  

4. 🚫 **移除 stop words**  
   使用 `sklearn.feature_extraction.text.ENGLISH_STOP_WORDS`  
   ➜ 過濾掉常見但語意薄弱的詞（如 "the", "is", "and"）

---

## 🧪 clean_text 函式程式碼

```python
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

stop_words = ENGLISH_STOP_WORDS

def clean_text(text):
    cleaned = re.sub(r"[^\w\s]", "", text)
    lowercase = cleaned.lower()
    words = lowercase.split()
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words
```

### 🧠 我的疑問與學習紀錄

#### ❓我問：
- 「為什麼文字資料需要做前處理？」
- 「怎麼挑出重點詞彙？（怎麼決定哪些詞該保留）」
- 「list comprehension 是什麼？」
- 「為什麼不能直接讓模型吃文字，而要轉成數字？」
- 「為什麼轉 list ➜ string 要用 join，而不能用 df['col'].join('')？」

#### ✅ 我學到：
- 前處理可以統一格式、濾掉噪音詞、幫助模型更有效學習
- 可以用 sklearn 內建的 stop words 清單濾掉常見無意義詞
- list comprehension 是用一行簡潔的語法來過濾或轉換 list
- 模型只能做數學運算，所以必須把文字轉成數字向量（才能學習、運算）
- df['col'].join('') 錯是因為 .join() 只能用在單一 list，不是整個欄位 Series

#### 📎 附加備註
為了讓 CountVectorizer 處理文字，我們將每筆 token 清單轉成字串：

```python
df['clean_text'] = df['clean_tokens'].apply(lambda tokens: ' '.join(tokens))
```
- 我曾試著寫成 df['clean_tokens'].join('')，但錯誤原因是 .join() 要用在 list，不是 Series。

🔜 下一步
我接下來會使用 CountVectorizer 把 clean_text 欄位轉成模型可用的數字向量格式，並控制詞彙數量以避免過度擴張。


## 🧮 2. 詞彙向量化（使用 CountVectorizer）

文字經過清洗與斷詞後，無法直接提供給機器學習模型使用，必須進一步轉換為數值格式（向量）。這一段我們使用 `CountVectorizer` 將每筆評論轉換為「詞袋模型」的向量。

---

### 🧠 我的疑問與學習紀錄

#### ❓我問：
- 「為什麼不能直接讓模型吃文字？」
- 「向量化之後的資料每列每欄是什麼？」
- 「為什麼要限制詞彙表大小？」

#### ✅ 我學到：
- 模型只能做數學運算，無法理解文字本身
- 向量化後的每列是一筆評論，每欄是一個詞（特徵），值為出現次數
- 如果詞彙表太大（一開始超過 18 萬欄）會造成訓練過慢、過擬合，甚至包含噪音
- `max_features=10000` 可只保留常見前 10,000 個詞

---

### ✅ 重點程式碼

```python
from sklearn.feature_extraction.text import CountVectorizer

# 將斷詞後的清單轉為文字（給 Vectorizer 用）
df['clean_text'] = df['clean_tokens'].apply(lambda tokens: ' '.join(tokens))

# 建立向量器，限制最多 10,000 個詞彙
vectorizer = CountVectorizer(max_features=10000)
X = vectorizer.fit_transform(df['clean_text'])

print(X.shape)  # ➜ (50000, 10000)
```

## ℹ️ 3. 避免資料外洩（Data Leakage）

如果在切分資料集之前就用全部資料來 `fit` 向量器，測試集的詞彙資訊會提前被模型「偷看」，導致測試結果過於樂觀，這就是資料外洩。

---

### 🗒️ 正確流程

1. 先用 `train_test_split` 切成訓練集與測試集（同時切文字與標籤）。
2. 只在訓練集的文字上 `fit` 向量器。
3. 測試集只用向量器的 `transform` 方法轉換，不再重新 `fit`。

### ✅ 重點程式碼

```python
from sklearn.model_selection import train_test_split

X_text_train, X_text_test, y_train, y_test = train_test_split(
    df['clean_text'], df['label'],
    test_size=0.2, random_state=9, stratify=df['label']
)

cv = CountVectorizer(max_features=10000)
X_train = cv.fit_transform(X_text_train)
X_test  = cv.transform(X_text_test)
```

## ℹ️ 4. 保存處理後的資料（Artifacts）

為了方便後續模型訓練與部署，可以將向量器與切分後的資料存成檔案，下次直接載入使用。

---

### ✅ 重點程式碼

```python
import os, joblib
from scipy import sparse

os.makedirs("artifacts", exist_ok=True)
joblib.dump(cv, "artifacts/vectorizer.joblib")
sparse.save_npz("artifacts/X_train.npz", X_train)
sparse.save_npz("artifacts/X_test.npz",  X_test)
y_train.to_csv("artifacts/y_train.csv", index=False)
y_test.to_csv("artifacts/y_test.csv", index=False)
```

- 產出物：
    - `vectorizer.joblib`：已訓練好的向量器（詞表與轉換規則）
    - `X_train.npz`、`X_test.npz`：向量化後的特徵
    - `y_train.csv`、`y_test.csv`：對應的標籤

## ℹ️ 5. Baseline 模型結果（Logistic Regression）

- **Train Accuracy**: 0.9747
- **Test Accuracy**: 0.8664
- **Precision (0/1)**: 0.8671 / 0.8657
- **Recall (0/1)**: 0.8654 / 0.8674
- **F1-score (0/1)**: 0.8663 / 0.8665

> 結論：測試集表現達到 86.64%，指標平衡，略有過擬合但可接受，作為後續優化的基準。


## ✔️ 6. 驗收檢查清單

- ☑️clean_text 處理無缺值
- ☑️先切分資料再向量化
- ☑️stratify 保持標籤比例一致
- ☑️向量器只在訓練集 fit
- ☑️所有檔案已正確儲存到 artifacts/