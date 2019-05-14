print(60*'-'+'\nEnter user name: ')
db_user = input()
print(60*'-'+'\nEnter password: ')
db_passwd = input()
print(60*'-')


db_connection_config = {
	'host':'127.0.0.1',
	'port':'3306',
	'database':'sql_students',
	'user':db_user,
	'passwd':db_passwd
}
