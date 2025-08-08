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

# 將每筆評論轉為向量（稀疏矩陣格式）
X = vectorizer.fit_transform(df['clean_text'])

print(X.shape)  # ➜ (50000, 10000)
