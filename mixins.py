class Loggable:
    def __init__(self):
        self.title = ''
    def log(self):
        print('Log message from ' + self.title)

class Connection:
    def __init__(self):
        self.sever = ''
    def connect(self):
        print('connecting to database on ' + self.sever)  

class SqlDatabase(Connection, Loggable):
    def __init__(self):
       self.title = 'Sql Connection Demo'
       self.sever = 'Some_sever'

def framework(item):
    if isinstance(item, Connection):
        item.connect
    if isinstance(item, Loggable):
        item.log()

#sql_connection = SqlDatabase()
class JustLog(Loggable):
    def __init__(self):
        self.title = 'Just logging'

just_log = JustLog()
framework(just_log)



