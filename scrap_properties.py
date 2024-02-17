import requests
from bs4 import BeautifulSoup
import csv

def scrape_house_data(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all house listings
    listings = soup.find_all('div', class_='property-list-item')
    
    house_data = []
    for listing in listings:
        # Extract price
        price_tag = listing.find('div', class_='property-price')
        price = price_tag.text.strip() if price_tag else 'N/A'
        
        # Extract location
        location_tag = listing.find('div', class_='property-location')
        location = location_tag.text.strip() if location_tag else 'N/A'
        
        # Extract number of bedrooms
        bedrooms_tag = listing.find('div', class_='property-beds')
        bedrooms = bedrooms_tag.text.strip() if bedrooms_tag else 'N/A'
        
        # Extract size
        size_tag = listing.find('div', class_='property-size')
        size = size_tag.text.strip() if size_tag else 'N/A'
        
        # Extract description
        description_tag = listing.find('div', class_='property-description')
        description = description_tag.text.strip() if description_tag else 'N/A'
        
        # Extract amenities
        amenities_tag = listing.find('ul', class_='property-amenities')
        amenities = [item.text.strip() for item in amenities_tag.find_all('li')] if amenities_tag else []
        
        # Construct house data dictionary
        house = {
            'Price': price,
            'Location': location,
            'Bedrooms': bedrooms,
            'Size': size,
            'Description': description,
            'Amenities': amenities
        }
        
        house_data.append(house)
    
    return house_data

# Example URL of the real estate listing website
url = 'https://www.buyrentkenya.com/houses-for-sale'

# Call the function to scrape data
house_data = scrape_house_data(url)

# Define the CSV file name
csv_file = 'house_data_buyrentkenya.csv'

# Write the scraped data to a CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Price', 'Location', 'Bedrooms', 'Size', 'Description', 'Amenities'])
    writer.writeheader()
    for house in house_data:
        writer.writerow(house)

print(f"Scraped data saved to '{csv_file}'")
