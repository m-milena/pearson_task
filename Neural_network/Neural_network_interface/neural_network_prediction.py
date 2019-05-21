import keras.models
import numpy as np

def check_probability(gpa, maths_exam, art_exam, language_exam, social_activity, essay_score, interview_score, score):
	
	data =[[1.0, 0.0, 0.0, 0.0, 1, 0.0, 0.0, 0], 
	[gpa, maths_exam, art_exam, language_exam, social_activity, essay_score, interview_score, score],
	[4.0, 1.0, 1.0, 1.0, 5, 1.0, 1.0, 1115]]

	from sklearn import preprocessing
	min_max_scaler = preprocessing.MinMaxScaler()
	data_scale = min_max_scaler.fit_transform(data)
	data_scaled =data_scale[1:2,:]
	model = keras.models.load_model("../learned_networks/16x8x16_acc_t6835v7088.model")

	if (data_scaled.ndim == 1):
	    data_scaled = np.array([data_scaled])

	prediction = float(model.predict(data_scaled))
	return prediction*100
