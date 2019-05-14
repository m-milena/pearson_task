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


# Get data about quantity of recruitment students in different years
quantity_of_students= []
for i in range(len(years)):
	sql_select = "SELECT COUNT(id) FROM score_board WHERE year="+str(years[i])
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	quantity_of_students.append(*db_record[0])


# Get data about how many students are accepted in different years
quantity_of_accepted = []
for i in range(len(years)):
	sql_select = "SELECT COUNT(id) FROM score_board WHERE year="+str(years[i])+" AND accepted='TRUE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	quantity_of_accepted.append(*db_record[0])


# Get data about how many students graduated from different years
quantity_of_graduated = []
for i in range(len(years)):
	sql_select = "SELECT COUNT(graduates.id) FROM graduates INNER JOIN score_board ON graduates.id=score_board.id WHERE score_board.year="+str(years[i])+" AND graduated='TRUE'"
	db_cursor.execute(sql_select)
	db_record = db_cursor.fetchall()
	quantity_of_graduated.append(*db_record[0])

# Data graph
import students_quantity_graph
students_quantity_graph.draw_graph(years, quantity_of_students, quantity_of_accepted, quantity_of_graduated)


# database disconnect
database_disconnect.database_disconnect(db_connection, db_connection.cursor())




