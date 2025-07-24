import tkinter as tk  # Tkinter кітапханасын қосамыз

root = tk.Tk()
root.title("Label Мысалы")  # Терезе атауы
root.geometry("300x200")  # Өлшемі

label = tk.Label(root, text="Сәлем, Tkinter!")  # Label виджетін құрамыз
label.pack()  # Label-ді терезеге қосамыз

root.mainloop()  # Терезені ашық ұстаймыз