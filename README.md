# Braille Text Translator

A Python project that converts text into Braille, prints it in a readable format, and visualizes it using Turtle graphics.

🔗 GitHub Repository: https://github.com/sunlitstorm/braille-text-analysis

This project includes:
- Letter, number, punctuation, and Grade 2 Braille support
- Text-to-Braille translation
- Console output formatting
- Turtle-based visual Braille rendering
- Number handling with Braille number sign (#)

---

## Features

### 1. Braille Dictionary
Maps:
- Letters (a–z)
- Common contractions (e.g., "but", "can", "like")
- Punctuation
- Numbers (via number sign system)

### 2. Text Translator
Converts a sentence into a nested Braille structure that can be:
- Printed in text form
- Drawn visually using Turtle graphics

### 3. Braille Printer
Outputs Braille in aligned rows for readability in the terminal.

### 4. Turtle Graphics Renderer
Draws each Braille character as a 6-dot cell using Python Turtle.

### 5. Number Handling
Automatically inserts a number sign (`#`) before digit sequences so numbers are correctly interpreted in Braille.

---

## How It Works

1. Input a sentence  
2. Preprocess numbers (`handle_special_braille`)  
3. Convert text into Braille (`translator`)  
4. Output:
   - Printed Braille (`print_braille`)
   - Visual Braille (`draw_word`)

---

## Example

```python
sentence = "Every 7 computers, 2 students!"
sentence = handle_special_braille(sentence.lower(), braille_dictionary)

lst = translator(sentence, braille_dictionary)

print_braille(lst)
draw_word(lst)
