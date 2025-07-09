from urllib.parse import quote_plus
from sqlalchemy import create_engine, text

from settings import login, password, host, port, base

class DbWorker:

    def __init__(self):
        self.engine = create_engine(f"mysql+pymysql://{login}:{quote_plus(password)}@{host}:{port}/{base}")

    def write_task_to_db(self, name, descriprion, term):
        sql = f'''INSERT INTO homework (subject, task, deadline) VALUES ('{name}', '{descriprion}', '{term}')'''
        print(sql) 

        with self.engine.connect() as connection:
            connection.execute(text(sql))
            connection.commit()

    def get_unticked_tasks(self):
        sql = '''SELECT id, subject, task, deadline FROM school_diary.homework WHERE is_done = 0;'''
   
        with self.engine.connect() as connection:
            result = connection.execute(text(sql))
        return result 

            
    def complete_task(self, task_id):
        sql = f'''UPDATE homework SET is_done = '1' WHERE id = '{task_id}';'''
        with self.engine.connect() as connection:
            connection.execute(text(sql))
            connection.commit()

    def get_ticked_tasks(self):
        sql = '''SELECT id, subject, task, deadline FROM school_diary.homework WHERE is_done = 1;'''
   
        with self.engine.connect() as connection:
            result = connection.execute(text(sql))
        return result
    
    def statictic(self):
        sql = '''SELECT subject, COUNT(DISTINCT task) AS unique_task_count FROM homework GROUP BY subject;'''

        with self.engine.connect() as connection:
            result = connection.execute(text(sql))
        return result
     
    def dead_deadline(self):
        sql = '''SELECT id, task FROM homework WHERE deadline < CURDATE();'''

        with self.engine.connect() as connection:
            result = connection.execute(text(sql))
        return result
    
    def export(self):
        sql = '''SELECT task FROM homework;'''
        with self.engine.connect() as connection:
            result = connection.execute(text(sql))
        return result


    

                

            