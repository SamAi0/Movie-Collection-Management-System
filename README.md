# 🎬 Movie Collection Management System

A beginner-friendly, modular, console-based Python application developed as an academic project for **Master of Computer Applications (MCA) Semester I**.

The system enables users to manage a personal or institutional movie collection with complete CRUD (Create, Read, Update, Delete) functionality, advanced search and filter options, automated collection statistics, and persistent JSON file storage with full input validation and exception handling.

---

## 📌 Project Objectives

1. **Demonstrate Core Python Concepts:** Implement variables, native data types (strings, integers, floats), composite data structures (lists and dictionaries), control flow (if-elif-else, for loops, while loops), modular functions, and robust exception handling.
2. **File Persistence:** Permanently persist movie records on disk using JSON serialization and deserialization, without requiring external database servers or third-party ORMs.
3. **Data Integrity & Validation:** Prevent application crashes by validating all console inputs (preventing duplicate IDs, empty strings, invalid numeric formats, out-of-range ratings, and corrupted files).
4. **Clean Console UI:** Provide an intuitive, formatted, menu-driven interface accessible to everyday users directly from the command line.

---

## ✨ Features

* **Add Movie:** Record new movies with Movie ID, Movie Name, Genre, Release Year, Language, Rating (0.0 to 10.0), and Director. Automatically enforces uniqueness of Movie IDs.
* **View All Movies:** Tabular layout with aligned columns for clean visualization of all saved movies.
* **Multi-Criteria Search:**
  * Search by Movie ID (exact, case-insensitive)
  * Search by Movie Name (keyword/substring, case-insensitive)
  * Search by Genre (keyword/substring, case-insensitive)
* **Update Movie Details:** Allows editing individual movie fields while preserving existing values with a simple press of the `[Enter]` key.
* **Safe Deletion:** Prompts user with a confirmation check `(y/n)` before permanently removing a movie from the database.
* **Sorting & Filtering (Optional Features):**
  * Sort movies alphabetically by Name (A to Z)
  * Sort movies by Rating (Highest to Lowest)
  * Sort movies by Release Year (Newest to Oldest)
  * Filter movies by specific Genre
* **Collection Insights & Statistics:**
  * Total movie count
  * Average rating of collection
  * Unique genre count and genre tags
  * Highest and lowest rated movies
* **Automated Data Initialization:** Automatically detects and creates `movies.json` if it does not exist.

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3.8+ (Standard Library only)
* **Data Storage Format:** JSON (JavaScript Object Notation via built-in `json` module)
* **Operating System Compatibility:** Cross-platform (Windows, macOS, Linux)
* **External Dependencies:** **None** (No `pip install` required)

---

## 🧠 Python Concepts Used

| Academic Concept | Implementation in Code |
| :--- | :--- |
| **Variables & Primitive Types** | Strings for text, integers for release years, floats for ratings, booleans for status flags. |
| **Data Structures** | **Dictionaries** represent individual movie records (`key: value`); **Lists** store the entire collection of movie dictionaries. |
| **Conditional Logic** | `if`, `elif`, and `else` blocks control menu choices, search routing, and duplicate validation. |
| **Iteration & Loops** | `while True` drives the main menu and input validation loops; `for` loops iterate over movie records for display, search, and computation. |
| **Modular Functions** | Pure, reusable functions with parameters and return values (`load_movies`, `save_movies`, `add_movie`, `search_movie`, etc.). |
| **Exception Handling** | `try...except` blocks protect against `ValueError` (type conversion), `json.JSONDecodeError` (corrupt files), `IOError`/`FileNotFoundError` (file access), and `KeyboardInterrupt` (graceful termination). |
| **File I/O** | `open()` using context managers (`with`) to reliably read (`r`) and write (`w`) formatted JSON data. |

---

## 📂 Project Structure

```text
Movie-Collection-Management-System/
│
├── movie_management.py      # Main executable console application
├── movies.json              # Persistent JSON database (contains sample records)
├── README.md                # Project documentation and guide
├── Assignment_Report.md     # Comprehensive academic report for MCA Sem I
│
└── screenshots/             # Folder containing console execution images
    └── README.md            # Guidelines on required screenshots
```

---

## ⚙️ System Requirements

* **Python:** Version 3.8 or higher installed
* **RAM:** 512 MB minimum
* **Disk Space:** Less than 5 MB
* **Terminal / Console:** Windows Command Prompt / PowerShell, macOS Terminal, or Linux Bash

---

## 🚀 How to Run the Application

### 1. Clone or Download the Project
Ensure all files are placed in a single folder named `Movie-Collection-Management-System`.

### 2. Open Terminal / Command Prompt
Navigate to the project directory:
```bash
cd Movie-Collection-Management-System
```

### 3. Run the Program
Execute using the standard Python interpreter:
```bash
python3 movie_management.py
```
*(On macOS / Linux systems with multiple Python versions installed, use `python3 movie_management.py`)*

