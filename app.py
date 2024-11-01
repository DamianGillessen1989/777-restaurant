# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT, date TEXT, time TEXT, comments TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY, name TEXT, review_text TEXT, rating INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS testimonials (id INTEGER PRIMARY KEY, name TEXT, testimonial_text TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, email TEXT, message TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Routes for each page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        # Save review details to the database
        pass  # Complete with review logic below
    return render_template('reviews.html')

@app.route('/testimonials', methods=['GET', 'POST'])
def testimonials():
    if request.method == 'POST':
        # Save testimonial details to the database
        pass  # Complete with testimonials logic below
    return render_template('testimonials.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Save contact details to the database
        pass  # Complete with contact logic below
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        comments = request.form['comments']
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("INSERT INTO bookings (name, email, phone, date, time, comments) VALUES (?, ?, ?, ?, ?, ?)", 
                  (name, email, phone, date, time, comments))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('booking.html')
