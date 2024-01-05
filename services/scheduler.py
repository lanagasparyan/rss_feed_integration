# scheduler.py

import time
import schedule
from .fetcher import RSSFetcher

def fetch_articles_job():
    """
    Job to fetch articles from RSS feeds.
    """
    fetcher = RSSFetcher()
    fetcher.fetch_feeds()
    print("Articles fetched successfully.")

def main():
    fetch_articles_job()
    # # Schedule the job (e.g., every hour)
    # schedule.every(1).hour.do(fetch_articles_job)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

if __name__ == '__main__':
    main()
