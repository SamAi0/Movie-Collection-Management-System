"""
=============================================================================
Project Title : Movie Collection Management System
Course        : MCA Semester I
Subject       : Problem Solving and Python Programming
File Name     : movie_management.py
Description   : A complete, menu-driven Python console application designed to
                manage a movie catalog. Demonstrates core Python concepts:
                Variables, Data Types, Conditionals, Loops, Functions,
                File I/O, JSON handling, and Exception Handling.
=============================================================================
"""

# [CONCEPT: Python Standard Library Modules]
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "movies.json")

MIN_RELEASE_YEAR = 1888
MAX_RELEASE_YEAR = 2100


# =============================================================================
# FILE I/O AND DATA PERSISTENCE FUNCTIONS
# =============================================================================

def load_movies(file_path=FILE_NAME):
    """
    [CONCEPT: File I/O - Reading & Exception Handling]
    Loads the movie collection from a JSON file.
    Handles:
      - Missing file (creates a new file with empty list)
      - Corrupted or invalid JSON data
      - Permission / OS errors
    Returns:
      list: A list of movie dictionaries.
    """
    if not os.path.exists(file_path):
        print(f"\n[INFO] Data file '{os.path.basename(file_path)}' not found. Creating a new one...")
        save_movies([], file_path)
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            movies = json.load(file)
            
            if isinstance(movies, list):
                return movies
            else:
                print("\n[WARNING] Corrupted data format detected. Resetting to an empty collection.")
                return []

    except json.JSONDecodeError:
        print("\n[ERROR] JSON decoding failed: Data file is empty or corrupted.")
        print("[INFO] Starting with an empty collection. Changes will overwrite on save.")
        return []

    except IOError as e:
        print(f"\n[ERROR] File read error: {e}")
        return []


def save_movies(movies, file_path=FILE_NAME):
    """
    [CONCEPT: File I/O - Writing & Exception Handling]
    Saves the list of movie dictionaries to the JSON file with indentation.
    Parameters:
      movies (list): Collection of movie records to persist.
      file_path (str): Target file path.
    Returns:
      bool: True if save succeeded, False otherwise.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(movies, file, indent=4)
        return True

    except IOError as e:
        print(f"\n[ERROR] Failed to save data to file: {e}")
        return False


# =============================================================================
# INPUT VALIDATION HELPER FUNCTIONS
# =============================================================================

def get_non_empty_string(prompt):
    """
    [CONCEPT: Loops & String Validation]
    Repeatedly prompts user until a non-empty string is provided.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [!] Input cannot be empty. Please enter a valid text.")


def get_valid_integer(prompt, min_val, max_val):
    """
    [CONCEPT: Data Types (int) & Exception Handling (ValueError)]
    Prompts user for an integer within [min_val, max_val].
    """
    while True:
        user_input = input(prompt).strip()
        try:
            val = int(user_input)
            if min_val <= val <= max_val:
                return val
            else:
                print(f"  [!] Please enter a year between {min_val} and {max_val}.")
        except ValueError:
            print("  [!] Invalid numeric format. Please enter a valid whole number.")


def get_valid_float(prompt, min_val=0.0, max_val=10.0):
    """
    [CONCEPT: Data Types (float) & Exception Handling (ValueError)]
    Prompts user for a float rating within [min_val, max_val].
    """
    while True:
        user_input = input(prompt).strip()
        try:
            val = float(user_input)
            if min_val <= val <= max_val:
                return round(val, 1)
            else:
                print(f"  [!] Rating must be between {min_val:.1f} and {max_val:.1f}.")
        except ValueError:
            print("  [!] Invalid input. Please enter a decimal rating (e.g., 8.5).")


def is_duplicate_id(movies, movie_id):
    """
    [CONCEPT: Loops & Conditionals - Checking unique keys in a list of dicts]
    Returns True if movie_id already exists in the collection (case-insensitive).
    """
    for movie in movies:
        if movie.get("movie_id", "").strip().lower() == movie_id.strip().lower():
            return True
    return False


def find_movie_by_id(movies, movie_id):
    """
    Searches for a movie by ID and returns its dictionary and list index.
    Returns: (index, movie_dict) or (-1, None)
    """
    for index, movie in enumerate(movies):
        if movie.get("movie_id", "").strip().lower() == movie_id.strip().lower():
            return index, movie
    return -1, None


# =============================================================================
# FORMATTING & DISPLAY HELPERS
# =============================================================================

