# Swiggy Menu Fetcher

This Python script fetches the menu of a restaurant from Swiggy's API and saves it to a CSV file.

## Overview

This script allows users to input a restaurant ID, fetches the menu data of that restaurant from Swiggy's API, and saves it to a CSV file. It utilizes the `requests` library to make HTTP requests and `pandas` to handle data manipulation and CSV file creation.

## Requirements

- Python 3.x
- requests library (`pip install requests`)
- pandas library (`pip install pandas`)

## Usage

- Clone the repository or download the script `swiggy_menu_fetch.py`.


1. **Install Dependencies**:
   - Make sure you have Python installed on your system.
   - Install the required dependencies using pip:
     ```
     pip install requests pandas
     ```

2. **Run the Script**:
   - Run the script `swiggy_menu.py`.
   - Enter the restaurant ID when prompted.

3. **Output**:
   - The script will save the menu data of the specified restaurant to a CSV file named `{restaurant_name}_menu.csv`.


## Example

```
python swiggy_menu.py
Enter the restaurant ID: 71320
CSV file saved successfully.
```
## Notes

- Ensure you have a stable internet connection to fetch the data from Swiggy's API.
- Restaurant IDs can be found by inspecting the URLs of restaurant pages on the Swiggy website.
- Make sure to provide a valid restaurant ID. If the provided ID is not valid, the script will raise an error.


## Author

K Y Nagarjuna
