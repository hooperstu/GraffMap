{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh15340\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # config.py\
\
import os\
\
class Config:\
    """Base configuration class."""\
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///pins.db'\
    SQLALCHEMY_TRACK_MODIFICATIONS = False\
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'\
    UPLOAD_FOLDER = 'static/uploads'\
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB file upload limit\
\
class DevelopmentConfig(Config):\
    """Development-specific configuration."""\
    DEBUG = True\
\
class ProductionConfig(Config):\
    """Production-specific configuration."""\
    DEBUG = False\
\
# Dictionary to map environment name to configuration class\
config = \{\
    'development': DevelopmentConfig,\
    'production': ProductionConfig,\
    'default': DevelopmentConfig\
\}\
}