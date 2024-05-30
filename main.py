import tkinter as tk

def convert_currency():
    try:
        npr_amount = float(entry_npr.get())
        inr_amount = npr_amount * npr_to_inr_rate
        label_result.config(text=f"Equivalent amount in INR: {inr_amount:.2f} INR")
    except ValueError:
        label_result.config(text="Invalid input. Please enter a valid number.")


npr_to_inr_rate = 1.60  # 1 NPR = 1.60 INR

root = tk.Tk()
root.title("NPR to INR Currency Converter")

label_npr = tk.Label(root, text="Nepali Rupees (NPR):")
label_npr.grid(row=0, column=0, padx=10, pady=10)

entry_npr = tk.Entry(root)
entry_npr.grid(row=0, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=1, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
