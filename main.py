# main.py

from db.db_manager import DatabaseManager
from services.scheduler import main as scheduler_main
from utils.logger import setup_logger

def initialize_database():
    """
    Initializes the database by creating a new instance of the DatabaseManager.
    This ensures that all necessary tables are created before starting the application.
    """
    print("Initializing database...")
    DatabaseManager()

def start_scheduler():
    """
    Starts the scheduler for fetching articles.
    """
    print("Starting article fetch scheduler...")
    scheduler_main()

if __name__ == '__main__':
    # Setup logger
    logger = setup_logger('rss_feed_integration', 'logs/rss_feed_integration.log')
    logger.info('Starting RSS Feed Integration application.')

    try:
        # Initialize the database
        initialize_database()

        # Start the article fetching scheduler
        start_scheduler()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
