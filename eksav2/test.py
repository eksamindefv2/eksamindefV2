import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '10.101.1.246' 
database = 'DBEksa' 
username = 'sa' 
password = 'seeDB@2017' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = execute("SELECT @@version;")
row = cursor.fetchone()
while row:
	print row[0]
	row = cursor.fetchone()