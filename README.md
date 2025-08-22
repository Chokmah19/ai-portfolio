# ai-portfolio
My AI Exercise Portfolio

> Last updated: 2025-08-14 · 排序依 repo 結構：**01 → 02 → 03 → …**

本 README 按資料夾編號排序，每個主題列出實際檔案連結與簡短描述，方便快速找到對應內容。

---

## 🎓 Coursework

### 01_Google_ai_note
- [README.md](./notes/01_Google_ai_note/README.md) — Google AI Essentials / Prompting Essentials 課程重點整理。

---

## 🧩 Practice

### 00_leetcode-solutions
- [README.md](./notes/00_leetcode-solutions/README.md) — LeetCode 解題紀錄總覽。
- 題目解答：
  - [problem_1_TwoSum README](./notes/00_leetcode-solutions/problem_1_TwoSum/README.md) ｜ [solution.py](./notes/00_leetcode-solutions/problem_1_TwoSum/solution.py)
  - [problem_2_PalindromeNumber README](./notes/00_leetcode-solutions/problem_2_PalindromeNumber/README.md) ｜ [solution.py](./notes/00_leetcode-solutions/problem_2_PalindromeNumber/solution.py)
  - [problem_3_RomanToInteger README](./notes/00_leetcode-solutions/problem_3_RomanToInteger/README.md) ｜ [solution.py](./notes/00_leetcode-solutions/problem_3_RomanToInteger/solution.py)
  - [problem_4_AddBinary README](./notes/00_leetcode-solutions/problem_4_AddBinary/README.md) ｜ [solution.py](./notes/00_leetcode-solutions/problem_4_AddBinary/solution.py)
  - [problem_5_SearchInsertPosition README](./notes/00_leetcode-solutions/problem_5_SearchInsertPosition/README.md) ｜ [solution.py](./notes/00_leetcode-solutions/problem_5_SearchInsertPosition/solution.py)

  ### 02_kaggle-pandas-practice
- [Kaggle_Pandas_Practice.ipynb](./notes/02_kaggle-pandas-practice/Kaggle_Pandas_Practice.ipynb) — Kaggle Pandas API 練習。
- [README.md](./notes/02_kaggle-pandas-practice/README.md) — 練習說明與重點。

---

## 🗒 Notes

### 03_cifar10-project
- [2025-07-10-explore.md](./notes/03_cifar10-project/2025-07-10-explore.md) — 資料下載與探索。
- [2025-07-11-inspect.md](./notes/03_cifar10-project/2025-07-11-inspect.md) — 基本資料檢視。
- [explore_cifar10.py](./notes/03_cifar10-project/explore_cifar10.py) ｜ [inspect_cifar10.py](./notes/03_cifar10-project/inspect_cifar10.py) — 輔助腳本。

### 04_data_pipeline_and_preprocessing
- [README.md](./notes/04_data_pipeline_and_preprocessing/README.md) — 資料處理管線概觀。
- [data_pipeline_and_preprocessing.ipynb](./notes/04_data_pipeline_and_preprocessing/data_pipeline_and_preprocessing.ipynb) — 清理與特徵工程示例。
- [preprocessing.py](./notes/04_data_pipeline_and_preprocessing/preprocessing.py) — 可重用前處理模組。

### 05_pandas_eda_advanced
- [README.md](./notes/05_pandas_eda_advanced/README.md) — 進階 EDA 筆記說明。
- [pandas_eda_advanced.ipynb](./notes/05_pandas_eda_advanced/pandas_eda_advanced.ipynb) — 教學 Notebook。
- [flights.csv](./notes/05_pandas_eda_advanced/flights.csv) ｜ [titanic.csv](./notes/05_pandas_eda_advanced/titanic.csv) — 範例資料。

---

## 🔭 Projects

### 06_sentiment_analysis_tensorflow（Ongoing）
- [01_project_plan.md](./notes/06_sentiment_analysis_tensorflow/01_project_plan.md) — 專案規劃與需求彙整。
- [02_model_design.md](./notes/06_sentiment_analysis_tensorflow/02_model_design.md) — 模型與流程設計。
- [03_data_preprocessing.ipynb](./notes/06_sentiment_analysis_tensorflow/03_data_preprocessing.ipynb) — 資料清理與切分。
- [03_text_preprocessing.md](./notes/06_sentiment_analysis_tensorflow/03_text_preprocessing.md) — 文字前處理。
- [04_model_building.ipynb](./notes/06_sentiment_analysis_tensorflow/04_model_building.ipynb) — Baseline Logistic Regression，卡關於 7/19，待優化正則化與 TF‑IDF。
- [04_baseline_report.md](./notes/04_baseline_report.md)  
  最終 Baseline（CountVectorizer + Logistic Regression, C=0.1）  
  訓練、驗證與存檔，Test Accuracy=0.8805，並提出後續改進方向（ngram、SVM）
- 資產與資料：[artifacts/](./notes/06_sentiment_analysis_tensorflow/artifacts/) ｜ [dataset/](./notes/06_sentiment_analysis_tensorflow/dataset/)



---

## 📚 Weekly Notes（原框架保留）
- [Week1‑2_Google_ai_note](./notes/01_Google_ai_note/README.md)
- [2025/07/10 ‑ 下載與探索](./notes/03_cifar10-project/2025-07-10-explore.md)
- [2025/07/11 ‑ 基本資料檢視](./notes/03_cifar10-project/2025-07-11-inspect.md)

---

## 🗺 Repo Map（精簡版）
```
notes/
  00_leetcode-solutions/
  01_Google_ai_note/
  02_kaggle-pandas-practice/
  03_cifar10-project/
  04_data_pipeline_and_preprocessing/
  05_pandas_eda_advanced/
  06_sentiment_analysis_tensorflow/
```

---

## 📝 Changelog
- 2025‑08‑14 — 依 `01/02/03` 資料夾順序重排 README，將 Sentiment Analysis 歸入 Projects 區塊，並修正所有檔案為 Markdown 連結格式。

