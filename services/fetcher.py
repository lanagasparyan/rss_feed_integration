# fetcher.py

import feedparser
from db.db_manager import DatabaseManager
from config.config_manager import get_rss_feed_urls, get_database_path

class RSSFetcher:
    def __init__(self):
        """
        Initializes the RSS fetcher.
        """
        self.db_manager = DatabaseManager(folder_path=get_database_path())
        self.feed_urls = get_rss_feed_urls()

    def fetch_feeds(self):
        """
        Fetches articles from all the configured RSS feeds and stores them in the database.
        """
        for url in self.feed_urls:
            self.fetch_feed(url)

    def fetch_feed(self, feed_url):
        """
        Fetches articles from a single RSS feed and stores them in the database.
        """
        feed = feedparser.parse(feed_url)
        print(f"Found {len(feed.entries)} articles.")
        for entry in feed.entries:
            # Create a dictionary of the article data
            print(f"Adding article: {entry.title}")
            try:
                article_data = {
                    'title': entry.title,
                    'source_feed': entry.link,
                    'content': entry.summary,
                    'publication_date': entry.published,
                }
                # Store the article in the database
                self.db_manager.add_article(article_data)
            except Exception as e:
                print(f"Error adding article: {e}")

if __name__ == '__main__':
    fetcher = RSSFetcher()
    fetcher.fetch_feeds()
