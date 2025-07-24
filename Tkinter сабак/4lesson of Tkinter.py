import tkinter as tk  # Tkinter-ді қосамыз

# Батырма басылғанда енгізілген мәтінді алу
def get_text():
    user_input = entry.get()  # Entry-ден мәтінді аламыз
    print(f"Сен жаздың: {user_input}")

root = tk.Tk()
root.title("Entry Мысалы")  # Терезе атауы
root.geometry("300x200")

entry = tk.Entry(root)  # Entry виджетін құрамыз
entry.pack()  # Терезеге қосамыз

button = tk.Button(root, text="Мәтінді алу", command=get_text)
button.pack()

root.mainloop()