---

## 📋 Menu Options

When the application starts, the user is presented with the following interactive menu:

```text
==================================================
      🎬 MOVIE COLLECTION MANAGEMENT SYSTEM
==================================================
  1. Add Movie
  2. View All Movies
  3. Search Movie
  4. Update Movie
  5. Delete Movie
  6. Sort & Filter Movies
  7. Collection Statistics
  8. Exit
==================================================
Enter your choice (1-8):
```

---

## 💬 Sample Input and Output

### 1. Adding a Movie (Option 1)
```text
==================================================
                 ADD NEW MOVIE
==================================================
Enter Movie ID (e.g., M106 or 106): M106
Enter Movie Name: Oppenheimer
Enter Genre (e.g., Action, Sci-Fi, Drama): Biography/Drama
Enter Release Year (1888-2100): 2023
Enter Language (e.g., English, Hindi): English
Enter Rating (0.0 to 10.0): 8.9
Enter Director: Christopher Nolan

[SUCCESS] Movie 'Oppenheimer' (ID: M106) added and saved successfully!
```

### 2. Viewing All Movies (Option 2)
```text
+--------+--------------------------+----------------+--------+------------+--------+----------------------+
| ID     | Movie Name               | Genre          | Year   | Language   | Rating | Director             |
+--------+--------------------------+----------------+--------+------------+--------+----------------------+
| M101   | Interstellar             | Sci-Fi         | 2014   | English    | 8.7    | Christopher Nolan    |
| M102   | Inception                | Sci-Fi         | 2010   | English    | 8.8    | Christopher Nolan    |
| M103   | 3 Idiots                 | Comedy/Drama   | 2009   | Hindi      | 8.4    | Rajkumar Hirani      |
| M104   | The Dark Knight          | Action/Crime   | 2008   | English    | 9.0    | Christopher Nolan    |
| M105   | Dangal                   | Biography/Drama| 2016   | Hindi      | 8.3    | Nitesh Tiwari        |
+--------+--------------------------+----------------+--------+------------+--------+----------------------+
  Total Records Displayed: 5
```

### 3. Deleting a Movie with Confirmation (Option 5)
```text
==================================================
                 DELETE MOVIE
==================================================
Enter Movie ID to delete: M105

Target Movie Found: 'Dangal' (2016) directed by Nitesh Tiwari
Are you sure you want to delete this movie? (y/n): y

[SUCCESS] Movie 'Dangal' (ID: M105) was permanently deleted!
```

---

## 💾 Data Storage Explanation

Movie information is stored in **JSON (JavaScript Object Notation)** format in `movies.json`. 

### Sample JSON Structure:
```json
[
    {
        "movie_id": "M101",
        "movie_name": "Interstellar",
        "genre": "Sci-Fi",
        "release_year": 2014,
        "language": "English",
        "rating": 8.7,
        "director": "Christopher Nolan"
    }
]
```

### Why JSON?
* **Human-Readable:** Text-based format easily inspected in any text editor.
* **Lightweight:** Does not require database servers like MySQL or MongoDB.
* **Direct Python Mapping:** JSON objects directly map to Python **dictionaries**, and JSON arrays map directly to Python **lists**.

---

## 🛡️ Exception Handling & Robustness

The application includes defensive programming mechanisms to avoid runtime crashes:
* **`ValueError`:** Handled during integer parsing (`int()`) for Release Year and floating-point parsing (`float()`) for Rating. If a user enters non-numeric text like `"ten"`, the application politely requests valid numeric input.
* **`json.JSONDecodeError`:** Handled during startup if `movies.json` is corrupted or has malformed syntax. Rather than crashing, the program informs the user and initializes safely.
* **`FileNotFoundError` / `IOError`:** Handled during file load/save. Missing files are automatically created on the fly.
* **`KeyboardInterrupt`:** Handled when the user presses `Ctrl + C`, ensuring a clean termination message without raw tracebacks.

---

## 🔮 Future Enhancements

* Add authentication (User/Admin login with role-based permissions).
* Export collection summary as a CSV or PDF report.
* Integration with an external API (such as OMDb or TMDb) for automatic poster and metadata fetching.
* Upgrade the interface to a Graphical User Interface (GUI) using Tkinter or PyQt.

---

## 🔗 GitHub Repository

Project Source Code Repository:
`YOUR_GITHUB_REPOSITORY_LINK`

*(Replace `YOUR_GITHUB_REPOSITORY_LINK` with your personal GitHub project URL prior to final submission).*

---

## 📸 Screenshots

**1. Main Menu**
![Main Menu](screenshots/Main%20Menu.png)

**2. Adding a Movie**
![Add Movie](screenshots/Add%20Movie.png)

**3. Viewing All Movies**
![View Movies](screenshots/View%20Movies.png)

**4. Collection Statistics**
![Collection Statistics](screenshots/Collection%20statistics.png)
