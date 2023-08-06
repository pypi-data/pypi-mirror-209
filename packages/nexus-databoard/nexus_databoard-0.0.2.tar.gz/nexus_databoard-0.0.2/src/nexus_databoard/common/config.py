import abc
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


class Singleton(abc.ABCMeta, type):
    """
    Singleton metaclass for ensuring only one instance of a class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call method for the singleton metaclass."""
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


class AbstractSingleton(abc.ABC, metaclass=Singleton):
    pass

class Config(metaclass=Singleton):
    """
    Configuration class to store the state
    """

    def __init__(self):
        """Initialize the Config class"""
        self.debug_mode = False
        self.db_dialect = os.getenv("DB_DIALECT", "postgresql+psycopg2")
        self.db_host = os.getenv("DB_HOST", "localhost")
        self.db_port = os.getenv("DB_PORT", "5432")
        self.db_database = os.getenv("DB_DATABASE", "postgres")
        self.db_user = os.getenv("DB_USERNAME", "postgres")
        self.db_password = os.getenv("DB_PASSWORD", "postgres")
        self.mailgun_api_key = os.getenv("MAILGUN_API_KEY", "123123123")
        self.mailgun_api_url = os.getenv("MAILGUN_API_URL", "https://api.mailgun.net/v3/sandbox123123123.mailgun.org/messages")
        self.app_name = os.getenv("APP_NAME", "Savantly Nexus Analytics")
        self.app_description = os.getenv("APP_DESCRIPTION", """
        This application provides the boilerplate for building data science applications.
        """)
