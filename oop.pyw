import tkinter

class NewPet:
    def __init__(self, master):
        self.master = master
        self.frame = tkinter.Frame(self.master)

        self.label = tkinter.Label(self.frame, text="Создание питомца", font="Helvetica 16")

        self.prompt1 = tkinter.Label(self.frame, text="Назовите своего питомца")
        self.entry1 = tkinter.Entry(self.frame)
        
        self.prompt2 = tkinter.Label(self.frame, text="Введите его возраст")
        self.entry2 = tkinter.Entry(self.frame)

        v = tkinter.StringVar()
        v.set("black")
        
        self.prompt3 = tkinter.Label(self.frame, text="Выберите цвет")
        self.color1 = tkinter.Radiobutton(self.frame, text="Чёрный", variable=v, value="black")
        self.color2 = tkinter.Radiobutton(self.frame, text="Рыжий", variable=v, value="red")
        self.color3 = tkinter.Radiobutton(self.frame, text="Белый", variable=v, value="white")
        
        self.submit = tkinter.Button(self.frame, text="Сохранить", command=self.save_pet)

        self.view = tkinter.Button(self.frame, text="Просмотреть", command=self.new_window)

        self.label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.prompt1.grid(row=1, column=0, padx=5, pady=5)
        self.entry1.grid(row=1, column=1, padx=5, pady=5)
        
        self.prompt2.grid(row=2, column=0, padx=5, pady=5)
        self.entry2.grid(row=2, column=1, padx=5, pady=5)
        
        self.prompt3.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.color1.grid(row=4, column=0, columnspan=2)
        self.color2.grid(row=5, column=0, columnspan=2)
        self.color3.grid(row=6, column=0, columnspan=2)
        
        self.submit.grid(row=7, column=0, padx=5, pady=10, sticky='nesw')

        self.view.grid(row=7, column=1, padx=5, pady=10, sticky='nesw')

        self.frame.grid(row=0, column=0)

    def save_pet(self):
        pass

    def new_window(self):
        self.new_window = tkinter.Toplevel(self.master)
        self.new_window.title("Просмотр питомца")
        self.app = PetShow(self.new_window)

class PetShow:
    def __init__(self, master):
        self.master = master
        self.frame = tkinter.Frame(self.master)
        
        self.open = tkinter.Button(self.frame, text="Открыть", command=self.open_file)

        self.open.grid(row=0, column=0, padx=5, pady=5)
        self.frame.grid(row=0, column=0)

    def open_file(self):
        pass

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Создание питомца")
    app = NewPet(root)
    root.mainloop()
