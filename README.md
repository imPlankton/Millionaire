# Millionaire Game

A simple command-line quiz game written in Python, inspired by *Who Wants to Be a Millionaire?*.

## Features

### Gameplay

* 15 multiple-choice questions
* 4 answer options for each question
* Increasing prize pool after each correct answer
* Game ends immediately on a wrong answer
* Final goal: win $1,000,000

### Mechanics

* Input validation (handles non-numeric input)
* Displays correct answer if the player loses
* Progressive difficulty through question order

## How to run

Clone the repository:

```bash
git clone https://github.com/imPlankton/millionaire
```

Go to the project folder:

```bash
cd millionaire
```

Run the program:

```bash
python main.py
```

## Notes

* Answers are entered as numbers:

  * 1 → a
  * 2 → b
  * 3 → c
  * 4 → d
* The game ends after the first incorrect answer
* Prize increases with each correct answer

## Example

```text
Which piece checkmates in Legal's checkmate?
a. King
b. Rook
c. Knight
d. Bishop

Enter your answer: 3
Great! That's the right answer!
Your prizepool right now is 500$
```

## Future improvements

* Add lifelines (50/50, ask the audience)
* Add checkpoints (safe money levels)
* Shuffle questions
* Add timer for each question
* Create a GUI version
