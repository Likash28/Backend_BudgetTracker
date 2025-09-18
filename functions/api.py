import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app
from mangum import Mangum

# Create the ASGI adapter for AWS Lambda/Netlify Functions
handler = Mangum(app)
