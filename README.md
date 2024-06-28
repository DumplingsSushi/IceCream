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
    git clone https://github.com/DumplingsSushi/IceCream/tree/main/Ice
    cd Ice
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

2. Run the database setup file:
    ```bash
    python BasicEntry.py
    ```
3. Run the application:
    ```bash
    python icecream.py
    ```

##Testing 

1. Once the application is running you'll find an interface with 3 tabs namely shop allergen and cart.
2. Under shop you have a button to add to the cart which adds the entry to the cart on the clock of the button, the entry is automatically made in the cart tab, and in case of multiple entries the quantity column next to the name of the entry increases.
3. The allergen tab gives you the ingredients that are used at the parlor and could have a side-effect if consumed by a person with a specific allergy and has a text box that allows you to add allergens with the allergen's name and description although the app has to be restarted once the entry is done to see the changes.
4. On the cart tab I've given a remove button that removes an entry from the cart and if there are entries with quantities higher than 1 it reduces the quantity count by 1, the order button given below the entries is only visible if there are  entries in the cart.
## Usage

- **Shop Tab**: Browse through different ice cream varieties by season and add them to your cart.
- **Allergen Tab**: View the list of common allergens and add new allergens.
- **Cart Tab**: Review your selected items and remove items if needed.



