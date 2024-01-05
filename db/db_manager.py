# db_manager.py

import json
import os
from .models import Article

class LocalMongoDBSimulator:
    def __init__(self, folder_path):
        """
        Initializes a LocalMongoDBSimulator instance.

        Args:
            folder_path (str): The path to the folder where the collections will be stored.
        """
        self.folder_path = folder_path

        # Create the directory if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

    def save_document(self, collection_name, document_id, document):
        """
        Saves a document in the specified collection.

        Args:
            collection_name (str): The name of the collection.
            document_id (str): The ID of the document.
            document (dict or str): The document to be saved. It can be a dictionary or a JSON string.

        Raises:
            ValueError: If the document is not a dictionary or a string.

        Returns:
            None
        """
        # Create a directory for the collection if it doesn't exist
        collection_path = os.path.join(self.folder_path, collection_name)
        os.makedirs(collection_path, exist_ok=True)

        # Convert the document to a JSON string
        if isinstance(document, dict):
            print(document)
            document_json = json.dumps(document)
        elif isinstance(document, str):
            document_json = document
        else:
            raise ValueError(f"Document must be a dict or a string, not {type(document)}")

        # Create a file for the document
        document_path = os.path.join(collection_path, f"{document_id}.json")
        with open(document_path, 'w') as document_file:
            document_file.write(document_json)

    def load_document(self, collection_name, document_id):
        """
        Loads a document from the specified collection.

        Args:
            collection_name (str): The name of the collection.
            document_id (str): The ID of the document.

        Returns:
            dict: The loaded document as a dictionary.
        """
        # Get the path to the document file
        document_path = os.path.join(self.folder_path, collection_name, f"{document_id}.json")

        # Load the document from the file
        with open(document_path, 'r') as document_file:
            document_json = document_file.read()

        return json.loads(document_json)


class DatabaseManager:
    def __init__(self, folder_path='data'):
        """
        Initializes the DatabaseManager with a local MongoDB simulator.
        """
        self.db = LocalMongoDBSimulator(folder_path)

    def add_article(self, article_data):
        """
        Adds a new article to the database.
        """
        article = Article(**article_data)
        self.db.save_document('articles', article.id, article.model_dump())

    def get_unprocessed_articles(self):
        """
        Retrieves all unprocessed articles from the database.
        """
        unprocessed_articles = []
        articles_path = os.path.join(self.db.folder_path, 'articles')
        for file_name in os.listdir(articles_path):
            with open(os.path.join(articles_path, file_name), 'r') as file:
                article_data = json.load(file)
                article = Article(**article_data)
                if not article.processed:
                    unprocessed_articles.append(article)
        return unprocessed_articles

    def mark_article_processed(self, article_id):
        """
        Marks an article as processed.
        """
        article_data = self.db.load_document('articles', article_id)
        article = Article(**article_data)
        article.processed = True
        self.db.save_document('articles', article.id, article.model_dump())

# Example usage
if __name__ == '__main__':
    db_manager = DatabaseManager(folder_path="/media/puneet/extdisk/test_rss_feed_data")
    # Add a new article example
    db_manager.add_article({
        'title': 'Sample Article',
        'source_feed': 'http://example.com/feed',
        'content': 'This is the content of the sample article.',
        'publication_date': "2023-01-01T00:00:00.000Z",
    })
    # Get unprocessed articles example
    print(db_manager.get_unprocessed_articles())
