
class Task():
    def __init__(self, title, done=False, piority=1):
        self.title = title
        self.done = done
        self.piority = piority
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

    def add(self, title, piority):
        pior = Task(piority)
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

    def nz(self):
        for i in range(len(self.tasks)):
            if self.tasks[i].done==False:
                print(self.tasks[i])

    def menu(self):
        print("""
            MENU:
                [1]: Dodaj
                [2]: Pokaż
                [3]: Zrobione
                [4]: Usuń
                [5]: Pokaż tylko nie zrobione
                [0]: Wyjdz
            
        """)
        t = int(input("Co chcesz zrobić?: "))
        if t == 0:
            return
        elif t == 1:
            self.add()
        elif t == 2:
            self.show()
        elif t == 3:
            self.mark_down()
        elif t == 4:
            self.remove()
        elif t == 5:
            self.nz()
        else:
            print("Wybierz prawidłową opcje")
            self.menu()



todolist = TodoList()

todolist.add("nauczyć sie pythona", 1)
todolist.add("nauczyć sie pythona", 3)
todolist.add("test", 3)
todolist.show()
#do testów
#print("-----")
todolist.mark_down(1)
todolist.remove(1)
todolist.mark_down(1)
todolist.show()
todolist.nz()