# Reading data from csv file
import pandas as pd
df = pd.read_csv('neural_network_data.csv')
# Writing data to array
dataset = df.values

# Neural network inputs:
X = dataset[:,1:9]
# Neural network output
Y = dataset[:,9]

# Scaling X data to be from 0 to 1
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)

# Splitting data to training and validation+test set (70/30%)
from sklearn.model_selection import train_test_split
X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size = 0.3)

# Splitting data to validation and test set (50/50%)
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size = 0.5)

# Creating neural network
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import advanced_activations

# Adding Regularization to our Neural Network
from keras.layers import Dropout
from keras import regularizers

# Network architecture
model = Sequential([
	Dense(16, kernel_initializer='normal', activation = 'relu', kernel_regularizer=regularizers.l2(0.02), input_shape = 8,)),
	Dropout(0.5),
	Dense(8, kernel_initializer='normal', activation = 'relu'),
	Dense(16, kernel_initializer='normal', activation = 'relu'),
	Dense(1, kernel_initializer='normal', activation = 'sigmoid'),
])

# Finding best weights
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# Training and validation
hist = model.fit(X_train, Y_train, batch_size=30, epochs=80, validation_data = (X_val, Y_val))

# Testing
loss = model.evaluate(X_test, Y_test)[0]
accuracy = model.evaluate(X_test, Y_test)[1]
print("Test loss: ", loss)
print("Test accuracy: ", accuracy)

print('Do you want to save this model? y/n')
answer = input()
if answer == 'y':
	print('Input filename:')
	filename = input()
	model.save(filename+'.model')
	hist_df = pd.DataFrame(hist.history) 
	with open(filename+'_logg.csv', 'w') as f:
    		hist_df.to_csv(f)

# visualisation
import matplotlib.pyplot as plt
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='upper right')
if answer == 'y':
	plt.savefig(filename+'_loss_graph.png',dpi=400)
plt.show()

plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='lower right')
if answer == 'y':
	plt.savefig(filename+'_acc_graph.png',dpi=400)
plt.show()



		
