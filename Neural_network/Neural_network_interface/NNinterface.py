from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from neural_network_prediction import check_probability

class NNinterface(QMainWindow):
	
	gpa = 0
	maths_exam = 0
	art_exam = 0
	language_exam = 0
	essay_score = 0
	interview_score = 0
	social_activity = 1
	score = 0
	probability = 0
	def __init__(self):
		super().__init__()
		uic.loadUi('graduation_prediction_interface.ui',self)
		self.setWindowTitle('Graduation prediction app')
	
	def on_graduation_button_clicked(self):
		gpa = float(self.gpa_edit.text())
		maths_exam = float(self.maths_edit.text())
		art_exam = float(self.art_edit.text())
		language_exam = float(self.language_edit.text())
		essay_score = float(self.essay_edit.text())
		interview_score = float(self.interview_edit.text())
		score = int(self.score_edit.text())
		social_activity = self.social_box.value()
		probability = check_probability(gpa, maths_exam, art_exam, language_exam, social_activity, essay_score, interview_score, score)
		self.graduation.setText(str(round(probability, 2))+'%')
		



        

