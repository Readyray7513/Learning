class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f'Removed: {removed['task']}')
        else:
            print('Invalid task number')

    def toggle_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = not self.tasks[index]['completed']
            status = 'completed' if self.tasks[index]['completed'] else 'uncompleted'
            print(f'Marked task {index + 1} as {status}')
        else:
            print('Invalid task number')

    def show_tasks(self):
        if not self.tasks:
            print('No tasks!')
            return
        for i, task in enumerate(self.tasks):
            status = '/' if task['completed'] else ' '
            print(f'{i + 1}. [{status}] {task['task']}')

def main():
     todo = TodoList()
     while True:
        print('\n=== TODO LIST ===')
        print('1. Add task')
        print('2. Remove task')
        print('3. Toggle completion')
        print('4. Show tasks')
        print('5. Quit')

        choice = input('choose an option (1-5): ') 
        if choice == '1':
            task = input('Enter task: ')
            todo.add_task(task)
        elif choice == '2':
            todo.show_tasks()
            index = int(input('Enter task number to remove: ')) - 1
            todo.remove_task(index)
        elif choice == '3':
            todo.show_tasks()
            index = int(input('Enter task number to toggle: ')) - 1
            todo.toggle_complete(index)
        elif choice == '4':
            todo.show_tasks()
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice')
    
if __name__ == '__main__':
    main()