def print_movie_table(movie_list):
    """
    [CONCEPT: String Formatting & Table Presentation]
    Displays a list of movie records in an organized console table.
    """
    if not movie_list:
        print("\n  No movies found to display.")
        return

    line_border = "+" + "-" * 8 + "+" + "-" * 26 + "+" + "-" * 20 + "+" + "-" * 8 + "+" + "-" * 12 + "+" + "-" * 8 + "+" + "-" * 22 + "+"
    print("\n" + line_border)
    print(f"| {'ID':<6} | {'Movie Name':<24} | {'Genre':<18} | {'Year':<6} | {'Language':<10} | {'Rating':<6} | {'Director':<20} |")
    print(line_border)

    for m in movie_list:
        m_id = str(m.get("movie_id", "N/A"))[:6]
        name = str(m.get("movie_name", "N/A"))[:24]
        genre = str(m.get("genre", "N/A"))[:18]
        year = str(m.get("release_year", "N/A"))[:6]
        lang = str(m.get("language", "N/A"))[:10]
        rating = f"{float(m.get('rating', 0.0)):.1f}"[:6]
        director = str(m.get("director", "N/A"))[:20]

        print(f"| {m_id:<6} | {name:<24} | {genre:<18} | {year:<6} | {lang:<10} | {rating:<6} | {director:<20} |")

    print(line_border)
    print(f"  Total Records Displayed: {len(movie_list)}")


# =============================================================================
# CORE APPLICATION FUNCTIONS (CRUD OPERATIONS)
# =============================================================================

def add_movie(movies):
    """
    [CONCEPT: Functions & Dictionaries]
    Requirement 1: Adds a new movie record with complete input validation.
    """
    print("\n" + "=" * 50)
    print("                 ADD NEW MOVIE")
    print("=" * 50)

    while True:
        movie_id = get_non_empty_string("Enter Movie ID (e.g., M106 or 106): ").upper()
        if is_duplicate_id(movies, movie_id):
            print(f"  [!] Error: Movie ID '{movie_id}' already exists! Choose a unique ID.")
        else:
            break

    movie_name = get_non_empty_string("Enter Movie Name: ")

    genre = get_non_empty_string("Enter Genre (e.g., Action, Sci-Fi, Drama): ")

    release_year = get_valid_integer(
        f"Enter Release Year ({MIN_RELEASE_YEAR}-{MAX_RELEASE_YEAR}): ",
        MIN_RELEASE_YEAR,
        MAX_RELEASE_YEAR
    )

    language = get_non_empty_string("Enter Language (e.g., English, Hindi): ")

    rating = get_valid_float("Enter Rating (0.0 to 10.0): ", 0.0, 10.0)

    director = get_non_empty_string("Enter Director: ")

    new_movie = {
        "movie_id": movie_id,
        "movie_name": movie_name,
        "genre": genre,
        "release_year": release_year,
        "language": language,
        "rating": rating,
        "director": director
    }

    movies.append(new_movie)

    if save_movies(movies):
        print(f"\n[SUCCESS] Movie '{movie_name}' (ID: {movie_id}) added and saved successfully!")
    else:
        print("\n[WARNING] Movie added to memory, but failed to write to disk.")


def view_movies(movies):
    """
    [CONCEPT: Functions & Loops]
    Requirement 2: Views all movies currently in the collection.
    """
    print("\n" + "=" * 50)
    print("               VIEW ALL MOVIES")
    print("=" * 50)

    if not movies:
        print("\n  [INFO] The movie collection is currently empty.")
        print("  Use Option 1 from the main menu to add your first movie!")
        return

    print_movie_table(movies)


def search_movie(movies):
    """
    [CONCEPT: Conditional Statements, Loops & Case-Insensitive String Search]
    Requirement 3: Searches movies by Movie ID, Movie Name, or Genre.
    """
    print("\n" + "=" * 50)
    print("                 SEARCH MOVIES")
    print("=" * 50)

    if not movies:
        print("\n  [INFO] The movie collection is empty. Nothing to search.")
        return

    print("1. Search by Movie ID")
    print("2. Search by Movie Name")
    print("3. Search by Genre")
    print("4. Back to Main Menu")

    choice = input("\nEnter your search option (1-4): ").strip()

    results = []

    if choice == "1":
        search_id = input("Enter Movie ID to search: ").strip().lower()
        for movie in movies:
            if movie.get("movie_id", "").strip().lower() == search_id:
                results.append(movie)

    elif choice == "2":
        search_name = input("Enter Movie Name (or keyword): ").strip().lower()
        if not search_name:
            print("  [!] Search keyword cannot be empty.")
            return
        for movie in movies:
            if search_name in movie.get("movie_name", "").lower():
                results.append(movie)

    elif choice == "3":
        search_genre = input("Enter Genre (or keyword): ").strip().lower()
        if not search_genre:
            print("  [!] Genre keyword cannot be empty.")
            return
        for movie in movies:
            if search_genre in movie.get("genre", "").lower():
                results.append(movie)

    elif choice == "4":
        return

    else:
        print("\n[ERROR] Invalid search option! Returning to main menu.")
        return

    if results:
        print(f"\n[RESULTS] Found {len(results)} matching movie(s):")
        print_movie_table(results)
    else:
        print("\n[INFO] No movies found matching your search criteria.")


