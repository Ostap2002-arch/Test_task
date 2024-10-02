from dotenv import load_dotenv
import os


load_dotenv(encoding='1251')

DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD =os.environ.get("DB_PASSWORD")
DB_HOST =os.environ.get("DB_HOST")
DB_PORT =os.environ.get("DB_PORT")
DB_NAMEDB =os.environ.get("DB_NAMEDB")


DB_USER_TEST = os.environ.get("DB_USER_TEST")
DB_PASS_TEST = os.environ.get("DB_PASS_TEST")
DB_HOST_TEST = os.environ.get("DB_HOST_TEST")
DB_PORT_TEST = os.environ.get("DB_PORT_TEST")
DB_NAME_TEST = os.environ.get("DB_NAME_TEST")
