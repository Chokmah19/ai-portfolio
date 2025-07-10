# 📒 Pandas 筆記

## 1. Creating, Reading and Writing

### A. 核心概念
- 如何從不同格式（CSV、Excel、JSON）讀取資料，以及如何儲存 DataFrame。
    - DateFrame : 類似試算表，是一個**帶有標籤**的二維資料結構，其各列可以包含**不同類型**的資料 。

### B. 常用指令

| 功能      | 指令                                             | 說明                        |
|---------- |-------------------------------------------------|-----------------------------|
| 讀 CSV    | `pd.read_csv('file.csv')`                       | 從 CSV 建立 DataFrame        |
| 讀 Excel  | `pd.read_excel('file.xlsx', sheet_name='Sheet1')` | 讀取指定工作表              |
| 讀 JSON   | `pd.read_json('file.json')`                     | 讀取 JSON                    |
| 輸出 CSV  | `df.to_csv('out.csv', index=False)`             | 不帶索引地輸出                |
| 輸出 Excel| `df.to_excel('out.xlsx', index=False)`          | 同上，輸出至 Excel            |

### C. 範例操作

```python
import pandas as pd

# 讀取 Titanic CSV
df = pd.read_csv('titanic.csv')
# 儲存成 Excel
df.to_excel('titanic.xlsx', index=False)
```

### D. Review Prompt
- 如何在讀取時直接篩掉空值過多的欄位？
    - 在讀取 CSV 時，Pandas 並沒有內建參數直接「跳過缺失值過多的欄位」，因此常用作法是先讀入整個檔案，然後再刪除包含太多 NaN 的欄位。可以先用 pd.read_csv() 讀取檔案。
    - 接著檢查各欄的空值比例，若發現某些欄位多數值為 NaN，就可用 dropna(axis=1, thresh=…) 刪除這些欄。axis=1 表示按欄刪除，thresh 則是「至少要有多少個非空值才保留此欄」的閾值。
    - 如果想按照百分比丟棄缺失值過多的欄，也可以將 thresh 設為 int(df.shape[0]*ratio)
```python
df = pd.read_csv("data.csv")  # 讀入 CSV 為 DataFrame
df.isnull().mean()

# 只保留至少有 3 個非空值的欄位（少於3個非空即丟棄該欄）
df = df.dropna(axis=1, thresh=3)
```

```python
# 刪除缺失超過一半的欄
thresh = int(df.shape[0]*0.5)
df = df.dropna(axis=1, thresh=thresh)
```

> 這樣做能清理資料，去掉無用或資訊太少的欄位，學習到的技能包括利用 Pandas 的缺失值處理函數（dropna）、理解 axis 和 thresh 參數的意義，以及資料清洗的邏輯（刪除缺失值過多的欄可以減少分析干擾）

- 如果要讀取多個 CSV，合併成一個 DataFrame，指令該怎麼寫？
   - **列出檔案清單**：使用 Python 的 os 或 glob 模組，取得指定資料夾中所有 CSV 的路徑列表。
       - 學到檔案 I/O 和檔案篩選（使用 os.listdir 並判斷檔名副檔名）。
   - **讀取並存成 DataFrame 清單**：用迴圈或列表解析（list comprehension）對每個檔案呼叫 pd.read_csv，並將結果存入一個列表。
       - 學到使用列表解析批次執行函數。
   - **合併所有 DataFrame**：使用 pd.concat() 將列表中的所有 DataFrame 併成一個大 DataFrame。
       - ignore_index=True 表示合併後重置索引（不保留原檔案的索引），使最終索引連續。concat 函數會自動將欄位對齊（若不同檔案有不同欄，則缺失值以 NaN 填補）。這一步學到資料整合與索引管理：將多個表格串起來，便於後續一起分析。也可用generator 或 map 省掉中間列表。

```python
import pandas as pd, os
folder_path = "data" # CSV 所在資料夾
csv_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".csv")]
all_data = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)
```
> 很多時候資料分散在多個檔案，透過自動讀取合併可以避免手動複製，快速整合成統一的資料集，方便後續分析和視覺化

