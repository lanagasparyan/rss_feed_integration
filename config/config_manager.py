# config_manager.py

from dynaconf import Dynaconf
import os

# Initialize Dynaconf settings
settings = Dynaconf(
    settings_files=['settings.toml'],
)


def get_setting(key):
    """
    Retrieve a specific configuration setting.
    
    :param key: The key of the setting to retrieve.
    :return: The value of the setting.
    """
    return settings.get(key)

# Example usage functions for demonstration
def get_database_path():
    """
    Retrieve the database URL from the configuration.
    
    :return: The database URL as a string.
    """
    return get_setting("DATABASE_PATH")

def get_rss_feed_urls():
    """
    Retrieve the list of RSS feed URLs from the configuration.
    
    :return: A list of RSS feed URLs.
    """
    return get_setting("RSS_FEED_URLS")

# You can add more functions to retrieve other specific settings as needed