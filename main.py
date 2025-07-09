import sys
import pandas as pd

from db_worker import DbWorker

class Diary:
    def __init__(self):
        self.db_worker = DbWorker()

    def add_task(self):
        print('Какое название у предмета?')
        name = input()
        print('Какое описание задания?')
        descriprion = input()
        print('Каков дедлайн выполнения?')
        term = input()

        self.db_worker.write_task_to_db(name, descriprion, term)
        # выполнить метод write_task_to_db класса DbWorker передав ему параметры, которые ты получил от пользователя

    def view_tasks(self):
        result = self.db_worker.get_unticked_tasks()  
        for id, subject, task, deadline in result:
                print(f"{id}, {subject}, {task}, {deadline.strftime('%Y-%m-%d') if deadline else deadline}")
    
    def tick_task(self):
        print('Какой id задания?')
        task_id = input()
        self.db_worker.complete_task(task_id)

    def view_ticked_tasks(self):
        result = self.db_worker.get_ticked_tasks()  
        for id, subject, task, deadline in result:
                print(f"{id}, {subject}, {task}, {deadline.strftime('%Y-%m-%d') if deadline else deadline}")
    
    def statictic_print(self):
       result = self.db_worker.statictic()
       for subject, task in result:
                print(f"{subject}, {task}")
        
    def deadline_check(self):
        result = self.db_worker.dead_deadline()
        for id, task in result:
                print(f"{id}, {task}")
        

    def better_export(self):
        result = self.db_worker.export()
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        df.to_csv(r"C:\Users\D.Stovba\Documents\Книга1.csv", index=False, encoding='utf-8-sig')
        
                    
                
                    


def menu(diary):
    print('''
    Пункт 1: Добавить задание.
    Пункт 2: Показать все задания.
    Пункт 3: Отметить задание выполненным.
    Пункт 4: Показать выполненные задания.
    Пункт 5: Статистика
    Пункт 6: Проверка по дедлайнам.
    Пункт 7: Экспорт в файл.      
    Пункт 8: Выход''')

    print('Введите номер пункта для выполнения')
    i = input()
    match i:
        case '1':
            # print('Еще не реализовано, введите следующий номер')
            diary.add_task()
        case '2':
            #print('Еще не реализовано, введите следующий номер')
            diary.view_tasks()
        case '3':
            #print('Еще не реализовано, введите следующий номер')
            diary.tick_task()      
        case '8':
            print('Выход из программы...')
            sys.exit(1)
        case '4':
            diary.view_ticked_tasks()
        case '5':
            diary.statictic_print()
        case '6':
            diary.deadline_check()
        case '7':
            diary.better_export()
        case _:
            print('Некорректное число, введите от 1 до 8') 


if __name__ == "__main__":
    diary = Diary()       
    while True:
        menu(diary)
        


