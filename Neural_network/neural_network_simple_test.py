import keras.models
import numpy as np

data =[[1.0, 0.0, 0.0, 0.0, 1, 0.0, 0.0, 0], [1.679173887707293,0.1303514800611129,0.0610303304224078,0.6460131622122098,1,0.1961935177014677,0.0011812160610932,220],
[3.5347758289426565,0.990938673377854,0.9931043614936594,0.6400070062755213,1,0.9754786368504057,0.9847186733572431,877],
[3.983336344989948,0.984815079223391,0.9632038736482279,0.9358949774447819,5,0.9993128283736582,0.13725716810265956,892],
[4.0, 1.0, 1.0, 1.0, 5, 1.0, 1.0, 1115]]

from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
data_scale = min_max_scaler.fit_transform(data)
data_scaled =data_scale[1:4,:]
model = keras.models.load_model("./learned_networks/16x8x16_acc_t6835v7088.model")

if (data_scaled.ndim == 1):
    data_scaled = np.array([data_scaled])

prediction = model.predict(data_scaled)

print(prediction)
