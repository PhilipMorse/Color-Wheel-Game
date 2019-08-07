import tkinter as tk


class WheelCanvas:
    def __init__(self, master, answers):
        self.master = master
        self.answers = answers
        self.frame = tk.Frame(self.master)
        self.button_correct = tk.Button(self.master, text="Correct", command=self.correct)
        self.button_incorrect = tk.Button(self.master, text="Incorrect", command=self.incorrect)
        self.canvas = tk.Canvas(width=500, height=500, bg='black')
        self.button_correct.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.button_incorrect.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
        self.canvas.grid(row=1, columnspan=2)

    def correct(self):
        self.answers.append("green")
        self.draw()

    def incorrect(self):
        self.answers.append("red")
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        size = len(self.answers)
        if size == 1:
            self.canvas.create_oval((100, 100, 400, 400), fill=self.answers[0])
        else:
            for i in range(size):
                self.canvas.create_arc((100, 100, 400, 400), fill=self.answers[i],
                                       start=360 * i / size,
                                       extent=360 / size)


if __name__ == '__main__':
    answers = []
    root = tk.Tk()
    canvas = WheelCanvas(root, answers)
    root.resizable(False, False)
    root.mainloop()
