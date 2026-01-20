# Guess Number Game (Python)

This is a simple console-based **Guess Number Game** developed using Python.  
The player must guess a randomly generated number within a fixed time limit.

---

## 🎮 Game Rules
- The computer randomly selects a number between **1 and 100**
- The player has **15 seconds** to guess the number
- Hints are provided:
  - "Try lesser number" if the guess is too high
  - "Some greater number" if the guess is too low
- If guessed correctly within time:
  - A winning message is displayed
  - A clapping sound is played 🎉
- If time runs out, the correct number is shown

---

## 🛠 Technologies Used
- Python
- Standard Libraries:
  - `random`
  - `time`
  - `sys`
- External Library:
  - `playsound`

---

## 📦 Requirements
Make sure Python is installed on your system.

Install the required module:
```bash
pip install playsound
