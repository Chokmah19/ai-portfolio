import pandas as pd
import numpy as np

class MyScaler:
    def __init__(self):
        # 用來存放每個欄位的 mean 和 std
        self.means = {}
        self.stds  = {}

    def fit(self, df: pd.DataFrame):
        # 指定要標準化的欄位清單
        cols = ['age', 'income']
        for col in cols:
            self.means[col] = df[col].mean()
            self.stds[col]  = df[col].std()
        return self

    def transform(self, df: pd.DataFrame):
        df_new = df.copy()
        for col, mean in self.means.items():
            std = self.stds[col]
            df_new[col] = (df_new[col] - mean) / std
        return df_new

    def fit_transform(self, df: pd.DataFrame, tol: float = 1e-6):
        # 1) 先 fit
        self.fit(df)
        # 2) 再 transform
        df_scaled = self.transform(df)
        # 3) 檢查結果：mean ≈ 0、std ≈ 1
        means = df_scaled[list(self.means.keys())].mean()
        stds  = df_scaled[list(self.stds.keys())].std()
        # 如果超出容許誤差，就報錯 (ValueError，並告知是「哪欄的平均／標準差」不對)
        for col in self.means.keys():
            if not np.isclose(means[col], 0.0, atol=tol):
                raise ValueError(f"欄位 {col} 平均不在 0 ± {tol}：{means[col]}")
            if not np.isclose(stds[col], 1.0, atol=tol):
                raise ValueError(f"欄位 {col} 標準差不在 1 ± {tol}：{stds[col]}")
        print("✅ 標準化檢查通過：mean =", means.to_dict(), "std =", stds.to_dict())
        return df_scaled
