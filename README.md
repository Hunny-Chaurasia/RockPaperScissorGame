# RockPaperScissorGame

Tech Stack: Python 3.x using the built-in random module for the bot's decisions. Logic: A continuous while loop normalizes player text (.lower()) for fair matching. It evaluates ties, rules (Rock/Paper/Scissors), updates points, and terminates at 10 points or via exit.

---

## 🎮 Features

*   **Interactive Command-Line Interface:** Easy-to-use text prompts for player moves.
*   **Smart Scoring System:** Tracks points for both the player and the bot in real-time.
*   **Race to 10:** The game automatically concludes and declares a winner once someone reaches 10 points.
*   **Case-Insensitive Input:** Accepts input regardless of capitalization (e.g., "Rock", "rock", or "ROCK").
*   **Graceful Exit:** Quit the game at any point by typing `exit`.

---

## 🛠️ Tech Stack

*   **Language:** Python 3.x
*   **Libraries:** Built entirely using Python's standard `random` library (no external dependencies required).

---

## 🚀 How to Run the Game

### Prerequisites
Make sure you have Python installed on your system. You can check this by running:
```bash
python --version
