import sys
from dotenv import load_dotenv

sys.path.insert(0, "lib/")

# Load .env variables
load_dotenv()

from main import app as application

if __name__ == "__main__":
    application.run()
