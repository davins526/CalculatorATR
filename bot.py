import tkinter as tk

def calculate_atr():
    try:
        ranges = []
        for i in range(5):
            high = float(high_entries[i].get())
            low = float(low_entries[i].get())
            ranges.append(high - low)

        atr = sum(ranges) / len(ranges)
        result_label.config(text=f"ATR(5) = {atr:.4f}")

    except:
        result_label.config(text="Ошибка ввода")

root = tk.Tk()
root.title("ATR Calculator")
root.geometry("300x250")

high_entries = []
low_entries = []

tk.Label(root, text="High").grid(row=0, column=1)
tk.Label(root, text="Low").grid(row=0, column=2)

for i in range(5):
    tk.Label(root, text=f"Candle {i+1}").grid(row=i+1, column=0)

    high_entry = tk.Entry(root)
    high_entry.grid(row=i+1, column=1)
    high_entries.append(high_entry)

    low_entry = tk.Entry(root)
    low_entry.grid(row=i+1, column=2)
    low_entries.append(low_entry)

calc_button = tk.Button(root, text="Calculate ATR", command=calculate_atr)
calc_button.grid(row=6, column=0, columnspan=3, pady=10)

result_label = tk.Label(root, text="ATR(5) = ")
result_label.grid(row=7, column=0, columnspan=3)

root.mainloop()