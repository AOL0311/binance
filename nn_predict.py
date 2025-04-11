import numpy as np
from sklearn.model_selection import train_test_split
from keras import models
from keras import layers

File = 'BTC_USDT/BTCUSDT_1Week.csv'

datasets = []
with open(File, 'r', encoding = 'utf-8') as file:
    data = file.readlines()

    for line in data:
        line = line.replace('\n', '').split(',')
        
        datasets.append(line)

features = [[float(line[1]), float(line[5]), float(line[6]), float(line[7]), float(line[8]), float(line[9])] for line in datasets[26:-1]]
labels = [1 if datasets[i + 1][4] > datasets[i][4] else 0 for i in range(len(datasets) - 1)]
labels = labels[26:]

features = np.array(features)
labels = np.array(labels)

train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.2, random_state = 77)

model = models.Sequential()
model.add(layers.Dense(64, input_dim = len(train_features[0]), activation = 'relu'))
model.add(layers.Dense(32, activation = 'relu'))
model.add(layers.Dense(1, activation = 'sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.fit(train_features, train_labels, epochs = 10, batch_size = 32)

loss, accuracy = model.evaluate(test_features, test_labels)
print(f'Accuracy: {accuracy}')