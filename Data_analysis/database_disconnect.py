import mysql.connector

def database_disconnect(db_connection, db_cursor):
	if(db_connection.is_connected()):
		db_cursor.close()
		db_connection.close()
		print('MySQL connection is closed')
