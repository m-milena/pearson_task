import mysql.connector

from database_config import db_connection_config
import database_connect
import database_disconnect
import graduated_scores_graph
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

from progress_bar import printProgressBar
progress_bar_count = 1
for i in range(len(years)):
	# Get data about gpa students which graduated
	sql_select = "SELECT score_board.gpa FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='TRUE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	gpa_graduated = []
	for row in db_record: 
		gpa_graduated.append(round(row[0],2))

	# Get data about gpa students which don't graduated
	sql_select = "SELECT score_board.gpa FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='FALSE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	gpa_dont_graduated = []
	for row in db_record: 
		gpa_dont_graduated.append(round(row[0],2))

	# Get data about maths_exam students which graduated
	sql_select = "SELECT score_board.maths_exam FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='TRUE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	maths_exam_graduated = []
	for row in db_record: 
		maths_exam_graduated.append(round(row[0],2))

	# Get data about maths_exam students which graduated
	sql_select = "SELECT score_board.maths_exam FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='FALSE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	maths_exam_dont_graduated = []
	for row in db_record: 
		maths_exam_dont_graduated.append(round(row[0],2))

	# Get data about art_exam students which graduated
	sql_select = "SELECT score_board.art_exam FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='TRUE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	art_exam_graduated = []
	for row in db_record: 
		art_exam_graduated.append(round(row[0],2))

	# Get data about art_exam students which dont graduated
	sql_select = "SELECT score_board.art_exam FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='FALSE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	art_exam_dont_graduated = []
	for row in db_record: 
		art_exam_dont_graduated.append(round(row[0],2))

	# Get data about language_exam students which graduated
	sql_select = "SELECT score_board.language_exam FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='TRUE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	language_exam_graduated = []
	for row in db_record: 
		language_exam_graduated.append(round(row[0],2))

	# Get data about language_exam students which dont graduated
	sql_select = "SELECT score_board.language_exam FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='FALSE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	language_exam_dont_graduated = []
	for row in db_record: 
		language_exam_dont_graduated.append(round(row[0],2))

	# Get data about social_activity students which graduated
	sql_select = "SELECT score_board.social_activity FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='TRUE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	social_activity_graduated = []
	for row in db_record: 
		social_activity_graduated.append(row[0])

	# Get data about social_activity students which dont graduated
	sql_select = "SELECT score_board.social_activity FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='FALSE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	social_activity_dont_graduated = []
	for row in db_record: 
		social_activity_dont_graduated.append(row[0])

	# Get data about essay_score students which graduated
	sql_select = "SELECT score_board.essay_score FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='TRUE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	essay_score_graduated = []
	for row in db_record: 
		essay_score_graduated.append(round(row[0],2))

	# Get data about essay_score students which dont graduated
	sql_select = "SELECT score_board.essay_score FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='FALSE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	essay_score_dont_graduated = []
	for row in db_record: 
		essay_score_dont_graduated.append(round(row[0],2))

	# Get data about interview_score students which dont graduated
	sql_select = "SELECT score_board.interview_score FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='TRUE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	interview_score_graduated = []
	for row in db_record: 
		interview_score_graduated.append(round(row[0],2))

	# Get data about interview_score students which dont graduated
	sql_select = "SELECT score_board.interview_score FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='FALSE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	interview_score_dont_graduated = []
	for row in db_record: 
		interview_score_dont_graduated.append(round(row[0],2))

	# Get data about total score students which dont graduated
	sql_select = "SELECT score_board.score FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='TRUE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	score_graduated = []
	for row in db_record: 
		score_graduated.append(round(row[0],2))

	# Get data about total score students which dont graduated
	sql_select = "SELECT score_board.score FROM score_board INNER JOIN graduates ON score_board.id=graduates.id  WHERE year="+str(years[i])+" AND graduates.graduated='FALSE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	score_dont_graduated = []
	for row in db_record: 
		score_dont_graduated.append(round(row[0],2))

	titles = ['Results of students which graduated', "Results of students which didn't graduated", '', ""]
	fig_title = "Exams and scores result in "+str(years[i])
	xlabel = ["MATHS EXAM", "MATHS EXAM", "INTERVIEW SCORE", "INTERVIEW SCORE"]
	ylabel = ["ART EXAM", "ART EXAM", "ESSAY SCORE", "ESSAY SCORE"]
	savename = "graduated_score_graph_"+str(years[i])+"_part1"
	graduated_scores_graph.draw_graph(maths_exam_graduated, art_exam_graduated, maths_exam_dont_graduated, art_exam_dont_graduated, interview_score_graduated, essay_score_graduated, interview_score_dont_graduated, essay_score_dont_graduated, titles, fig_title, xlabel, ylabel, savename)


	titles = ['Results of students which graduated', "Results of students which didn't graduated", '', ""]
	fig_title = "Exams and scores result in "+str(years[i])
	xlabel = ["GPA", "GPA", "LANGUAGE EXAM", "LANGUAGE EXAM"]
	ylabel = ["TOTAL SCORE", "TOTAL SCORE", "SOCIAL ACTIVITY", "SOCIAL ACTIVITY"]
	savename = "graduated_score_graph_"+str(years[i])+"_part2"
	graduated_scores_graph.draw_graph(gpa_graduated, score_graduated, gpa_dont_graduated, score_dont_graduated, language_exam_graduated, social_activity_graduated, language_exam_dont_graduated, social_activity_dont_graduated, titles, fig_title, xlabel, ylabel, savename)
	printProgressBar(progress_bar_count, len(years), prefix = 'Getting data:', suffix = 'Complete', length = 50)
	progress_bar_count = progress_bar_count + 1

# database disconnect
database_disconnect.database_disconnect(db_connection, db_connection.cursor())




