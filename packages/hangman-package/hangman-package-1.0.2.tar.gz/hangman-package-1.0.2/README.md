# Hangman Package

The Hangman package is a Python implementation of the classic game, Hangman. It allows users to play the game by guessing letters to complete a hidden word.

## Installation

The package can be installed using pip:

```bash
pip install hangman-package
```

## Usage

The package can be used in the following way:

```python
from hangman import Hangman

# Create a new instance of Hangman
hangman = Hangman()

# Start the game
hangman.play()
```

You can pass a list of strings to utilize custom words:
```python
from hangman import Hangman

words = ["banana", "orange", "apple", "grape", "strawberry", "lemon", "watermelon"]

# Create a new instance of Hangman with custom words
hangman = Hangman(words=words)

# Start the game
hangman.play()
```

When `play()` is called, the game will begin and the user will be prompted to guess letters to complete the hidden word. The game ends when the user either completes the word or runs out of guesses.

## Contributing

Contributions to the Hangman package are welcome! If you encounter a bug or have a feature request, please open an issue on the [GitHub repository](https://github.com/viniciusenari/hangman-package).

If you would like to contribute to the package, please fork the repository and submit a pull request with your changes.

## License

The Hangman package is open-source software licensed under the [MIT license](https://opensource.org/licenses/MIT).
