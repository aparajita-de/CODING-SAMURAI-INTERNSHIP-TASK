# scraper.py - Advanced Menu Version
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

class WebScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.data = []
    
    def scrape_quotes(self):
        """Scrape quotes from quotes.toscrape.com"""
        print("\n🌐 Scraping quotes...")
        url = "http://quotes.toscrape.com"
        
        try:
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            quotes = soup.find_all('div', class_='quote')
            
            for quote in quotes:
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_='author').text
                tags = [tag.text for tag in quote.find_all('a', class_='tag')]
                
                self.data.append({
                    'type': 'quote',
                    'content': text,
                    'author': author,
                    'tags': ', '.join(tags),
                    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
            
            print(f"✅ Scraped {len(quotes)} quotes")
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def scrape_news(self):
        """Scrape headlines from Hacker News"""
        print("\n🌐 Scraping news headlines...")
        url = "https://news.ycombinator.com/"
        
        try:
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            headlines = soup.find_all('span', class_='titleline')
            
            for i, headline in enumerate(headlines[:10], 1):
                link = headline.find('a')
                title = link.text if link else "No title"
                
                self.data.append({
                    'type': 'news',
                    'title': title,
                    'source': 'Hacker News',
                    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
            
            print(f"✅ Scraped {min(10, len(headlines))} headlines")
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def save_to_csv(self):
        """Save data to CSV"""
        if not self.data:
            print("⚠️ No data to save!")
            return
        
        df = pd.DataFrame(self.data)
        filename = f"scraped_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(filename, index=False)
        print(f"✅ Saved to {filename}")
        print("\n📋 Preview:")
        print(df.head())
    
    def show_menu(self):
        """Display interactive menu"""
        while True:
            print("\n" + "="*50)
            print("ADVANCED WEB SCRAPER MENU")
            print("="*50)
            print("1. Scrape Quotes")
            print("2. Scrape News Headlines")
            print("3. Save Data to CSV")
            print("4. Show Current Data Count")
            print("5. Clear Data")
            print("6. Exit")
            
            choice = input("\nEnter choice (1-6): ").strip()
            
            if choice == '1':
                self.scrape_quotes()
            elif choice == '2':
                self.scrape_news()
            elif choice == '3':
                self.save_to_csv()
            elif choice == '4':
                print(f"📊 Current data: {len(self.data)} items")
            elif choice == '5':
                self.data = []
                print("✅ Data cleared")
            elif choice == '6':
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice")

if __name__ == "__main__":
    scraper = WebScraper()
    scraper.show_menu()