## 2. Indexing, Selecting & Assigning

### A. 核心概念
- 如何用標籤與位置存取列與欄，以及如何新增、修改資料。
    - 負數也可用以選擇，會從最後值開始往前計數

### B. 常用指令

| 功能            | 指令                                   | 說明                        |
|---------------|--------------------------------------|--------------------------------|
| 標籤存取資料     | `df.loc[row_label, col_label]`       | 以索引／欄名存取               |
| 位置存取資料     | `df.iloc[row_idx, col_idx]`          | 以整數位置存取                 |
| 子集取值        | `df['Age']`                          | 取得單一欄                     |
| 布林選擇        | `df[df['Age'] > 30]`                 | 年齡大於 30 的所有列            |
| 新增欄位        | `df['Child'] = df['Age'] < 16`       | 建立新欄位                     |

- loc & iloc差異
    - 定位方式
        - df.loc[...]：**標籤（label）**為基準，以索引或欄名來選取。
        - df.iloc[...]：**位置（integer position）**為基準，以整數位置來選取。
    - 切片（slice）行為
        - loc[a:b]：包含終點標籤 b。
        - iloc[i:j]：不包含終點位置 j 。
    - 接受的輸入類型
        - loc：標籤、標籤清單、布林陣列、條件篩選。
        - iloc：整數、整數清單、整數陣列（不接受布林 Series）。

### C. 範例操作

```python
# 取得第 5 列、第 2 欄
value = df.iloc[4, 1]
# 取出所有女性資料
females = df.loc[df['Sex']=='female', :]
# 加入 Child 欄位
df['Child'] = df['Age'].apply(lambda x: 1 if x<16 else 0)
```

### D. Review Prompt
- 如果要連續取多個欄位（Age, Fare），用哪種寫法效率更高？
    - df[['Age','Fare']] vs. df.loc[:, ['Age','Fare']]
    - df[['Age','Fare']] 這種索引取用直接透過 __getitem__，在 Pandas 內部實作上少了一層「標籤 → 位置 → 再存取」的流程，相較於 loc 會略快一些。
```python
# 建議用法（較直覺且略快）
subset = df[['Age', 'Fare']]

# 等價但多一步解析定位器，執行略慢
subset = df.loc[:, ['Age', 'Fare']]
```
> 學到「索引取用的內部實作機制」：不同 API 看起來功能相同，但實作路徑不同，影響效能。

- 新增欄位時，如何避免 SettingWithCopyWarning？
    - Pandas 有時對切出的「view」(共用記憶體的子集) 和「copy」(獨立記憶體) 不明確，直接賦值會出現警告。
        - View（檢視）  
            原 DataFrame 內部記憶體的「窗口」，修改時會反映到母體，也常導致 Pandas 無法判定是改 view 還是 copy，跳出 SettingWithCopyWarning。
        - Copy（複製）  
            完全分配新的記憶體空間，和原 DataFrame 無關，修改不會影響原物件，也不會有警告。
```python
# ❌ 錯誤示範：可能是在切片的 view 上操作
sub = df[df['Age'] > 30]
sub['is_senior'] = True           # ← 這裡常跳 warning

# ✅ 正確做法：用 .loc 明確告訴 Pandas「在原 DataFrame 上」賦值
df.loc[df['Age'] > 30, 'is_senior'] = True

# 或，先確保操作對象是新的 copy
sub = df[df['Age'] > 30].copy()
sub['is_senior'] = True           # ← 這時不會 warning
```
> 學到「view vs. copy」的差別，以及如何用 .loc[...] 或 .copy() 明確掌控記憶體行為
## 3. Summary Functions and Maps

### A. 核心概念
- 使用聚合函數（mean、sum、max）與 map/apply 快速轉換資料。

### B. 常用指令

| 功能              | 指令                                     | 說明                          |
|-----------------|----------------------------------------|-----------------------------|
| 計算平均值         | `df['Fare'].mean()`                    | 算出平均票價                    |
| 計算總和           | `df['Survived'].sum()`                 | 算出存活人數                    |
| map 轉換        | `df['Sex'].map({'male':0,'female':1})` | 對 Series 進行對應轉換              |
| apply 函數      | `df['Age'].apply(lambda x: x+1)`       | 對每筆資料套用函數                 |

