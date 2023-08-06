import threading
from common import email
from sqlalchemy import PoolProxiedConnection, Connection, ResultProxy, create_engine
import common.config as config
cfg = config.Config()

def db_connection() -> PoolProxiedConnection: 
    try: 
        # Create an engine instance
        alchemy_engine = create_engine(f'{cfg.db_dialect}://{cfg.db_user}:{cfg.db_password}@{cfg.db_host}:{cfg.db_port}/{cfg.db_database}', pool_recycle=3600);
        # Connect to PostgreSQL server
        return alchemy_engine.connect();
    except: 
        raise RuntimeError('Error getting DB connection')

def query_sql(connection: Connection, sql: str, parameters) -> ResultProxy:
    return connection.execute(sql, parameters)

# Remember to handle the connection close in the calling code
def execute_sql(connection, sql: str, jobName: str, timeoutSeconds = 10*60, emailFailure = False, raiseException = True):
    print("executing sql: {}".format(sql))
    cursor = connection.cursor() 
    # warn after some time
    t = threading.Timer(timeoutSeconds, email.send_email_closure('WARNING: slow running SQL query from {}'.format(jobName), sql))
    t.start()
    try:
        cursor.execute(sql) 
        connection.commit() 
        cursor.close()
    except Exception as e:
        print('Error executing sql')
        print(e)
        if emailFailure:
            email.send_email('Error: SQL failed', "sql: {} \nerror: {}".format(sql, e))
        if raiseException:
            raise e
    finally:
        t.cancel()

