from datetime import datetime
import time
from cli import cli

g = cli(debug=True, speed=2)

class FlaskGlaceon:

    def __init__(self, glaceon_instance):
        self.g = glaceon_instance

    def info(self, message):
        self.g.print("INFO", message)

    def warning(self, message):
        self.g.print("WARNING", message)

    def error(self, message):
        self.g.print("ERROR", message)

    def success(self, message):
        self.g.print("SUCCESS", message)

    def debug(self, message):
        self.g.print("DEBUG", message)

