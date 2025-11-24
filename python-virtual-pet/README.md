# python-virtual-pet

A cute and interactive virtual pet game built with Python and Tkinter. Name your pet, take care of its hunger, happiness, and energy levels, and enjoy a pastel pink themed GUI with adorable pet images and sounds.

---

## Features

- Name your pet with a custom or default name.
- Visual status bars for Hunger, Happiness, and Energy.
- Interactive buttons to Feed, Play, and Put your pet to Sleep.
- Background music and sound effects using pygame.
- Pastel pink, user-friendly GUI with pet image display.
- Automatic pet status updates every 5 seconds.
- Alerts if pet’s status becomes critical.

---

## How It Works

- On launch, the app asks you to name your pet.
- Displays your pet’s image and status bars.
- Buttons allow you to feed, play, or put your pet to sleep, affecting its stats.
- Stats automatically increase or decrease over time to simulate pet needs.
- If hunger gets too high or happiness/energy too low, the game ends with a message.
- Background music plays continuously to enhance the experience.

---

## Installation

### Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Pygame

### Install pygame

```bash
pip install pygame
```

### Assets

- Place `pet.png` (pet image) in the same folder as the script.
- Place `pet_sound.mp3` (background music) in the same folder as the script.

---

## Usage

Run the virtual pet app:

```bash
python virtual_pet.py
```

- Enter a name for your pet or accept the default.
- Use the buttons to interact with your pet.
- Monitor pet’s hunger, happiness, and energy bars.
- Close the window or follow prompts to exit.

---

## Code Overview

- Uses Tkinter for GUI elements: labels, buttons, progress bars.
- Uses `pygame.mixer` for background music playback.
- Pet stats are managed with `ttk.Progressbar` widgets.
- The pet’s status updates every 5 seconds via `root.after()`.
- Button commands modify the pet’s stats accordingly.
- Error handling for missing pet image.

---

## Project Structure

```
python-virtual-pet/
├── virtual_pet.py       # Main application script
├── pet.png              # Pet image file
├── pet_sound.mp3        # Background music file
└── README.md            # This file
```

---

## Contact

Created by Heaven (GitHub: [nerdyalgorithm](https://github.com/nerdyalgorithm)).

---

## References

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Pygame Mixer Documentation](https://www.pygame.org/docs/ref/mixer.html)
- Tutorials on building virtual pets with Python and Tkinter

---

Enjoy caring for your adorable virtual pet!
