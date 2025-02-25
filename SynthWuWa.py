import tkinter as tk
from tkinter import messagebox
import os

def synthesize_items(A, B, C, D):
    C += D // 3
    D %= 3

    B += C // 3
    C %= 3

    A += B // 3
    B %= 3

    return A, B, C, D

def load_from_file():
    if os.path.exists("item_counts.txt"):
        with open("item_counts.txt", "r") as file:
            try:
                data = file.readline().strip().split(", ")
                values = [int(item.split(": ")[1]) for item in data]
                return values if len(values) == 4 else [0, 0, 0, 0]
            except:
                return [0, 0, 0, 0]
    return [0, 0, 0, 0]

def update_counts():
    global A, B, C, D
    try:
        new_A = int(entry_A.get())
        new_B = int(entry_B.get())
        new_C = int(entry_C.get())
        new_D = int(entry_D.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers")
        return

    new_A, new_B, new_C, new_D = synthesize_items(new_A, new_B, new_C, new_D)

    label_result.config(text=f"A: {new_A}, B: {new_B}, C: {new_C}, D: {new_D}")

def apply_changes():
    global A, B, C, D
    try:
        A = int(entry_A.get())
        B = int(entry_B.get())
        C = int(entry_C.get())
        D = int(entry_D.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers")
        return

    label_result.config(text=f"A: {A}, B: {B}, C: {C}, D: {D}")

def reset_inputs():
    entry_A.delete(0, tk.END)
    entry_B.delete(0, tk.END)
    entry_C.delete(0, tk.END)
    entry_D.delete(0, tk.END)

def edit_counts():
    entry_A.delete(0, tk.END)
    entry_A.insert(0, str(A))
    entry_B.delete(0, tk.END)
    entry_B.insert(0, str(B))
    entry_C.delete(0, tk.END)
    entry_C.insert(0, str(C))
    entry_D.delete(0, tk.END)
    entry_D.insert(0, str(D))

def save_to_file():
    with open("item_counts.txt", "w") as file:
        file.write(f"A: {A}, B: {B}, C: {C}, D: {D}\n")
    messagebox.showinfo("Save", "Counts saved to item_counts.txt")

def main():
    global A, B, C, D, entry_A, entry_B, entry_C, entry_D, label_result
    A, B, C, D = load_from_file()

    root = tk.Tk()
    root.title("Item Synthesizer")

    tk.Label(root, text="Enter the number of A items:").grid(row=0, column=0, padx=5, pady=5)
    entry_A = tk.Entry(root)
    entry_A.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Enter the number of B items:").grid(row=1, column=0, padx=5, pady=5)
    entry_B = tk.Entry(root)
    entry_B.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Enter the number of C items:").grid(row=2, column=0, padx=5, pady=5)
    entry_C = tk.Entry(root)
    entry_C.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="Enter the number of D items:").grid(row=3, column=0, padx=5, pady=5)
    entry_D = tk.Entry(root)
    entry_D.grid(row=3, column=1, padx=5, pady=5)

    button_frame = tk.Frame(root)
    button_frame.grid(row=4, column=0, columnspan=2, pady=10)

    tk.Button(button_frame, text="Update Counts", command=update_counts, width=15).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(button_frame, text="Apply Changes", command=apply_changes, width=15).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(button_frame, text="Edit Previous", command=edit_counts, width=15).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(button_frame, text="Save to File", command=save_to_file, width=15).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(button_frame, text="Reset Inputs", command=reset_inputs, width=15).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    label_result = tk.Label(root, text=f"A: {A}, B: {B}, C: {C}, D: {D}", font=("Arial", 12, "bold"))
    label_result.grid(row=5, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()