# my_first_scraper.py - COMPLETE WORKING VERSION
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

print("=" * 60)
print("WEB SCRAPING WITH BEAUTIFULSOUP")
print("=" * 60)

# Website to scrape
url = "http://quotes.toscrape.com"

print(f"\n🌐 Connecting to: {url}")

try:
    # headers to mimic a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    #to the website
    print("   Downloading webpage...")
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    
    print("✅ Connected successfully!")
    print(f"   Status code: {response.status_code}")
    
    # Parse the HTML
    print("   Parsing HTML...")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all quotes
    print("   Looking for quotes...")
    quotes = soup.find_all('div', class_='quote')
    
    if not quotes:
        print("❌ No quotes found! The website structure might have changed.")
    else:
        print(f"📊 Found {len(quotes)} quotes")
        print("\n" + "-" * 60)
        
        # Store data
        all_quotes = []
        
        for i, quote in enumerate(quotes, 1):
            # Get quote text
            text_elem = quote.find('span', class_='text')
            text = text_elem.text if text_elem else "No text"
            
            # Get author
            author_elem = quote.find('small', class_='author')
            author = author_elem.text if author_elem else "Unknown"
            
            # Get tags
            tags = []
            tag_elems = quote.find_all('a', class_='tag')
            for tag in tag_elems:
                tags.append(tag.text)
            
            # Display progress
            print(f"\n📝 Quote #{i}")
            print(f"   Author: {author}")
            print(f"   Text: {text[:60]}...")
            print(f"   Tags: {', '.join(tags) if tags else 'None'}")
            
            # Add to list
            all_quotes.append({
                'quote': text,
                'author': author,
                'tags': ', '.join(tags) if tags else '',
                'scrape_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
        
        print("\n" + "-" * 60)
        print(f"\n✅ Extracted {len(all_quotes)} quotes")
        
        # Save to CSV
        if all_quotes:
            filename = f"quotes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            print(f"\n💾 Saving to: {filename}")
            
            df = pd.DataFrame(all_quotes)
            df.to_csv(filename, index=False, encoding='utf-8')
            
            print(f"✅ Saved successfully!")
            print(f"📁 Location: {os.path.abspath(filename)}")
            
            # Preview
            print("\n📋 Preview of saved data:")
            print(df.head(3))
            
            # File info
            if os.path.exists(filename):
                size = os.path.getsize(filename)
                print(f"\n📊 File size: {size} bytes")
        else:
            print("❌ No data to save")

except requests.exceptions.ConnectionError:
    print("❌ Connection error! Check your internet connection.")
except requests.exceptions.Timeout:
    print("❌ Timeout error! The website is too slow.")
except requests.exceptions.RequestException as e:
    print(f"❌ Request error: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

print("\n" + "=" * 60)
print("🎉 Done!")
print("=" * 60)

# Keep window open if double-clicked
input("\nPress Enter to exit...")