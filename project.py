import csv

def main():
    watchlist = load_watchlist()

    while True:
        print("\nMovie Watchlist App")
        print("1. Add a movie to the watchlist")
        print("2. View watchlist")
        print("3. Mark a movie as watched")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            movie = input("Enter movie name: ").strip()
            add_to_watchlist(movie, watchlist)

        elif choice == "2":
            display_watchlist(watchlist)

        elif choice == "3":
            movie = input("Enter the name of the movie to mark as watched: ").strip()
            mark_as_watched(movie, watchlist)

        elif choice == "4":
            save_watchlist(watchlist)
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# Function to load watchlist from CSV
def load_watchlist(filename='films.csv'):
    try:
        with open(filename, 'r') as file:
            return [row[0] for row in csv.reader(file)]
    except FileNotFoundError:
        return []


# Function to save watchlist to CSV
def save_watchlist(watchlist, filename='films.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for movie in watchlist:
            writer.writerow([movie])


# Function to add a movie to the watchlist
def add_to_watchlist(movie, watchlist):
    if movie not in watchlist:
        watchlist.append(movie)
        print(f"'{movie}' added to your watchlist!")
    else:
        print(f"'{movie}' is already in your watchlist!")


# Function to display the watchlist
def display_watchlist(watchlist):
    if watchlist:
        print("\nYour Watchlist:")
        for movie in watchlist:
            print(f"- {movie}")
    else:
        print("\nYour watchlist is empty!")


# Function to mark a movie as watched
def mark_as_watched(movie, watchlist):
    if movie in watchlist:
        watchlist.remove(movie)
        print(f"'{movie}' marked as watched!")
    else:
        print(f"'{movie}' is not in your watchlist!")

if __name__ == "__main__":
    main()

