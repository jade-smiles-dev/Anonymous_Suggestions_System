# Anonymous Suggestions System

## What is this code?

This is a Python application that allows individuals to submit anonymous suggestions within a team or workplace.

The purpose of the application is to give everyone a way to share ideas, suggestions, or concerns without needing to speak up in meetings. This is particularly useful for those who are less confident or not comfortable speaking in group settings.

Managers can then review, prioritise, and track these suggestions for further consideration and implementation.

---

## What does it do?

- Submit suggestions anonymously  
- Choose a category for suggestions (e.g. Process, Communication, Technical)  
- Assign an urgency rating (Low, Medium, High)  
- Automatically calculate a priority score  
- View all suggestions (sorted by priority)  
- View only new suggestions  
- Update the status of suggestions (e.g. Under Review, Accepted)  
- Store data using a SQLite database  
- Includes basic input validation and error handling  
- Works via command line or a simple graphical user interface (GUI)  

---

## What technology has been used?

- Python 3  
- SQLite (built-in database)  
- Tkinter (for the GUI)  

---

## Project structure

```
anonymous_suggestions_box/
│
├── main.py         # Command-line version
├── gui.py          # Simple GUI version
├── database.py     # Handles database operations
├── services.py     # Validation + logic (like priority scoring)
├── suggestions.db     # Database (created automatically)
└── README.md
```

## How to run the application

### Command line version

Run:

```
python main.py
```


Follow the menu options to submit and view suggestions.

---

### GUI version

Run:

```
python gui.py
```

This will open a simple window where you can interact with the system.

---

## How does the application work?

Suggestions are stored in a SQLite database.

Each suggestion is assigned a priority score based on its urgency and category. This allows suggestions to be sorted so that the most important ones appear first.

Suggestions can also be updated through different statuses, allowing them to be tracked over time.

---

## Example of application usage

1. Submit a suggestion (e.g. "Improve meeting structure")  
2. Assign a category and urgency  
3. View suggestions sorted by priority  
4. Update status as it progresses  

---

## Future improvement considerations

- Convert the application into a web-based system  
- Add user authentication and role-based access levels  
- Integrate with tools such as Microsoft Teams  
- Add analytics or reporting features  
- Improve the priority scoring system  
- Improve the user interface and introduce branded styling  

---

## Author

Jade Smiles (BP0287729)