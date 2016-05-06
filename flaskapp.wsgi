#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)

# Dev
# sys.path.insert(0,"/var/www/FlaskApp/")
# from Blog import app as application

# Production
sys.path.insert(0,"/var/www/flask")
from memonimo import app as application

application.secret_key = 'memonimo secret key'
