import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Target URL for data extraction (Sample test website)
url = "http://books.toscrape.com/"

# 2. Send HTTP GET request to the target website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Page loaded successfully!")
    
    # 3. Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    data_list = []
    
    # 4. Extract target data (Book titles and prices)
    products = soup.find_all("article", class_="product_pod")
    
    for item in products:
        title = item.h3.a["title"]
        price = item.find("p", class_="price_color").text
        
        data_list.append({
            "Title": title,
            "Price": price
        })
    
    # 5. Convert extracted data to Pandas DataFrame and export to CSV
    df = pd.DataFrame(data_list)
    df.to_csv("scraped_data.csv", index=False, encoding="utf-8")
    print("Data successfully saved to 'scraped_data.csv'!")

else:
    print(f"Failed to load page. Status code: {response.status_code}")