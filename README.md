# ATR Calculator

**Python / Tkinter · Desktop utility · Trading**

A compact desktop calculator for estimating the **average candle range over five periods**. Created as a personal tool while studying trading and market volatility.

> **Calculation note:** the current implementation averages `High − Low` for five candles. Although the interface calls the result `ATR(5)`, it does **not** implement the canonical Average True Range (True Range also considers the previous candle's Close). No trading signals or investment recommendations are generated.

## What it does

- Provides five rows for candle High and Low prices.
- Validates missing inputs and rejects `Low > High`.
- Accepts either a comma or a dot as the decimal separator.
- Displays the calculated average to four decimal places and lists individual ranges.
- Includes demo values, clear/reset controls, and a custom dark Tkinter theme.

## Formula

For the five entered candles:

```text
Range[i] = High[i] - Low[i]
Displayed average = (Range[1] + ... + Range[5]) / 5
```

With the bundled demo data, the ranges are `6, 8, 5, 3, 6`, giving **5.6000**.

## Run locally

Requires Python 3 with Tkinter support (included in standard Windows Python installations).

```bash
python atr_gui.py
```

There are no third-party Python imports in the application. The repository also contains `atr_gui.spec` for a PyInstaller Windows build. If you want to rebuild the executable:

```bash
python -m pip install pyinstaller
pyinstaller atr_gui.spec
```

## Repository structure

| File / folder | Purpose |
| --- | --- |
| `atr_gui.py` | GUI, input validation, demo inputs, and calculation |
| `atr_gui.spec` | PyInstaller build configuration |
| `dist/` | Previously generated Windows executable |
| `build/` | Generated PyInstaller build intermediates; not needed to read the source |

## Scope and possible improvements

This is a focused learning/utility project, not an analytical platform. Future improvements could include a canonical ATR based on previous Close, a selectable period, a separated calculation module, and unit tests.

---

Part of [Daniil Goncharov's portfolio](https://goncharov-code.ru/) · [GitHub profile](https://github.com/davins526).
