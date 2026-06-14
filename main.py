from turtle import *

"""
Braille Text Analysis System

A rule-based translation system that converts English text into Braille
using a structured dictionary, text rendering, and turtle-based visualization.

Features:
- Grade 1 + Grade 2 Braille support
- Number handling via Braille number sign
- Text rendering output
- Turtle graphics visualization

Developed as an accessibility-focused computing project.
"""

def add_letters(bd):
    """
    Builds a Braille encoding dictionary for:
    - letters (a-z)
    - common Grade 2 contractions
    - punctuation
    - numbers (via number sign + letter mapping)

    The dictionary maps characters to 6-dot Braille patterns.
    """

    bd['a'] = [1, 0, 0, 0, 0, 0]
    bd['b'] = [1, 1, 0, 0, 0, 0]
    bd['c'] = [1, 0, 0, 1, 0, 0]
    bd['d'] = [1, 0, 0, 1, 1, 0]
    bd['e'] = [1, 0, 0, 0, 1, 0]
    bd['f'] = [1, 1, 0, 1, 0, 0]
    bd['g'] = [1, 1, 0, 1, 1, 0]
    bd['h'] = [1, 1, 0, 0, 1, 0]
    bd['i'] = [0, 1, 0, 1, 0, 0]
    bd['j'] = [0, 1, 0, 1, 1, 0]

    bd['k'] = [1, 0, 1, 0, 0, 0]
    bd['l'] = [1, 1, 1, 0, 0, 0]
    bd['m'] = [1, 0, 1, 1, 0, 0]
    bd['n'] = [1, 0, 1, 1, 1, 0]
    bd['o'] = [1, 0, 1, 0, 1, 0]
    bd['p'] = [1, 1, 1, 1, 0, 0]
    bd['q'] = [1, 1, 1, 1, 1, 0]
    bd['r'] = [1, 1, 1, 0, 1, 0]
    bd['s'] = [0, 1, 1, 1, 0, 0]
    bd['t'] = [0, 1, 1, 1, 1, 0]

    bd['u'] = [1, 0, 1, 0, 0, 1]
    bd['v'] = [1, 1, 1, 0, 0, 1]
    bd['w'] = [0, 1, 0, 1, 1, 1]
    bd['x'] = [1, 0, 1, 1, 0, 1]
    bd['y'] = [1, 0, 1, 1, 1, 1]
    bd['z'] = [1, 0, 1, 0, 1, 1]

    # contractions
    bd['but'] = [1, 1, 0, 0, 0, 0]
    bd['can'] = [1, 0, 0, 1, 0, 0]
    bd['do'] = [1, 0, 0, 1, 1, 0]
    bd['every'] = [1, 0, 0, 0, 1, 0]
    bd['from'] = [1, 1, 0, 1, 0, 0]
    bd['go'] = [1, 1, 0, 1, 1, 0]
    bd['have'] = [1, 1, 0, 0, 1, 0]
    bd['just'] = [0, 1, 0, 1, 1, 0]
    bd['knowledge'] = [1, 0, 1, 0, 0, 0]
    bd['like'] = [1, 1, 1, 0, 0, 0]
    bd['more'] = [1, 0, 1, 1, 0, 0]
    bd['not'] = [1, 0, 1, 1, 1, 0]
    bd['people'] = [1, 1, 1, 1, 0, 0]
    bd['quite'] = [1, 1, 1, 1, 1, 0]
    bd['rather'] = [1, 1, 1, 0, 1, 0]
    bd['so'] = [0, 1, 1, 1, 0, 0]
    bd['that'] = [0, 1, 1, 1, 1, 0]
    bd['us'] = [1, 0, 1, 0, 0, 1]
    bd['very'] = [1, 1, 1, 0, 0, 1]
    bd['it'] = [1, 0, 1, 1, 0, 1]
    bd['you'] = [1, 0, 1, 1, 1, 1]
    bd['as'] = [1, 0, 1, 0, 1, 1]
    bd['will'] = [0, 1, 0, 1, 1, 1]

    # punctuation
    bd['.'] = [0, 1, 0, 0, 1, 1]
    bd['?'] = [0, 1, 1, 0, 0, 1]
    bd['!'] = [0, 1, 1, 0, 1, 0]
    bd[','] = [0, 1, 0, 0, 0, 0]
    bd[';'] = [0, 1, 1, 0, 0, 0]
    bd[':'] = [0, 1, 0, 0, 1, 0]

    # number sign
    bd['#'] = [0, 0, 1, 1, 1, 1]

    # numbers map to letters after #
    bd['1'] = bd['a']
    bd['2'] = bd['b']
    bd['3'] = bd['c']
    bd['4'] = bd['d']
    bd['5'] = bd['e']
    bd['6'] = bd['f']
    bd['7'] = bd['g']
    bd['8'] = bd['h']
    bd['9'] = bd['i']
    bd['0'] = bd['j']


