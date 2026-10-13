# French–English Flashcards

A small desktop flashcard app built with Python and Tkinter. It displays a French word, then flips the card to show its English translation after three seconds. Mark a word as known to remove it from future practice; choose the cross to keep it in the study list and move on.

## Requirements

- Python 3
- `pandas`
- Tkinter (usually included with Python; on some Linux distributions it must be installed separately, for example via the system package `python3-tk`)

## Run the app

From this project directory, install pandas if needed and start the application:

```bash
python -m pip install pandas
python main.py
```

On systems where Python 3 is invoked as `python3`, use `python3` in place of `python`.

## How progress is saved

The app loads its study list from `data/words_to_learn.csv` when that file exists. If it does not, the app starts with `data/french_words.csv`. Clicking the checkmark removes the current card from the in-memory list and saves the remaining cards to `data/words_to_learn.csv`. Clicking the cross skips the card without removing it.

To reset progress, delete `data/words_to_learn.csv`; the next launch will load the original word list again. The source CSV files use the columns `French` and `English`.

## Project structure

- `main.py` — Tkinter application and flashcard logic
- `data/french_words.csv` — original French–English word list
- `data/words_to_learn.csv` — saved list of cards still to learn
- `images/` — card backgrounds and answer buttons
