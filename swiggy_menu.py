import requests
import pandas as pd

def fetch_and_save_menu():
    try:
        # Prompt the user to input the restaurant ID
        restaurant_id = input("Enter the restaurant ID: ")

        # URL of the API endpoint
        url = f"https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=18.56&lng=73.95&restaurantId={restaurant_id}"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }

        # Send a GET request to the specified URL with headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Extract JSON data from the response
        json_data = response.json()

        # Check if the restaurant data is present in the JSON response
        if 'cards' not in json_data['data'] or not json_data['data']['cards']:
            raise ValueError("No restaurant found with the given ID.")

        # Extract restaurant name from the json response
        restaurant_name = json_data['data']['cards'][0]['card']['card']['info']['name']

        # Initialize lists to store extracted data
        menu_items = []

        # Extract relevant data and append to lists
        for card in json_data['data']['cards']:
            card_group_map = card.get('groupedCard', {}).get('cardGroupMap', {})
            regular_cards = card_group_map.get('REGULAR', {}).get('cards', [])
            for grouped_card in regular_cards:
                item_cards = grouped_card.get('card', {}).get('card', {}).get('itemCards', [])
                for item_card in item_cards:
                    if item_card.get('card', {}).get('@type') == 'type.googleapis.com/swiggy.presentation.food.v2.Dish':
                        dish_info = item_card.get('card', {}).get('info', {})
                        menu_items.append({
                            'Name': dish_info.get('name', ''),
                            'Category': dish_info.get('category', ''),
                            'Description': dish_info.get('description', 'No description'),
                            'Price': dish_info.get('price', 0) / 100  # Convert price to rupees
                        })

        # Create a DataFrame
        df = pd.DataFrame(menu_items)

        # Save DataFrame to CSV file
        df.to_csv(f'{restaurant_name}_menu.csv', index=False)

        print("CSV file saved successfully.")

    except requests.RequestException as e:
        print("Error accessing API:", e)
    except (KeyError, ValueError) as e:
        print("Error processing data from API:", e)

# Example usage
fetch_and_save_menu() 
