import numpy as np

import sys
sys.path.insert(0,'./fashion-mnist/utils')
import mnist_reader


X_train, y_train = mnist_reader.load_mnist(\
	'./fashion-mnist/data/fashion', kind='train')
X_test, y_test = mnist_reader.load_mnist(\
	'./fashion-mnist/data/fashion', kind='t10k')

print(X_train, y_train)


