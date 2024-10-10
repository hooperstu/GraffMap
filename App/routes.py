{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # app/routes.py\
from flask import render_template, request, jsonify\
from app import app, db\
from app.models import Pin, Photo\
\
@app.route('/')\
def index():\
    pins = Pin.query.filter_by(deleted=False).all()\
    return render_template('index.html', pins=pins)\
\
@app.route('/pins', methods=['POST'])\
def add_pin():\
    data = request.get_json()\
    pin = Pin(\
        latitude=data['latitude'],\
        longitude=data['longitude'],\
        description=data.get('description')\
    )\
    db.session.add(pin)\
    db.session.commit()\
    return jsonify(\{'status': 'success', 'pin': \{'id': pin.id\}\})\
\
@app.route('/pins/<int:pin_id>/photos', methods=['POST'])\
def add_photo(pin_id):\
    data = request.get_json()\
    photo = Photo(\
        pin_id=pin_id,\
        url=data['url']\
    )\
    db.session.add(photo)\
    db.session.commit()\
    return jsonify(\{'status': 'success', 'photo': \{'id': photo.id\}\})\
\
@app.route('/pins/<int:pin_id>', methods=['DELETE'])\
def delete_pin(pin_id):\
    pin = Pin.query.get(pin_id)\
    pin.deleted = True\
    db.session.commit()\
    return jsonify(\{'status': 'success'\})\
\
@app.route('/pins/<int:pin_id>/mark_done', methods=['POST'])\
def mark_done(pin_id):\
    pin = Pin.query.get(pin_id)\
    pin.done = True\
    db.session.commit()\
    return jsonify(\{'status': 'success'\})\
}