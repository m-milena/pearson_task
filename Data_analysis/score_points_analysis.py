import mysql.connector

from database_config import db_connection_config
import database_connect
import database_disconnect
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

# Get data about minimum score point where students are accepted in different years
minimum_score = []
for i in range(len(years)):
	sql_select = "SELECT MIN(score) FROM score_board WHERE accepted='TRUE' AND year="+str(years[i])
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	minimum_score.append(*db_record[0])
print(minimum_score)

# Get data about maximum score point in different years
maximum_score = []
for i in range(len(years)):
	sql_select = "SELECT MAX(score) FROM score_board WHERE accepted='TRUE' AND year="+str(years[i])
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	maximum_score.append(*db_record[0])

print(maximum_score)

# Get data about average score point accepted students in different years
average_score = []
for i in range(len(years)):
	sql_select = "SELECT AVG(score) FROM score_board WHERE accepted='TRUE' AND year="+str(years[i])
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	average_score.append(*db_record[0])

print(average_score)

# TODO: przyblizenie wartości sredniej

# database disconnect
database_disconnect.database_disconnect(db_connection, db_connection.cursor())




