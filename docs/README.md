# StudySprint

StudySprint is a command-line flashcard quiz tool for practicing study questions. It loads a saved deck from a JSON file and provides a numbered menu.

## Run it

From the repository root, run:

```bash
python main.py
```

Choose a menu number, or choose `0` to quit.

## What works in this release

- Take a quiz of the saved flashcards and see the number and percentage of correct answers.
- List flashcards or add a new question and answer. Added cards are saved to the JSON deck.
- Study questions filtered by category.
- View the last card in the deck.
- Show counts by category from the deck (menu option 6).
- Display the deck name and total number of cards (menu option 7).

Note: `features/reports.py` also contains an unfinished `category_report` helper. The working menu option 6 uses `features/core.py` instead; the unfinished report is **not** part of this release. The app also assumes a deck is present when asking for the last card.

## Run tests

```bash
python -m unittest
```

The current `main` branch includes two starter unit tests in `tests/test_core.py`; they check answer matching and adding a new card. These tests do not cover every menu action.

## Files

| File | Purpose |
|---|---|
| `main.py` | Command-line menu |
| `storage.py` | Load and save JSON data |
| `features/core.py` | Quiz, cards and category counting |
| `features/reports.py` | Deck summary and unfinished category report |
| `data/studysprint.json` | Stored flashcard deck |
| `tests/test_core.py` | Existing starter tests |
| `docs/RELEASE_NOTES.md` | Release history |

## Development

See `CONTRIBUTING.md` for collaboration guidelines. Track remaining tasks in GitHub Issues. The release includes only the features actually available on `main`; changes in unmerged pull requests are not yet shipped.