# ==============================================================
# Translation Engine
# ==============================================================

def translator(sentence, bd):
    """
    Converts a sentence into a nested Braille representation.
    Handles both full-word contractions and character-by-character translation.
    """

    sentence = sentence.lower()
    words = sentence.split(' ')
    translated = []

    for word in words:

        if word in bd:
            translated.append(bd[word])

        else:
            word_translation = []

            for char in word:
                if char in bd:
                    word_translation.append(bd[char])

            if word_translation:
                translated.append(word_translation)

    return translated


# ==============================================================
# Braille Output (Text)
# ==============================================================

def print_braille(lst):
    """
    Prints Braille output as three aligned rows.
    """

    line1 = ''
    line2 = ''
    line3 = ''

    for item in lst:

        if item and isinstance(item[0], list):

            for next in item:
                line1 += str(next[0]) + ' '
                line2 += str(next[1]) + ' '
                line3 += str(next[2]) + ' '
                line1 += str(next[3]) + ' '
                line2 += str(next[4]) + ' '
                line3 += str(next[5]) + ' '

        else:
            line1 += str(item[0]) + ' '
            line2 += str(item[1]) + ' '
            line3 += str(item[2]) + ' '
            line1 += str(item[3]) + ' '
            line2 += str(item[4]) + ' '
            line3 += str(item[5]) + ' '

    print(line1)
    print(line2)
    print(line3)


# ==============================================================
# Braille Drawing (Turtle Graphics)
# ==============================================================

def draw_word(lst):
    for item in lst:
        if isinstance(item[0], list):
            for next in item:
                draw_braille_character(next)
        else:
            draw_braille_character(item)


def draw_braille_character(bc):
    """
    Draws a single Braille cell using turtle graphics.
    """

    radius = 5
    spacing = 30
    index = 0

    penup()

    for i in range(2):
        for j in range(3):

            if bc[index] == 1:
                pendown()
                begin_fill()
                circle(radius)
                end_fill()
                penup()
            else:
                penup()
                circle(radius)

            right(90)
            forward(spacing)
            left(90)

            index += 1

        left(90)
        forward(spacing * 3)
        right(90)

        if i == 0:
            forward(spacing)

    penup()
    forward(spacing)
    pendown()


# ==============================================================
# Number Handling
# ==============================================================

def handle_special_braille(sentence, bd):
    """
    Inserts a number marker (#) before digit sequences.
    """

    processed = ""
    in_number = False

    for ch in sentence:
        if ch.isdigit():
            if not in_number:
                processed += "#"
                in_number = True
        else:
            in_number = False

        processed += ch

    return processed


# ==============================================================
# Example Usage (Demo)
# ==============================================================

if __name__ == "__main__":

    braille_dictionary = {}
    add_letters(braille_dictionary)

    sentence = "Every 7 computers, 2 students!"
    sentence = handle_special_braille(sentence.lower(), braille_dictionary)

    result = translator(sentence, braille_dictionary)

    print(result)
    print_braille(result)

    draw_word(result)