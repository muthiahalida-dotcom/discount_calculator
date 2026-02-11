import tkinter as tk
from tkinter import messagebox

class DiscountCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Discount Calculator")
        self.root.geometry("350x260")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="Original Price").grid(row=0, column=0, padx=10, pady=8, sticky="w")
        tk.Label(self.root, text="Quantity").grid(row=1, column=0, padx=10, pady=8, sticky="w")
        tk.Label(self.root, text="Discount (%)").grid(row=2, column=0, padx=10, pady=8, sticky="w")

        # Entry fields
        self.price_entry = tk.Entry(self.root)
        self.quantity_entry = tk.Entry(self.root)
        self.discount_entry = tk.Entry(self.root)

        self.price_entry.grid(row=0, column=1, padx=10)
        self.quantity_entry.grid(row=1, column=1, padx=10)
        self.discount_entry.grid(row=2, column=1, padx=10)

        # Button
        calculate_btn = tk.Button(
            self.root,
            text="Calculate",
            command=self.calculate_price
        )
        calculate_btn.grid(row=3, column=0, columnspan=2, pady=15)

        # Result
        self.result_var = tk.StringVar(value="Final Price: -")
        result_label = tk.Label(
            self.root,
            textvariable=self.result_var,
            font=("Arial", 11, "bold")
        )
        result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_price(self):
        try:
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
            discount = float(self.discount_entry.get())

            if price < 0 or quantity <= 0:
                raise ValueError("Price and quantity must be positive.")

            if discount < 0 or discount > 100:
                raise ValueError("Discount must be between 0 and 100.")

            total = price * quantity
            final_price = total - (total * discount / 100)

            self.result_var.set(f"Final Price: {final_price:.2f}")

        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = DiscountCalculatorApp(root)
    root.mainloop()