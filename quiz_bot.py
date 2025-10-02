# commit_bot.py
import datetime
import random
import os

TEMPLATES = [
    "Note: small refactor of utils",
    "Docs: add example usage",
    "Chore: update README badges",
    "Tests: add simple unit check",
    "Format: ran code formatter",
    "Note: learning log — tried X",
]

def append_journal():
    now = datetime.datetime.utcnow().isoformat() + "Z"
    entry = f"{now} - {random.choice(TEMPLATES)}\n"
    os.makedirs(".", exist_ok=True)
    with open("journal.md", "a", encoding="utf-8") as f:
        f.write(entry)

if __name__ == "__main__":
    append_journal()
    print("Wrote a journal entry.")
