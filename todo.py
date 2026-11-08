
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
        self.tasks = []
    def add(self, title):
        task = Task(title)
        self.tasks.append(task)
    def main(self):
        print("""
        ---------------------
                TO DO 
        ---------------------
        """)
    def show(self):
        for number, task in enumerate(self.tasks, start=1):
            print(f"{number}. {task}")
    def mark_down(self, number):
        if number > 1 or number < len(self.tasks):
            # zmien done na true
            self.tasks[number - 1].done = True
        else:
           raise ValueError("Zły numer zadania")
    def remove(self):
        #skonczyc
        pass


todolist = TodoList()

todolist.add("nauczyć sie pythona")
todolist.show()