### C. 範例操作

```python
# 平均票價
avg_fare = df['Fare'].mean()
# map 性別到數值
df['Sex_num'] = df['Sex'].map({'male':0,'female':1})
```

### D. Review Prompt
當資料中有缺值時，mean() 會怎麼處理？如何跳過缺值？

map 與 replace 有什麼差異，何時用哪一個？

## 4. GroupBy and Sorting

### A. 核心概念
- 分群統計與排序，快速找出資料趨勢與異常。

### B. 常用指令

| 功能             | 指令                                                 | 說明                         |
|----------------|----------------------------------------------------|----------------------------|
| 分群計算平均       | `df.groupby('Pclass')['Survived'].mean()`            | 各艙等存活率                    |
| 分群多重聚合       | `df.groupby('Pclass').agg({'Age':'mean','Fare':'sum'})` | 同時計算多個欄位的不同聚合函數           |
| 排序              | `df.sort_values('Fare', ascending=False)`           | 依 Fare 由大到小排序            |
| reset index    | `df.reset_index()`                                  | 分群後重建連續索引               |

### C. 範例操作

```python
# 各艙等存活率
surv_rate = df.groupby('Pclass')['Survived'].mean()
# 同時計算年齡平均與票價總和
stats = df.groupby('Pclass').agg({'Age':'mean','Fare':'sum'})
# 依票價排序
top_fare = df.sort_values('Fare', ascending=False).head(10)
```

### D. Review Prompt
如果要先排序再分群，指令順序怎麼寫？

分群後要加上 reset_index() 的原因是？


## 5. Data Types and Missing Values

### A. 核心概念
- 瞭解欄位資料型態，處理缺失值。

### B. 常用指令

| 功能                 | 指令                                       | 說明                       |
|--------------------|------------------------------------------|--------------------------|
| 查看型態            | `df.dtypes`                              | 各欄位的資料型態                |
| 轉換型態            | `df['Age'] = df['Age'].astype(int)`       | 把 Age 轉為整數                 |
| 檢查缺值            | `df.isna().sum()`                        | 每個欄位的缺失值數量               |
| 丟棄缺值行          | `df.dropna(subset=['Age'])`              | 丟掉 Age 為 NA 的列             |
| 填補缺值            | `df['Age'].fillna(df['Age'].mean(), inplace=True)` | 以平均值填補                   |

### C. 範例操作

```python
# 查看各欄位資料型態
print(df.dtypes)
# 填補缺值：用平均年齡
df['Age'].fillna(df['Age'].mean(), inplace=True)
```

### D. Review Prompt
何時要用 dropna() 而不是 fillna()？

如果只想填補部分列，subset 參數要怎麼用？



## 6. Renaming and Combining

### A. 核心概念
- 重命名欄位、合併多個 DataFrame。

### B. 常用指令

| 功能             | 指令                                            | 說明                         |
|----------------|-----------------------------------------------|----------------------------|
| 重命名欄位        | `df.rename(columns={'old':'new'}, inplace=True)` | 一次重命名多個欄位                |
| 併列合併 (horizontal) | `pd.concat([df1, df2], axis=1)`                | 按列方向拼接                     |
| 併行合併 (vertical)   | `pd.concat([df1, df2], axis=0)`                | 按行方向拼接                     |
| 依 key 合併       | `pd.merge(df1, df2, on='id', how='inner')`      | SQL 式資料合併                    |

### C. 範例操作

```python
# 重命名
df.rename(columns={'PassengerId':'PID','Survived':'Alive'}, inplace=True)
# 併行合併
df_all = pd.concat([df_train, df_test], axis=0)
# key 合併
merged = pd.merge(df1, df2, on='id', how='left')
```

### D. Review Prompt
concat 與 merge 的差異是什麼？

如果要做 multiple-key 的 merge，要如何指定？