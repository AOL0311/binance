import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.exceptions import DataConversionWarning
import warnings

# 關閉 sklearn 的 dtype 警告
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

folder_path = 'BTC_USDT'

for filename in os.listdir(folder_path):
    if filename.startswith('BTCUSDT_') and filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        try:
            data = pd.read_csv(file_path, header=None, low_memory=False)
            data = data[26:]

            # 強制轉 float（特徵與價格欄位）
            for col in [1, 4, 5, 6, 7, 8, 9]:
                data.iloc[:, col] = pd.to_numeric(data.iloc[:, col], errors='coerce')

            # 特徵
            features = data.iloc[:, [1, 5, 6, 7, 8, 9]]

            # 標籤 = 明天收盤 > 今天收盤
            data.iloc[:, 10] = (data.iloc[:, 4].shift(-1) > data.iloc[:, 4]).astype(int)
            labels = data.iloc[:, 10]

            # 移除任何 NaN 行
            combined = pd.concat([features, labels], axis=1).dropna()
            features = combined.iloc[:, :-1]
            labels = combined.iloc[:, -1].astype(int)

            # 若標籤不是 0/1，跳過
            if not set(labels.unique()).issubset({0, 1}):
                print(f"⚠️ {filename}：標籤不為二元分類，跳過")
                continue

            # 分割資料
            x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=77)

            model = SVC(kernel='linear')
            model.fit(x_train, y_train)

            y_pred = model.predict(x_test)
            acc = accuracy_score(y_test, y_pred)

            print(f"✅ {filename}")
            print(f"   Accuracy: {acc:.4f}")
            result_df = pd.DataFrame({
                'Predicted': y_pred,
                'Actual': y_test.values
            })
            print(result_df.head(10))
            print("----\n")

        except Exception as e:
            print(f"❌ {filename} 發生錯誤: {e}")
