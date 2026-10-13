
from pathlib import Path
from tkinter import PhotoImage, Button, Tk, Canvas
import random
import pandas

data_path = Path(__file__).parent
current_flashcard = {}
to_dict = {}


BACKGROUND_COLOR = "#B1DDC6"

try:
# Randomly select a flashcard from the CSV file and display it on the canvas
    flashcards = pandas.read_csv(data_path / "data" / "words_to_learn.csv")
except FileNotFoundError:
    original_flashcards = pandas.read_csv(data_path / "data" / "french_words.csv")
    print(original_flashcards)
    to_dict = original_flashcards.to_dict(orient="records")
else:
    to_dict = flashcards.to_dict(orient="records")




def next_flashcard():
    global current_flashcard, flip_timer
    window.after_cancel(flip_timer)
    current_flashcard = random.choice(to_dict)
    canvas.itemconfig(title_text, text="French", fill="Black")
    canvas.itemconfig(word_text, text=current_flashcard["French"], fill="Black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_flashcard)

def flip_flashcard():
    canvas.itemconfig(title_text, text="English", fill="White")
    canvas.itemconfig(word_text, text=current_flashcard["English"], fill="White")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_dict.remove(current_flashcard)
    print(to_dict)
    data = pandas.DataFrame(to_dict)
    data.to_csv(data_path / "data" / "words_to_learn.csv", index=False)
    next_flashcard()

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer = window.after(3000, flip_flashcard)

canvas = Canvas(window, width=800, height=526)
card_front_img = PhotoImage(file=data_path / "images" / "card_front.png")
card_back_img = PhotoImage(file=data_path / "images" / "card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)


title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 20, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 40, "bold"))

canvas.configure(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file=data_path / "images" / "wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_flashcard)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=data_path / "images" / "right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)



next_flashcard()

window.mainloop()

