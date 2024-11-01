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

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        comments = request.form['comments']
        
        # Insert data into the database
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("INSERT INTO bookings (name, email, phone, date, time, comments) VALUES (?, ?, ?, ?, ?, ?)",
                  (name, email, phone, date, time, comments))
        conn.commit()
        conn.close()
        
        # Redirect to the home page or a confirmation page
        return redirect(url_for('index'))
    
    return render_template('booking.html')

@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        # Retrieve review data
        name = request.form['name']
        review_text = request.form['review_text']
        rating = request.form['rating']
        
        # Insert review into the database
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("INSERT INTO reviews (name, review_text, rating) VALUES (?, ?, ?)",
                  (name, review_text, rating))
        conn.commit()
        conn.close()
        
        # Redirect to the reviews page
        return redirect(url_for('reviews'))
    
    # Retrieve all reviews from the database to display on the page
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM reviews")
    reviews = c.fetchall()
    conn.close()
    
    return render_template('reviews.html', reviews=reviews)

@app.route('/testimonials', methods=['GET', 'POST'])
def testimonials():
    if request.method == 'POST':
        # Retrieve testimonial data
        name = request.form['name']
        testimonial_text = request.form['testimonial_text']
        
        # Insert testimonial into the database
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("INSERT INTO testimonials (name, testimonial_text) VALUES (?, ?)",
                  (name, testimonial_text))
        conn.commit()
        conn.close()
        
        return redirect(url_for('testimonials'))
    
    return render_template('testimonials.html')


