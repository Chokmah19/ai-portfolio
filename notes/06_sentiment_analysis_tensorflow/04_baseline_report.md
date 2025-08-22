# 04 — Baseline 模型報告（Logistic Regression, CountVectorizer）

## 1. 設定
- 向量化器：CountVectorizer（max_features=10,000）
- 模型：LogisticRegression（solver=liblinear, C=0.1, max_iter=1000）
- 資料切分：train/test = 80/20（stratify），**先切再 fit（避免資料外洩）**

## 2. 指標
- **Train Accuracy**：0.946325
- **Test  Accuracy**：0.8805


## 3. 為何選這組（與 8/13 的比較）
- **C=0.1 vs. C=1**  
  - 測試集準確率：由 **0.8664 提升到 0.8805**  
  - train-test gap：由 **10.8% 降到 6.6%**  
  → 過擬合情況減輕，泛化能力更好。

- **Count vs. TF-IDF**  
  - Count 的測試集準確率更高（**0.8805 vs. 0.8610**）  
  - TF-IDF 的 gap 較小（更穩定，但測試分數略低）  
  → 在這階段，我們優先保留 Count 版本。

## 4. 限制與風險
- 仍有輕微過擬合（train > test）
- 只用 unigram，可能忽略「否定 + 形容詞」等雙詞語境（例：not good）

## 5. 下一步
- **特徵**：嘗試 `ngram_range=(1,2)`、調整停用詞、設定最小詞頻
- **模型**：試 Linear SVM（文字分類常見強基線）
- **驗證**：以 Test Accuracy 與 F1 為主，目標 > 0.8805
