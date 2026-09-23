"""
Cinema Seat Booking System
Data Structure: 2D List
Language: Python

Menu:
1. View Seats
2. Book Seat
3. Cancel Booking
4. Search Seat
5. Booking Statistics
6. Exit

O = Available
X = Booked

No database or file storage is used. Booking data exists
only while the program is running.
"""

ROWS = 5
COLUMNS = 5
ROW_NAMES = ["A", "B", "C", "D", "E"]


def create_seat_matrix():
    """Create a 5x5 2D list with every seat initially available."""
    seats = []

    for _ in range(ROWS):
        row = []

        for _ in range(COLUMNS):
            row.append("O")

        seats.append(row)

    return seats


def display_seats(seats):
    """Display the current cinema seating arrangement."""
    print("\n" + "=" * 45)
    print("             CINEMA SEAT LAYOUT")
    print("=" * 45)

    print("       ", end="")

    for column in range(1, COLUMNS + 1):
        print(f"{column:^5}", end="")

    print()
    print("-" * 45)

    for i in range(ROWS):
        print(f"  {ROW_NAMES[i]}   ", end="")

        for j in range(COLUMNS):
            print(f"[{seats[i][j]}]  ", end="")

        print()

    print("-" * 45)
    print("O = Available     X = Booked")
    print("=" * 45)


def get_seat_position(seat_number):
    """
    Convert a seat such as B3 into 2D-list indexes.

    B3 -> row index 1, column index 2
    """
    seat_number = seat_number.strip().upper()

    if len(seat_number) < 2:
        return None

    row_letter = seat_number[0]
    column_part = seat_number[1:]

    if row_letter not in ROW_NAMES:
        return None

    if not column_part.isdigit():
        return None

    column_number = int(column_part)

    if column_number < 1 or column_number > COLUMNS:
        return None

    row_index = ROW_NAMES.index(row_letter)
    column_index = column_number - 1

    return row_index, column_index


def book_seat(seats):
    """Book an available seat."""
    print("\n" + "=" * 45)
    print("                 BOOK SEAT")
    print("=" * 45)

    display_seats(seats)

    seat_number = input("\nEnter seat number to book (Example: B3): ")
    position = get_seat_position(seat_number)

    if position is None:
        print("\nInvalid seat number.")
        print("Please use a format such as A1, B3, or E5.")
        return

    row, column = position

    if seats[row][column] == "X":
        print(f"\nSeat {seat_number.upper()} is already booked.")
        return

    seats[row][column] = "X"
    print(f"\nSeat {seat_number.upper()} booked successfully!")


def cancel_booking(seats):
    """Cancel an existing booking."""
    print("\n" + "=" * 45)
    print("              CANCEL BOOKING")
    print("=" * 45)

    display_seats(seats)

    seat_number = input("\nEnter seat number to cancel: ")
    position = get_seat_position(seat_number)

    if position is None:
        print("\nInvalid seat number.")
        print("Please use a format such as A1, B3, or E5.")
        return

    row, column = position

    if seats[row][column] == "O":
        print(f"\nSeat {seat_number.upper()} is not booked.")
        return

    seats[row][column] = "O"
    print(f"\nBooking for seat {seat_number.upper()} cancelled successfully!")


def search_seat(seats):
    """Search for a seat and display whether it is booked or available."""
    print("\n" + "=" * 45)
    print("                 SEARCH SEAT")
    print("=" * 45)

    seat_number = input("Enter seat number to search: ")
    position = get_seat_position(seat_number)

    if position is None:
        print("\nInvalid seat number.")
        return

    row, column = position
    status = seats[row][column]

    print("\n" + "-" * 30)
    print(f"Seat Number : {seat_number.upper()}")

    if status == "X":
        print("Status      : BOOKED")
    else:
        print("Status      : AVAILABLE")

    print("-" * 30)


def show_statistics(seats):
    """Count booked/available seats by traversing the 2D list."""
    print("\n" + "=" * 45)
    print("             BOOKING STATISTICS")
    print("=" * 45)

    total_seats = ROWS * COLUMNS
    booked_seats = 0
    available_seats = 0

    for row in seats:
        for seat in row:
            if seat == "X":
                booked_seats += 1
            else:
                available_seats += 1

    occupancy = (booked_seats / total_seats) * 100

    print(f"\nTotal Seats       : {total_seats}")
    print(f"Booked Seats      : {booked_seats}")
    print(f"Available Seats   : {available_seats}")
    print(f"Occupancy         : {occupancy:.2f}%")
    print("=" * 45)


def show_menu():
    """Display the main menu."""
    print("\n")
    print("=" * 45)
    print("       CINEMA SEAT BOOKING SYSTEM")
    print("=" * 45)
    print("1. View Seats")
    print("2. Book Seat")
    print("3. Cancel Booking")
    print("4. Search Seat")
    print("5. Booking Statistics")
    print("6. Exit")
    print("=" * 45)


def main():
    """Run the Cinema Seat Booking System."""
    seats = create_seat_matrix()

    print("\nWelcome to the Cinema Seat Booking System!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            display_seats(seats)

        elif choice == "2":
            book_seat(seats)

        elif choice == "3":
            cancel_booking(seats)

        elif choice == "4":
            search_seat(seats)

        elif choice == "5":
            show_statistics(seats)

        elif choice == "6":
            print("\nThank you for using the Cinema Seat Booking System!")
            print("Program ended.")
            break

        else:
            print("\nInvalid choice.")
            print("Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
