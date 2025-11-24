# Calculator

A cute and compact GUI calculator built with Python's Tkinter library. It supports basic arithmetic operations, parentheses, and percentage calculations, all wrapped in a pink-themed interface.

---

## Features

- Basic arithmetic: addition, subtraction, multiplication, division.
- Parentheses support with automatic multiplication insertion.
- Percentage calculations handled by converting `%` to division by 100.
- Clear (`C`) button to reset the input.
- User-friendly pink-themed interface with large buttons.
- Error handling for invalid expressions.

---

## How It Works

- The calculator displays an input field where expressions are typed or constructed by clicking buttons.
- Clicking buttons appends their value to the display.
- Pressing `=` evaluates the expression using Python's `eval()` function.
- The `%` symbol is internally converted to `/100` to handle percentages.
- If the expression is invalid, the display shows `"Error"`.
- Parentheses insertion intelligently adds a multiplication sign if needed (e.g., `2(` becomes `2*(`).

---

## Installation

### Requirements

- Python 3.x (Tkinter is included by default)
  
No additional packages are required.

---

## Usage

Run the script:

```bash
python calculator.py
```

- Click buttons to build your expression.
- Press `=` to calculate the result.
- Use `C` to clear the display.
- Supports decimal points and parentheses.

---

## Code Overview

- Uses Tkinter `Entry` widget for the display.
- Buttons are arranged in a grid layout.
- Button clicks are handled by a single function `on_click()` that updates or evaluates the expression.
- The GUI uses pink color schemes for a cute aesthetic.

---

## Example Button Layout

| ( | ) | % | C |
|---|---|---|---|
| 7 | 8 | 9 | / |
| 4 | 5 | 6 | * |
| 1 | 2 | 3 | - |
| 0 | . | = | + |

---

## Contact

Created by Heaven (GitHub: [nerdyalgorithm](https://github.com/nerdyalgorithm)).

---

Enjoy your cute pink calculator!
