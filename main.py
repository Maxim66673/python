import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import random

def generate_file():
    """Создает новый текстовый файл с заданным количеством случайных чисел."""
    try:
        count = int(number_entry.get())
        if count <= 0:
            raise ValueError("Количество чисел должно быть больше нуля.")
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filepath:
            with open(filepath, "w") as file:
                for _ in range(count):
                    file.write(str(random.randint(1, 100)) + "\n")
            messagebox.showinfo("Успех", f"Файл '{filepath}' создан с {count} случайных чисел.")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))


def read_and_calculate(filepath):
    """Читает текстовый файл с числами, вычисляет среднее и выводит результат."""
    try:
        with open(filepath, "r") as file:
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
            if not numbers:
                raise ValueError("Файл пуст или содержит нечисловые данные.")
            avg = sum(numbers) / len(numbers)
            result_text = f"Содержимое файла:\n{numbers}\n\nСреднее значение: {avg:.2f}"
            result_label.config(text=result_text, wraplength=300)

    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл не найден.")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла непредвиденная ошибка: {e}")


def read_file():
    """Открывает диалоговое окно для выбора файла и вычисляет среднее значение."""
    filepath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filepath:
        read_and_calculate(filepath)



root = tk.Tk()
root.title("Обработка данных")
root.geometry("450x600")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=10, font=("Arial", 12), background="#4CAF50", foreground="white")
style.map("TButton", background=[("active", "#45a049")])
style.configure("TLabel", font=("Arial", 12), padding=5)
style.configure("TEntry", font=("Arial", 12), padding=5, borderwidth=2, relief="solid")

result_frame = ttk.LabelFrame(root, text="Результат", padding=10, style="TLabelframe")
result_label = ttk.Label(result_frame, text="", wraplength=400, justify="left", font=("Arial", 10))
result_label.pack(pady=10)
result_frame.grid(row=10, column=0, columnspan=2, sticky="nsew", pady=10)

number_label = ttk.Label(root, text="Кол-во случайных чисел:", style="TLabel")
number_label.grid(row=0, column=0, padx=10, pady=(20, 5), sticky="w")

number_entry = ttk.Entry(root, width=20, style="TEntry")
number_entry.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="e")

generate_button = ttk.Button(root, text="Создать файл", command=generate_file, style="TButton")
generate_button.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")

read_button = ttk.Button(root, text="Открыть файл", command=read_file, style="TButton")
read_button.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")

number_value = ttk.Label(root, text="Введите два числа:", style="TLabel")
number_value.grid(row=3, column=0, columnspan=2, pady=(15,5), sticky="w")

a_value = ttk.Entry(root, width=20, style="TEntry")
a_value.grid(row=4, column=0, padx=10, pady=5, sticky="e")
b_value = ttk.Entry(root, width=20, style="TEntry")
b_value.grid(row=4, column=1, padx=10, pady=5, sticky="e")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.mainloop()