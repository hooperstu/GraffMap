{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # app/models.py\
from app import db\
from datetime import datetime\
\
class Pin(db.Model):\
    id = db.Column(db.Integer, primary_key=True)\
    latitude = db.Column(db.Float, nullable=False)\
    longitude = db.Column(db.Float, nullable=False)\
    description = db.Column(db.String(255))\
    photos = db.relationship('Photo', backref='pin', lazy=True)\
    done = db.Column(db.Boolean, default=False)\
    deleted = db.Column(db.Boolean, default=False)\
    created_at = db.Column(db.DateTime, default=datetime.utcnow)\
\
class Photo(db.Model):\
    id = db.Column(db.Integer, primary_key=True)\
    pin_id = db.Column(db.Integer, db.ForeignKey('pin.id'), nullable=False)\
    url = db.Column(db.String(255), nullable=False)\
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)\
}