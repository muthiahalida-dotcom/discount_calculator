import tkinter as tk
from tkinter import messagebox

def calculate_price():
    try:
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
        discount = float(discount_entry.get())

        if price < 0 or quantity <= 0:
            messagebox.showerror("Error", "Price dan Quantity harus lebih dari 0")
            return

        if discount < 0 or discount > 100:
            messagebox.showerror("Error", "Discount harus antara 0 - 100")
            return

        total = price * quantity
        discount_amount = total * discount / 100
        final_price = total - discount_amount

        result_label.config(text=f"Final Price: {final_price:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid")


root = tk.Tk()
root.title("Discount Calculator")
root.geometry("350x250")

tk.Label(root, text="Original Price").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Label(root, text="Discount (%)").pack()
discount_entry = tk.Entry(root)
discount_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_price)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Final Price: -", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
