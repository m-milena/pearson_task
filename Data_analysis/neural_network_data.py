import mysql.connector

from database_config import db_connection_config
import database_connect
import database_disconnect
import csv

# database connect
db_connection = database_connect.database_connect(db_connection_config)
db_cursor = db_connection.cursor()

sql_select = "SELECT year, gpa, maths_exam, art_exam, language_exam, social_activity, essay_score, interview_score, score, graduated FROM sql_students.graduates INNER JOIN sql_students.score_board ON graduates.id=score_board.id"

with open('../Neural_network/neural_network_data.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows([['year', 'gpa', 'maths exam', 'art exam', 'language exam', 'social activity', 'essay score', 'interview score', 'score', 'graduated']])
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	count = 0
	for row in db_record:
		writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])


csvfile.close()
		 



# database disconnect
database_disconnect.database_disconnect(db_connection, db_connection.cursor())
