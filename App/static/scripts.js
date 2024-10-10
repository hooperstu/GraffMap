{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 // static/js/scripts.js\
\
// Define icons for normal and done pins\
var defaultIcon = L.icon(\{\
    iconUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png',\
    shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png'\
\});\
\
var doneIcon = L.icon(\{\
    iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-green.png',\
    shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png'\
\});\
\
// Initialize map centered on Wokingham\
var map = L.map('map').setView([51.4103, -0.8351], 13);\
\
// Load and display tile layers on the map\
L.tileLayer('https://\{s\}.tile.openstreetmap.org/\{z\}/\{x\}/\{y\}.png', \{\
    maxZoom: 19,\
\}).addTo(map);\
\
// Fetch existing pins and add them to the map\
fetch('/pins')\
    .then(response => response.json())\
    .then(data => \{\
        data.pins.forEach(pin => \{\
            createPin(pin);\
        \});\
    \});\
\
// Add new pins on map click\
map.on('click', function (e) \{\
    var description = prompt("Enter a description for the new pin:");\
    if (description) \{\
        fetch('/pins', \{\
            method: 'POST',\
            headers: \{\
                'Content-Type': 'application/json'\
            \},\
            body: JSON.stringify(\{\
                latitude: e.latlng.lat,\
                longitude: e.latlng.lng,\
                description: description\
            \})\
        \}).then(response => response.json()).then(data => \{\
            createPin(\{\
                id: data.pin.id,\
                latitude: e.latlng.lat,\
                longitude: e.latlng.lng,\
                description: description,\
                done: false\
            \});\
        \});\
    \}\
\});\
\
// Create a pin on the map\
function createPin(pin) \{\
    var marker = L.marker([pin.latitude, pin.longitude], \{\
        icon: pin.done ? doneIcon : defaultIcon\
    \}).addTo(map);\
\
    marker.bindPopup(`\
        <b>$\{pin.description\}</b><br>\
        <button onclick="markDone($\{pin.id\})">Mark as Done</button><br>\
        <button onclick="deletePin($\{pin.id\})">Delete</button>\
    `);\
\}\
\
// Mark a pin as done\
function markDone(pinId) \{\
    fetch(`/pins/$\{pinId\}/mark_done`, \{ method: 'POST' \}).then(() => \{\
        location.reload();\
    \});\
\}\
\
// Delete a pin\
function deletePin(pinId) \{\
    fetch(`/pins/$\{pinId\}`, \{ method: 'DELETE' \}).then(() => \{\
        location.reload();\
    \});\
\}\
}