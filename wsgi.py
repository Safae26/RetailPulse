import sys
import os
from pathlib import Path

# Fix paths
sys.path.insert(0, str(Path(__file__).parent / 'app'))

from app.app import app as application