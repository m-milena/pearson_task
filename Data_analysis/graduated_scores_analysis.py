import mysql.connector

from database_config import db_connection_config
import database_connect
import database_disconnect
import dotted_graph
# database connect
db_connection = database_connect.database_connect(db_connection_config)
db_cursor = db_connection.cursor()

# Get data about years of recruitment
sql_select = "SELECT DISTINCT year FROM score_board"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
years = []
for row in db_record:
	years.append(row[0]) 

#------------------ YEAR = 1980 ----------------------------------------
# Get data about gpa students which graduated
sql_select = "SELECT score_board.gpa FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='TRUE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
gpa_graduated = []
for row in db_record: 
	gpa_graduated.append(round(row[0],2))

# Get data about gpa students which don't graduated
sql_select = "SELECT score_board.gpa FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='FALSE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
gpa_dont_graduated = []
for row in db_record: 
	gpa_dont_graduated.append(round(row[0],2))

# Get data about maths_exam students which graduated
sql_select = "SELECT score_board.maths_exam FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='TRUE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
maths_exam_graduated = []
for row in db_record: 
	maths_exam_graduated.append(round(row[0],2))

# Get data about maths_exam students which graduated
sql_select = "SELECT score_board.maths_exam FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='FALSE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
maths_exam_dont_graduated = []
for row in db_record: 
	maths_exam_dont_graduated.append(round(row[0],2))

# Get data about art_exam students which graduated
sql_select = "SELECT score_board.art_exam FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='TRUE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
art_exam_graduated = []
for row in db_record: 
	art_exam_graduated.append(round(row[0],2))

# Get data about art_exam students which dont graduated
sql_select = "SELECT score_board.art_exam FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='FALSE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
art_exam_dont_graduated = []
for row in db_record: 
	art_exam_dont_graduated.append(round(row[0],2))

dotted_graph.draw_graph(maths_exam_graduated, art_exam_graduated, maths_exam_dont_graduated, art_exam_dont_graduated, "Maths and Art Exam analyse (1980)", "MATHS EXAM", "ART EXAM", "graph1")

# Get data about language_exam students which graduated
sql_select = "SELECT score_board.language_exam FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='TRUE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
language_exam_graduated = []
for row in db_record: 
	language_exam_graduated.append(round(row[0],2))

# Get data about language_exam students which dont graduated
sql_select = "SELECT score_board.language_exam FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='FALSE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
language_exam_dont_graduated = []
for row in db_record: 
	language_exam_dont_graduated.append(round(row[0],2))

# Get data about social_activity students which graduated
sql_select = "SELECT score_board.social_activity FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='TRUE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
social_activity_graduated = []
for row in db_record: 
	social_activity_graduated.append(row[0])

# Get data about social_activity students which dont graduated
sql_select = "SELECT score_board.social_activity FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='FALSE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
social_activity_dont_graduated = []
for row in db_record: 
	social_activity_dont_graduated.append(row[0])

# Get data about essay_score students which graduated
sql_select = "SELECT score_board.essay_score FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='TRUE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
essay_score_graduated = []
for row in db_record: 
	essay_score_graduated.append(round(row[0],2))

# Get data about essay_score students which dont graduated
sql_select = "SELECT score_board.essay_score FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='FALSE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
essay_score_dont_graduated = []
for row in db_record: 
	essay_score_dont_graduated.append(round(row[0],2))

# Get data about interview_score students which graduated
sql_select = "SELECT score_board.interview_score FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='TRUE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
interview_score_graduated = []
for row in db_record: 
	interview_score_graduated.append(round(row[0],2))


# Get data about interview_score students which dont graduated
sql_select = "SELECT score_board.interview_score FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year=1980 AND graduates.graduated='FALSE'"
db_cursor.execute(sql_select)
db_record = db_cursor.fetchall()
interview_score_dont_graduated = []
for row in db_record: 
	interview_score_dont_graduated.append(round(row[0],2))

dotted_graph.draw_graph(interview_score_graduated, essay_score_graduated, interview_score_dont_graduated, essay_score_dont_graduated, "Interview and Essay Score analyse (1980)", "INTERVIEW SCORE", "ESSAY SCORE", "graph1")

# database disconnect
database_disconnect.database_disconnect(db_connection, db_connection.cursor())




