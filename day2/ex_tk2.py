from tkinter import *


class MoveBall:
    def __init__(self, app):
        self.canvas = Canvas(app, width=400, height=300)
        self.canvas.pack()
        self.app = app
        self.deltax = 2
        self.deltay = 2
        self.canvas.create_oval(100, 150, 150, 200, fill='red', tags='redBall')
        self.canvas.pack()

    def fn_move_left(self, event):
        self.canvas.move('redBall', -self.deltax, 0)
        self.canvas.after(20)
        self.canvas.update()

    def fn_move_right(self, event):
        self.canvas.move('redBall', self.deltax, 0)
        self.canvas.after(20)
        self.canvas.update()


app = Tk()
mov = MoveBall(app)
mov.canvas.bind('<Left>', mov.fn_move_left)
mov.canvas.bind('<Right>', mov.fn_move_right)
mov.canvas.focus_set()
mov.canvas.pack()
app.mainloop()
