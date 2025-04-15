import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

for file in os.listdir('BTC_USDT'):
    if file.startswith('BTCUSDT_') and file.endswith('.csv'):
        path = os.path.join('BTC_USDT', file)

        try:
            df = pd.read_csv(path, low_memory = False)
            df = df.dropna(subset = ['5EMA', '10EMA', '20EMA', 'RSI', 'MACD', 'Signal'])

            x = df[['5EMA', '10EMA', '20EMA', 'RSI', 'MACD', 'Signal']]
            y = df['Close']

            scaler = StandardScaler()
            x_scale = scaler.fit_transform(x)

            x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size = 0.2, random_state = 77)

            svr = SVR(kernel = 'rbf')
            svr.fit(x_train, y_train)

            df['Predicted Close'] = svr.predict(x_scale)

            print(f'Finish SVM predict {path}')
            print(df.tail())

        except Exception as e:
            print(e)