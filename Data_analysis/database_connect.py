import mysql.connector

def database_connect(db_connection_config):

	try:	
		db_connection = mysql.connector.connect(**db_connection_config)
		if db_connection.is_connected():
			db_info = db_connection.get_server_info()
			print('Connected to MySQL database...\nMySQL Server version on', db_info)
			db_cursor = db_connection.cursor()
			db_cursor.execute("select database();")
			db_record = db_cursor.fetchone()
			print ('You are connected to', *db_record)
			return db_connection


	except mysql.connector.Error as db_error:
		print ('Error while conecting to MySQL', db_error)

