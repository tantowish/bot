import tkinter as tk
import autoLogin
def submit():
    # get the username and password values
    username = entry_username.get()
    password = entry_password.get()
    window.destroy()
    print(username,password)
    autoLogin.main(username,password)
    

# create a new tkinter window
window = tk.Tk()
window.title("Login masbro")
window.geometry("400x300")

# create username label and entry widget
label_username = tk.Label(window, text="Username:")
label_username.grid(row=0, column=0)
entry_username = tk.Entry(window)
entry_username.grid(row=0, column=1)

# create password label and entry widget
label_password = tk.Label(window, text="Password:")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(window, show="*")
entry_password.grid(row=1, column=1)

# create submit button
button_submit = tk.Button(window, text="Submit", command=submit)
button_submit.grid(row=2, column=0, columnspan=2)

# centering
button_submit.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
entry_password.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
entry_username.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
label_username.place(relx=0.416, rely=0.23, anchor=tk.CENTER)
label_password.place(relx=0.416, rely=0.43, anchor=tk.CENTER)

# run the tkinter event loop
window.mainloop()