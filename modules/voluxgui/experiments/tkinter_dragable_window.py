import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.floater = FloatingWindow(self, init_x=100, init_y=100)
        self.floater2 = FloatingWindow(self, init_x=100, init_y=200)


class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, init_x=100, init_y=100, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)
        self.geometry("+%s+%s" % (init_x, init_y))

        self.label = tk.Label(self, text="Click on the grip to move")
        self.grip = tk.Label(self, bitmap="gray25")
        self.grip.pack(side="left", fill="y")
        self.label.pack(side="right", fill="both", expand=True)

        self.grip.bind("<ButtonPress-1>", self.StartMove)
        self.grip.bind("<ButtonRelease-1>", self.StopMove)
        self.grip.bind("<B1-Motion>", self.OnMotion)

    def StartMove(self, event):
        print("start move")
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        print("stop move")
        self.x = None
        self.y = None

    def OnMotion(self, event):
        print("on motion")
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x, y))


app = App()
app.mainloop()
