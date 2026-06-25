# Braille Accessibility System

An accessibility-focused project exploring how written language can be represented and experienced through multiple modalities: visual Braille, structured encoding, and audio output.

The project began as a rule-based Braille translation engine in Python and evolved into a web-based interactive system with real-time Braille visualization and text-to-speech functionality.

---

## Overview

This project investigates how natural language can be transformed into alternative accessible formats. It combines algorithmic text processing with interactive user interfaces to support multiple ways of engaging with written content.

The system is designed around three layers:

- A core Braille translation engine (Python)
- A web-based interactive prototype (HTML/CSS/JavaScript)
- A final integrated accessibility interface (portfolio implementation)

---

## Features

### Braille Translation Engine (Python)
- Rule-based encoding system mapping English text to Braille
- Support for:
  - Letters (a–z)
  - Numbers with number sign handling
  - Punctuation
  - Common contractions (Grade 1 / partial Grade 2 support)
- Preprocessing pipeline for handling numeric sequences
- Text-based Braille output formatting
- Turtle graphics visualization of Braille cells

---

### Web Prototype (HTML / CSS / JavaScript)
- Real-time Braille toggle system
- DOM-based text transformation
- Interactive UI for switching between English and Braille views
- Early exploration of accessibility-focused interface design

---

### Portfolio Integration
- Braille view toggle embedded in personal portfolio website
- Text-to-speech functionality using the browser Speech Synthesis API
- Selectable text reading for user-controlled accessibility
- Multi-modal interaction (visual + auditory + structural)

---

## Tech Stack

**Python**
- Core logic and translation engine
- Turtle graphics for visualization

**Frontend**
- HTML
- CSS
- JavaScript (DOM manipulation, event handling)

**Web APIs**
- SpeechSynthesis API (text-to-speech)

---

