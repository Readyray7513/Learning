 # Movie Watchlist App
    #### Video Demo:  <(https://youtu.be/azgm71gUWMY)>
    #### Description: The Movie Watchlist App is a simple command-line Python application that allows users to maintain and manage a watchlist of movies. The main features of the app include:
    - Add a movie to the watchlist: Users can input a movie title and add it to their watchlist.
    - View the current watchlist: The app displays all movies currently in the watchlist.
    - Mark movies as watched: Users can remove movies from the watchlist after they've watched them.
    - CSV file storage: The watchlist is saved to a CSV file, which allows users to persist their data between sessions.

This project was developed as part of a personal learning journey to improve my Python programming skills, specifically in handling data and implementing simple user interfaces in the terminal.

       Features
    - Persistent data: The app saves your watchlist to a CSV file called `films.csv`, ensuring that your watchlist is saved even after closing the program.
    - No duplicates: If you try to add a movie that's already in the watchlist, the app prevents duplicates.
    - Interactive menu: The app displays a menu of options, making it easy for users to navigate between adding movies, viewing the list, and marking movies as watched.

Approach:

The application is built using Python, with data being stored locally in a file or database, ensuring the watchlist persists between sessions. The user interacts with the program via simple text-based commands in the terminal. Each command corresponds to an operation that either modifies or displays the list of films.

Challenges:

One of the key challenges during development was ensuring that the data was properly saved after each operation, so the watchlist could be reloaded upon restarting the app. Another challenge was designing a simple, user-friendly interface in the terminal without relying on complex libraries.

Future Improvements:

While the current version of the app is functional, future enhancements could include:

Search Functionality: Allow users to search for films in the watchlist.
Sorting Options: Users could sort their movies by genre, release year, or other categories.
Enhanced UI: A graphical interface could be developed for a more user-friendly experience.
Data Persistence: Moving to a more robust database, like SQLite, to manage the data better as the watchlist grows.
