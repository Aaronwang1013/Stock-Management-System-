class BaseConfig:
    username = 'devs'
    password = 'pythonstock'
    host = '127.0.0.1'
    port = '3306'
    database = 'Stock_management'
    charset= 'utf8'

class DBTable(BaseConfig):
    table = {
        'Stock_management' : 'inst_institute'
    }