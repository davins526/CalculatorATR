import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass
from typing import List


@dataclass
class Theme:
    bg: str = "#1f232a"
    panel: str = "#2a2f38"
    panel_alt: str = "#323844"
    text: str = "#e6eaf2"
    muted: str = "#aab3c2"
    accent: str = "#5b8cff"
    accent_hover: str = "#78a0ff"
    border: str = "#404857"
    input_bg: str = "#171b21"
    success: str = "#7bd88f"
    error: str = "#ff7a7a"


THEME = Theme()


class ATRApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("ATR Calculator")
        self.geometry("520x430")
        self.minsize(500, 410)
        self.configure(bg=THEME.bg)

        self.high_entries: List[tk.Entry] = []
        self.low_entries: List[tk.Entry] = []
        self.result_var = tk.StringVar(value="ATR(5) = —")
        self.status_var = tk.StringVar(value="Введи High и Low для 5 свечей")

        self._configure_styles()
        self._build_ui()
        self._fill_demo_data()

    def _configure_styles(self) -> None:
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Title.TLabel",
            background=THEME.bg,
            foreground=THEME.text,
            font=("Segoe UI", 18, "bold"),
        )
        style.configure(
            "Subtitle.TLabel",
            background=THEME.bg,
            foreground=THEME.muted,
            font=("Segoe UI", 10),
        )
        style.configure(
            "Header.TLabel",
            background=THEME.panel,
            foreground=THEME.text,
            font=("Segoe UI", 10, "bold"),
        )
        style.configure(
            "Row.TLabel",
            background=THEME.panel,
            foreground=THEME.text,
            font=("Segoe UI", 10),
        )
        style.configure(
            "Result.TLabel",
            background=THEME.panel_alt,
            foreground=THEME.success,
            font=("Segoe UI", 16, "bold"),
        )
        style.configure(
            "Status.TLabel",
            background=THEME.bg,
            foreground=THEME.muted,
            font=("Segoe UI", 9),
        )
        style.configure(
            "Primary.TButton",
            background=THEME.accent,
            foreground="#ffffff",
            borderwidth=0,
            focusthickness=0,
            focuscolor=THEME.accent,
            font=("Segoe UI", 10, "bold"),
            padding=(12, 8),
        )
        style.map(
            "Primary.TButton",
            background=[("active", THEME.accent_hover)],
            foreground=[("disabled", "#c8d0de")],
        )
        style.configure(
            "Secondary.TButton",
            background=THEME.panel_alt,
            foreground=THEME.text,
            borderwidth=0,
            focusthickness=0,
            focuscolor=THEME.panel_alt,
            font=("Segoe UI", 10),
            padding=(12, 8),
        )
        style.map(
            "Secondary.TButton",
            background=[("active", THEME.border)],
        )

    def _build_ui(self) -> None:
        outer = tk.Frame(self, bg=THEME.bg, padx=18, pady=18)
        outer.pack(fill="both", expand=True)

        ttk.Label(outer, text="ATR Calculator", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            outer,
            text="Введи High и Low для 5 свечей. ATR считается как средний диапазон (High - Low).",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(4, 14))

        card = tk.Frame(
            outer,
            bg=THEME.panel,
            highlightbackground=THEME.border,
            highlightthickness=1,
            bd=0,
        )
        card.pack(fill="x")

        header = tk.Frame(card, bg=THEME.panel)
        header.pack(fill="x", padx=14, pady=(14, 8))

        ttk.Label(header, text="Свеча", style="Header.TLabel").grid(row=0, column=0, sticky="w", padx=(0, 18))
        ttk.Label(header, text="High", style="Header.TLabel").grid(row=0, column=1, sticky="w", padx=(0, 14))
        ttk.Label(header, text="Low", style="Header.TLabel").grid(row=0, column=2, sticky="w")

        table = tk.Frame(card, bg=THEME.panel)
        table.pack(fill="x", padx=14, pady=(0, 8))

        for i in range(5):
            ttk.Label(table, text=f"Свеча {i + 1}", style="Row.TLabel").grid(row=i, column=0, sticky="w", pady=6, padx=(0, 18))

            high_entry = tk.Entry(
                table,
                bg=THEME.input_bg,
                fg=THEME.text,
                insertbackground=THEME.text,
                relief="flat",
                highlightthickness=1,
                highlightbackground=THEME.border,
                highlightcolor=THEME.accent,
                width=14,
                font=("Segoe UI", 10),
            )
            high_entry.grid(row=i, column=1, pady=6, padx=(0, 14), ipady=6)
            self.high_entries.append(high_entry)

            low_entry = tk.Entry(
                table,
                bg=THEME.input_bg,
                fg=THEME.text,
                insertbackground=THEME.text,
                relief="flat",
                highlightthickness=1,
                highlightbackground=THEME.border,
                highlightcolor=THEME.accent,
                width=14,
                font=("Segoe UI", 10),
            )
            low_entry.grid(row=i, column=2, pady=6, ipady=6)
            self.low_entries.append(low_entry)

        result_card = tk.Frame(
            outer,
            bg=THEME.panel_alt,
            highlightbackground=THEME.border,
            highlightthickness=1,
            bd=0,
            padx=16,
            pady=16,
        )
        result_card.pack(fill="x", pady=(14, 12))

        ttk.Label(result_card, textvariable=self.result_var, style="Result.TLabel").pack(anchor="center")

        actions = tk.Frame(outer, bg=THEME.bg)
        actions.pack(fill="x")

        ttk.Button(actions, text="Рассчитать ATR", style="Primary.TButton", command=self.calculate_atr).pack(side="left")
        ttk.Button(actions, text="Очистить", style="Secondary.TButton", command=self.clear_inputs).pack(side="left", padx=(10, 0))
        ttk.Button(actions, text="Демо", style="Secondary.TButton", command=self._fill_demo_data).pack(side="left", padx=(10, 0))

        ttk.Label(outer, textvariable=self.status_var, style="Status.TLabel").pack(anchor="w", pady=(12, 0))

    def _fill_demo_data(self) -> None:
        demo = [
            ("105", "99"),
            ("110", "102"),
            ("108", "103"),
            ("107", "104"),
            ("111", "105"),
        ]
        self.clear_inputs(set_status=False)
        for i, (high, low) in enumerate(demo):
            self.high_entries[i].insert(0, high)
            self.low_entries[i].insert(0, low)
        self.status_var.set("Загружены демо-значения")
        self.result_var.set("ATR(5) = —")

    def clear_inputs(self, set_status: bool = True) -> None:
        for entry in self.high_entries + self.low_entries:
            entry.delete(0, tk.END)
        self.result_var.set("ATR(5) = —")
        if set_status:
            self.status_var.set("Поля очищены")

    def calculate_atr(self) -> None:
        try:
            ranges = []
            for i in range(5):
                high_text = self.high_entries[i].get().strip().replace(",", ".")
                low_text = self.low_entries[i].get().strip().replace(",", ".")

                if not high_text or not low_text:
                    raise ValueError(f"Заполни High и Low для свечи {i + 1}")

                high = float(high_text)
                low = float(low_text)

                if low > high:
                    raise ValueError(f"У свечи {i + 1} Low не может быть больше High")

                ranges.append(high - low)

            atr = sum(ranges) / len(ranges)
            self.result_var.set(f"ATR(5) = {atr:.4f}")
            self.status_var.set(f"Успешно рассчитано. Диапазоны: {', '.join(f'{x:.2f}' for x in ranges)}")
        except ValueError as e:
            self.result_var.set("ATR(5) = —")
            self.status_var.set(str(e))
            messagebox.showerror("Ошибка ввода", str(e))
        except Exception:
            self.result_var.set("ATR(5) = —")
            self.status_var.set("Не удалось рассчитать ATR")
            messagebox.showerror("Ошибка", "Проверь введённые значения")


if __name__ == "__main__":
    app = ATRApp()
    app.mainloop()
