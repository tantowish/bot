import tkinter as tk

def main():
    def ya():
        window.destroy()
        import gui

    def eksit():
        window.destroy()

    window = tk.Tk()
    window.title("Login masbro")
    window.geometry("300x350")
    button_reOpen = tk.Button(window, text="ulangi program",command=ya)
    button_exit = tk.Button(window, text="exit",command=eksit)
    button_reOpen.grid(row=0, column=0, columnspan=2)
    button_exit.grid(row=1, column=0, columnspan=2)
    
    button_reOpen.place(relx=0.5, rely=0.38, anchor=tk.CENTER)
    button_exit.place(relx=0.5, rely=0.53, anchor=tk.CENTER)
    
    window.mainloop()