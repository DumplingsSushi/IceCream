# IceCream
A small application for an ice-cream parlor.

# Ice Cream Parlor Application

## Description
The Ice Cream Parlor application is a desktop GUI app built using customtkinter and SQLite. It allows users to browse different ice cream varieties based on seasons, view allergens, add items to the cart, and save new allergens to the database.

## Features
- **Shop Tab**: Displays ice cream varieties based on the season (Summer, Rainy, Winter).
- **Allergen Tab**: Shows a list of allergens used at the parlor and allows users to add new allergens.
- **Cart Tab**: Displays items added to the cart and allows users to remove items.

## Prerequisites
- Python 3.x
- customtkinter

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:
    ```bash
    pip install customtkinter
    ```

## Database Setup
 To create these tables and enter the required values, I've added a file named BasicEntry.py that allows you to create tables and enter the values needed before starting.
1. Create the SQLite database and tables:


    ```sql
    CREATE TABLE Varieties (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        variety_name TEXT NOT NULL,
        season TEXT NOT NULL,
        allergens TEXT
    );

    CREATE TABLE Allergy (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    );

    CREATE TABLE Cart (
        cartid INTEGER PRIMARY KEY AUTOINCREMENT,
        iceid INTEGER NOT NULL,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    );
    ```

3. Insert initial data into the `Varieties` and `Allergy` tables as required.

## Running the Application

1. Navigate to the project directory:
    ```bash
    cd <repository-directory>
    ```

2. Run the application:
    ```bash
    python icecream.py
    ```

## Usage

- **Shop Tab**: Browse through different ice cream varieties by season and add them to your cart.
- **Allergen Tab**: View the list of common allergens and add new allergens.
- **Cart Tab**: Review your selected items and remove items if needed.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

