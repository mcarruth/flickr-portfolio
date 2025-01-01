import sys

sys.path.insert(0, "lib/")

from main import app as application

if __name__ == "__main__":
    application.run()
