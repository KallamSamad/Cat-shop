# Cat Shop

## Project Overview
The **Cat Shop** project is a Python-based simulation that allows users to browse and purchase cats based on various attributes, such as breed, color, age, weight, and gender. The program provides a catalog of cats, filters them according to the user’s preferences, manages the user's budget, and generates a receipt after each purchase.

## Features
- **Cat Catalog**: Displays a catalog of available cat breeds with their prices.
- **User Preferences**: Users can specify preferences like breed, color, age, weight, and gender to narrow down the selection.
- **Cat Search and Filtering**: Filters available cats based on the user’s input to show only matching options.
- **Budget Management**: Tracks and updates the user's budget after each purchase.
- **Receipt Generation**: Generates a receipt with details of the purchased cat and the remaining budget.

## Pros
- **Interactive Experience**: The app engages users by prompting them for input and showing real-time results based on their preferences.
- **Customizable Filtering**: Users can filter cats by multiple attributes like breed, color, age, and gender.
- **Simple and Fun**: With minimal setup, users can easily browse the catalog and make purchases.
- **Budget Tracking**: The program ensures that the user stays within their specified budget and updates the remaining balance after each purchase.
- **Receipt Generation**: A receipt is generated after each purchase, summarizing the transaction and remaining budget.

## Cons
- **Hardcoded Data**: The available breeds and prices are fixed in the code and cannot be dynamically updated without modifying the source.
- **No Real Transactions**: This is a simulation, so no real financial transactions are involved.
- **Text-Based Interface**: The interaction is text-based, and there's no graphical user interface (GUI).
- **Limited Error Handling**: While basic validation is implemented, there’s room for further improvements in error handling and user experience features.

## How It Works
1. **Introduction**: The user is greeted with their initial budget and shown a catalog of cats with details on available breeds and colors.
2. **User Input**: The user specifies their preferences by entering values for breed, color, age, weight, and gender.
3. **Filtering**: Based on the user's input, the application filters the catalog and shows the available cats that match the criteria.
4. **Purchase and Checkout**: The user selects a cat, adds it to their basket, and proceeds to checkout. The program updates the user's remaining budget after each purchase.
5. **Receipt Generation**: After a purchase, the user has the option to generate a receipt with a breakdown of the purchase and the remaining budget.
6. **Retry or Exit**: After completing a purchase, the user can choose to continue shopping or exit the program.

## Example of Usage
1. **Run the Program**: Start the Python script.
2. **Browse the Catalog**: The program will display a list of available cats with their details and prices.
3. **Enter Preferences**: The user is prompted to input their preferences, such as breed, color, age, and weight.
4. **Filter Results**: Based on the input, the application filters and shows matching cats.
5. **Add to Basket**: The user selects a cat and adds it to their shopping basket.
6. **Checkout**: The user proceeds to checkout, seeing a breakdown of their purchase and remaining budget.
7. **Receipt**: Optionally, a receipt is generated for the transaction.

## Example Workflow

- **Step 1**: The user enters their budget.
- **Step 2**: The user browses the catalog, selecting preferences (breed, color, etc.).
- **Step 3**: Cats are filtered based on the input.
- **Step 4**: The user chooses a cat and adds it to the basket.
- **Step 5**: The user checks out, and the budget is updated.
- **Step 6**: A receipt is generated and saved.

## Technologies Used
- **Python**: The core language used to build the application.
- **Pandas**: Used for handling data related to the catalog.
- **Matplotlib/Seaborn**: Libraries used for possible data visualization (not shown in the code but can be added for analysis).

## Future Improvements
- **Graphical User Interface (GUI)**: A graphical interface could be added for a more user-friendly experience.
- **Dynamic Data**: Instead of hardcoding the cat breeds and prices, data could be fetched from an external source (like a database or API).
- **Error Handling**: Enhanced error handling and input validation could be implemented for a more robust user experience.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
