# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('db.sqlite3')  # Connects to or creates a SQLite database file
    c = conn.cursor()
    
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY, 
                    name TEXT, 
                    email TEXT, 
                    phone TEXT, 
                    date TEXT, 
                    time TEXT, 
                    comments TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY, 
                    name TEXT, 
                    review_text TEXT, 
                    rating INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS testimonials (
                    id INTEGER PRIMARY KEY, 
                    name TEXT, 
                    testimonial_text TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY, 
                    name TEXT, 
                    email TEXT, 
                    message TEXT)''')
    
    conn.commit()
    conn.close()
