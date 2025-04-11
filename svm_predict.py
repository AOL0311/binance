import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

File = 'BTC_USDT/BTCUSDT_1Day.csv'

data = pd.read_csv(File, header = None)
data = data[26:]

features = data.iloc[:, [1, 5, 6, 7, 8, 9]]
data.iloc[:, [10]] = (data.iloc[:, [4]].shift(-1) > data.iloc[:, [4]]).astype(int)

labels = data.iloc[:, [10]]

x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size = 0.2, random_state = 77)

svm_model = SVC(kernel = 'linear')
svm_model.fit(x_train, y_train)

y_pred = svm_model.predict(x_test)

print(f'Accuracy Score: {accuracy_score(y_test, y_pred)}')