# Flask Number Guessing Game

This project is a simple web application built using the Flask framework in Python. It demonstrates the basics of setting up a Flask application and uses Flask decorators to define different routes for handling HTTP requests. The project also incorporates basic HTML and CSS styling to create an interactive user interface. 

## Project Overview

The Flask Number Guessing Game is a fun and interactive game where the user tries to guess a randomly generated number between 0 and 9. The application provides feedback on whether the guessed number is too high, too low, or correct. Each guess is handled through a different route, making use of Flask's powerful routing capabilities.

## Features

- A simple user interface to interact with the number guessing game.
- Random number generation for a new game each time the server is restarted.
- Feedback to the user if their guess is too high, too low, or correct.
- Use of Flask decorators to handle routing.
- Basic HTML and CSS for page layout and styling.
- Display of relevant GIFs based on the user's guess.

## How to Run the Project

1. **Install Flask**: Make sure you have Flask installed in your Python environment. You can install it using pip:
    ```bash
    pip install Flask
    ```

2. **Run the Application**: Execute the following command in your terminal to start the Flask development server:
    ```bash
    python app.py
    ```

3. **Open in Browser**: Navigate to `http://127.0.0.1:5000/` in your web browser to start playing the game.

## Code Explanation

Below is a brief explanation of the main components of the code:

### Importing Required Libraries

```python
from flask import Flask
import random
