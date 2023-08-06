import urllib
import sqlalchemy as sa
import pymysql
import sqlite3
import psycopg2
import cx_Oracle
import teradatasql

pymysql.install_as_MySQLdb()

#MS SQL Server

def msscon(server,database,uid,pwd,port=1433,dr="{SQL Server}"):
    '''
    This Function creates connection to the SQL Server database for the data Retrieval/Insertion
    **Parameters Required for the connection
    -driver: Default SQL Server
    -server: Your Database server
    -port: Your Database server port Default is 1433
    -database: Database name
    -uid: SQL Server username
    -pwd: SQL Server password
    '''
    try:
        params = 'DRIVER='+dr+';' \
                 'SERVER='+server+';' \
                 'PORT='+str(port)+';' \
                 'DATABASE='+database+';' \
                 'UID='+uid+';' \
                 'PWD='+pwd+';'
        params = urllib.parse.quote_plus(params)
        con = sa.create_engine('mssql+pyodbc:///?odbc_connect=%s' % params)
    except Exception as e:
        raise e
    return con

#My SQL Server

def mscon(host,database,username,password,port=3306):
    '''
    This Function creates connection to the MySQL database for the both data retrieval and for data Insertion
    -Parameters Required for the connection
    -Host: Your Database server name
    -Database: Database name
    -Username: Database username
    -Password: Database password
    -Port: Default is 3306
    '''
    try:
        DB = {'servername': host,
          'database': database,
             'username':username,
             'password':password,
             'port':str(port)}
        con = sa.create_engine('mysql://'+ DB['username']+':' + DB['password']+'@'+ DB['servername'] +':'+DB['port']+'/'+ DB['database']+'')
    except Exception as e:
        raise e
    return con


#PG SQL Server
def pgscon(username,password,host,database,port=5432):
    '''
    This Function creates connection to the Postgresql database for the both data retrieval and for data Insertion
    -Parameters Required for the connection
    -Host: Your Database server name
    -Database: Database name
    -Username: Database username
    -Password: Database password
    -port: Default is 5432
    '''
    try:
        DB = {'servername': host,
              'port': str(port),
          'database': database,
             'username':username,
             'password':password}
        con = sa.create_engine('postgresql://'+DB['username']+':'+DB['password']+'@'+DB['servername']+':'+DB['port']+'/'+DB['database']+'')
    except Exception as e:
        raise e
    return con

#Oracle Server

def ocon(host,username,password,service='xe',dialect='oracle',sqldriver='cx_oracle',port=1521):
    '''
    This Function creates connection to the Oracle database for the both data retrieval and for data Insertion
    -Parameters Required for the connection
    -Host: Your Database server name or IP
    -Username: Database username
    -Password: Database password
    -port: Default is 1521
    -service: Default is xe,For Checking Open CMD then write lsnrctl status, Press Enter Check the service name
    -Dialect: Default is oracle
    -sqldriver: Default is cx_oracle
    '''
    DIALECT = dialect
    SQL_DRIVER = sqldriver
    USERNAME = username
    PASSWORD = password
    HOST = host
    PORT = port
    SERVICE = service
    ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE
    try:
        con = sa.create_engine(ENGINE_PATH_WIN_AUTH)
    except Exception as e:
        raise e
    return con
#TeraData Server
def tdscon(host,database,username,password):
    '''
    This Function creates connection to the Teradata database for the both data retrieval and for data Insertion
    -Parameters Required for the connection
    -Host: Your Database server name / IP
    -Database: Database name
    -Username: Database username
    -Password: Database password
    '''
    DB = {'servername': host,
      'database': database,
         'username':username,
         'password':password}
    try:
        con = sa.create_engine(f"teradatasql://{DB['username']}:{DB['password']}@{DB['servername']}/?database={database}")
    except Exception as e:
        raise e
    return con

#MariaDB
def mdb(host,database,username,password,port=3307):
    '''
    This Function creates connection to the Maria database for the both data retrieval and for data Insertion
    -Parameters Required for the connection
    -Host: Your Database server name
    -Database: Database name
    -Username: Database username
    -Password: Database password
    -Port: Default is 3306
    '''
    try:
        DB = {'servername': host,
          'database': database,
             'username':username,
             'password':password,
             'port':str(port)}
        con = sa.create_engine('mysql://'+ DB['username']+':' + DB['password']+'@'+ DB['servername'] +':'+DB['port']+'/'+ DB['database']+'')
    except Exception as e:
        raise e
    return con





