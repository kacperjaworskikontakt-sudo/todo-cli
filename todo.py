#Projekt: pętla menu (1 dodaj, 2 pokaż, 3 zrobione, 4 usuń, 0 wyjście), jak w kalkulatorze; commit
class Task():
    def __init__(self, title, done=False):
        self.title = title
        self.done = done
        # Uruchamia sie automatycznie, nadaje parametry title i done
    def __str__(self):
        if self.done:
            return f"[x] {self.title}"
        return f"[ ] {self.title}"
        #robi to co wyswieti sie po uzyciu print

class TodoList:
    def __init__(self):
        print("""
        ---------------------
                TO DO 
        ---------------------
        """)
        self.tasks = []
    def add(self, title):
        task = Task(title)
        self.tasks.append(task)
    def show(self):
        for number, task in enumerate(self.tasks, start=1):
            print(f"{number}. {task}")
    def mark_down(self, number):
        if number >= 1 and number < len(self.tasks):
            self.tasks[number - 1].done = True
        else:
            raise ValueError("Zły numer zadania")
    def remove(self, number):
        if number >= 1 and number < len(self.tasks):
            self.tasks.pop(number - 1)
        else:
            raise ValueError("Zły numer zadania")
    def menu(self):
        print("""
            MENU:
                [1]: Dodaj
                [2]: Pokaż
                [3]: Zrobione
                [4]: Usuń
                [0]: Wyjdz
            
        """)
        t = int(input("Co chcesz zrobić?: "))
        if t == 0:
            return
        elif t == 1:
            #skonczyc
            pass



todolist = TodoList()

todolist.add("nauczyć sie pythona")
todolist.add("nauczyć sie pythona")
todolist.show()
#do testów
#print("-----")
todolist.mark_down(1)
todolist.remove(10)
todolist.show()