def update_movie(movies):
    """
    [CONCEPT: Functions, Dictionaries & Conditionals]
    Requirement 4: Updates an existing movie's details based on Movie ID.
    User can enter new values or press Enter to keep current values.
    """
    print("\n" + "=" * 50)
    print("                 UPDATE MOVIE")
    print("=" * 50)

    if not movies:
        print("\n  [INFO] The movie collection is empty. Nothing to update.")
        return

    target_id = input("Enter Movie ID to update: ").strip()
    index, movie = find_movie_by_id(movies, target_id)

    if index == -1:
        print(f"\n[ERROR] Movie with ID '{target_id}' was not found in the collection.")
        return

    print("\n--- Current Movie Details ---")
    print(f"ID           : {movie.get('movie_id')}")
    print(f"Name         : {movie.get('movie_name')}")
    print(f"Genre        : {movie.get('genre')}")
    print(f"Release Year : {movie.get('release_year')}")
    print(f"Language     : {movie.get('language')}")
    print(f"Rating       : {movie.get('rating')}")
    print(f"Director     : {movie.get('director')}")
    print("---------------------------------")
    print("[HINT] Press [Enter] without typing anything to keep the current value.\n")

    new_name = input(f"New Name [{movie['movie_name']}]: ").strip()
    if new_name:
        movie["movie_name"] = new_name

    new_genre = input(f"New Genre [{movie['genre']}]: ").strip()
    if new_genre:
        movie["genre"] = new_genre

    while True:
        year_input = input(f"New Release Year [{movie['release_year']}]: ").strip()
        if not year_input:
            break  
        try:
            val = int(year_input)
            if MIN_RELEASE_YEAR <= val <= MAX_RELEASE_YEAR:
                movie["release_year"] = val
                break
            else:
                print(f"  [!] Year must be between {MIN_RELEASE_YEAR} and {MAX_RELEASE_YEAR}.")
        except ValueError:
            print("  [!] Please enter a valid numeric year.")

    new_lang = input(f"New Language [{movie['language']}]: ").strip()
    if new_lang:
        movie["language"] = new_lang

    while True:
        rating_input = input(f"New Rating [{movie['rating']}]: ").strip()
        if not rating_input:
            break
        try:
            val = float(rating_input)
            if 0.0 <= val <= 10.0:
                movie["rating"] = round(val, 1)
                break
            else:
                print("  [!] Rating must be between 0.0 and 10.0.")
        except ValueError:
            print("  [!] Please enter a valid decimal rating (e.g., 8.5).")

    new_director = input(f"New Director [{movie['director']}]: ").strip()
    if new_director:
        movie["director"] = new_director

    if save_movies(movies):
        print(f"\n[SUCCESS] Movie '{movie['movie_name']}' (ID: {movie['movie_id']}) updated successfully!")
    else:
        print("\n[WARNING] Updated in memory, but could not write to disk.")


def delete_movie(movies):
    """
    [CONCEPT: Functions, Lists & Confirmation Checks]
    Requirement 5: Deletes a movie by Movie ID with confirmation prompt.
    """
    print("\n" + "=" * 50)
    print("                 DELETE MOVIE")
    print("=" * 50)

    if not movies:
        print("\n  [INFO] The movie collection is empty. Nothing to delete.")
        return

    target_id = input("Enter Movie ID to delete: ").strip()
    index, movie = find_movie_by_id(movies, target_id)

    if index == -1:
        print(f"\n[ERROR] Movie with ID '{target_id}' was not found in the collection.")
        return

    print(f"\nTarget Movie Found: '{movie['movie_name']}' ({movie['release_year']}) directed by {movie['director']}")
    
    confirm = input("Are you sure you want to delete this movie? (y/n): ").strip().lower()

    if confirm == "y" or confirm == "yes":
        deleted_movie = movies.pop(index)
        if save_movies(movies):
            print(f"\n[SUCCESS] Movie '{deleted_movie['movie_name']}' (ID: {deleted_movie['movie_id']}) was permanently deleted!")
        else:
            print("\n[WARNING] Removed from memory, but failed to save file.")
    else:
        print("\n[INFO] Deletion canceled by user. No changes were made.")


# =============================================================================
# OPTIONAL & ADVANCED FEATURES (SORTING, FILTERING & STATISTICS)
# =============================================================================

