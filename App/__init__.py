{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # app/__init__.py\
from flask import Flask\
from flask_sqlalchemy import SQLAlchemy\
from config import config\
\
# Initialize Flask app\
app = Flask(__name__)\
\
# Load configuration from config.py\
env = os.environ.get('FLASK_ENV') or 'default'\
app.config.from_object(config[env])\
\
# Initialize the database\
db = SQLAlchemy(app)\
\
# Import routes and models\
from app import routes, models\
\
# Create the database tables\
db.create_all()\
}