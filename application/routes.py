# import render_template function from the flask module
from flask import render_template, redirect, url_for, request

# import the app object from the ./application/__init__.py
from application.models import Slides
from application import app, db

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Golden Shoe Presentation: road to the future')
  
@app.route('/slide1', methods=['GET', 'POST'])
def slide1Display():
    slideData = db.session.query(Slides).filter_by(slideID=1).all()
    return render_template('slideDisplay.html', title='Current issues', slideData=slideData)

@app.route('/slide2', methods=['GET', 'POST'])
def slide2Display():
    slideData = db.session.query(Slides).filter_by(slideID=2).all()
    return render_template('slideDisplay.html', title='Critical issues', slideData=slideData)

@app.route('/slide3', methods=['GET', 'POST'])
def slide3Display():
    slideData = db.session.query(Slides).filter_by(slideID=3).all()
    return render_template('slideDisplay.html', title='Critical issues: Quick wins', slideData=slideData)

@app.route('/slide4', methods=['GET', 'POST'])
def slide4Display():
    slideData = db.session.query(Slides).filter_by(slideID=4).all()
    return render_template('slideDisplay.html', title='Transformation: Revenues', slideData=slideData)

@app.route('/slide5', methods=['GET', 'POST'])
def slide5Display():
    slideData = db.session.query(Slides).filter_by(slideID=5).all()
    return render_template('slideDisplay.html', title='Transformation: Online platform', slideData=slideData)

@app.route('/slide6', methods=['GET', 'POST'])
def slide6Display():
    slideData = db.session.query(Slides).filter_by(slideID=6).all()
    return render_template('slideDisplay.html', title='Transformation: Agile delivery', slideData=slideData)

@app.route('/slide7', methods=['GET', 'POST'])
def slide7Display():
    slideData = db.session.query(Slides).filter_by(slideID=7).all()
    return render_template('slideDisplay.html', title='Transformation: Talent upskilling', slideData=slideData)

@app.route('/slide8', methods=['GET', 'POST'])
def slide8Display():
    slideData = db.session.query(Slides).filter_by(slideID=8).all()
    return render_template('slideDisplay.html', title='Transformation: Customer engagement', slideData=slideData)