def sort_and_filter_menu(movies):
    """
    [CONCEPT: Optional Features - Sorting & Filtering]
    Provides sorting by name/rating and filtering by genre.
    """
    print("\n" + "=" * 50)
    print("            SORT & FILTER MOVIES")
    print("=" * 50)

    if not movies:
        print("\n  [INFO] The movie collection is empty.")
        return

    print("1. Sort Movies by Name (A to Z)")
    print("2. Sort Movies by Rating (Highest to Lowest)")
    print("3. Sort Movies by Release Year (Newest First)")
    print("4. Filter Movies by Genre")
    print("5. Back to Main Menu")

    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "1":
        sorted_list = sorted(movies, key=lambda m: m.get("movie_name", "").lower())
        print("\n--- Movies Sorted by Name (A to Z) ---")
        print_movie_table(sorted_list)

    elif choice == "2":
        sorted_list = sorted(movies, key=lambda m: float(m.get("rating", 0.0)), reverse=True)
        print("\n--- Movies Sorted by Rating (Highest First) ---")
        print_movie_table(sorted_list)

    elif choice == "3":
        sorted_list = sorted(movies, key=lambda m: int(m.get("release_year", 0)), reverse=True)
        print("\n--- Movies Sorted by Year (Newest First) ---")
        print_movie_table(sorted_list)

    elif choice == "4":
        genre_query = input("Enter Genre to filter by: ").strip().lower()
        filtered = [m for m in movies if genre_query in m.get("genre", "").lower()]
        if filtered:
            print(f"\n--- Movies in Genre '{genre_query.capitalize()}' ---")
            print_movie_table(filtered)
        else:
            print(f"\n[INFO] No movies found in genre '{genre_query}'.")

    elif choice == "5":
        return
    else:
        print("\n[ERROR] Invalid choice! Returning to main menu.")


def display_statistics(movies):
    """
    [CONCEPT: Numerical Calculations, Accumulators & Statistics]
    Calculates and displays total count, average rating, highest rated, etc.
    """
    print("\n" + "=" * 50)
    print("          COLLECTION STATISTICS & INSIGHTS")
    print("=" * 50)

    total_count = len(movies)

    if total_count == 0:
        print("\n  [INFO] No movies available to compute statistics.")
        return

    total_rating = 0.0
    genres = set()
    highest_rated = movies[0]
    lowest_rated = movies[0]

    for m in movies:
        r = float(m.get("rating", 0.0))
        total_rating += r
        genres.add(m.get("genre", "Unknown"))

        if r > float(highest_rated.get("rating", 0.0)):
            highest_rated = m
        if r < float(lowest_rated.get("rating", 0.0)):
            lowest_rated = m

    avg_rating = total_rating / total_count

    print(f"\n  • Total Movies in Collection : {total_count}")
    print(f"  • Average Movie Rating       : {avg_rating:.2f} / 10.0")
    print(f"  • Unique Genres Count        : {len(genres)} ({', '.join(sorted(genres))})")
    print(f"  • Highest Rated Movie        : '{highest_rated['movie_name']}' ({highest_rated['rating']}/10.0)")
    print(f"  • Lowest Rated Movie         : '{lowest_rated['movie_name']}' ({lowest_rated['rating']}/10.0)")
    print("-" * 50)


# =============================================================================
# MENU AND MAIN EXECUTION CONTROLLER
# =============================================================================

def display_menu():
    """
    [CONCEPT: Menu-driven Console UI Design]
    Displays the application's clean main menu.
    """
    print("\n" + "=" * 50)
    print("      🎬 MOVIE COLLECTION MANAGEMENT SYSTEM")
    print("=" * 50)
    print("  1. Add Movie")
    print("  2. View All Movies")
    print("  3. Search Movie")
    print("  4. Update Movie")
    print("  5. Delete Movie")
    print("  6. Sort & Filter Movies")
    print("  7. Collection Statistics")
    print("  8. Exit")
    print("=" * 50)


def main():
    """
    [CONCEPT: Main Controller Function & While Loop]
    Entry point of the Movie Collection Management System.
    Loads data once, continuously serves menu choices, and exits cleanly.
    """
    print("\n" + "*" * 58)
    print("   WELCOME TO MOVIE COLLECTION MANAGEMENT SYSTEM")
    print("        MCA Semester I - Python Programming")
    print("*" * 58)

    movies = load_movies(FILE_NAME)
    print(f"[INFO] Initialized system. Loaded {len(movies)} movie record(s) from 'movies.json'.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            view_movies(movies)
        elif choice == "3":
            search_movie(movies)
        elif choice == "4":
            update_movie(movies)
        elif choice == "5":
            delete_movie(movies)
        elif choice == "6":
            sort_and_filter_menu(movies)
        elif choice == "7":
            display_statistics(movies)
        elif choice == "8":
            print("\n" + "=" * 50)
            print("  Thank you for using Movie Collection Management!")
            print("  Have a great day. Exiting program...")
            print("=" * 50 + "\n")
            break
        else:
            print("\n[ERROR] Invalid choice! Please enter a number between 1 and 8.")

        input("\nPress [Enter] to continue back to menu...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[INFO] Application interrupted by user. Goodbye!")
        sys.exit(0)
