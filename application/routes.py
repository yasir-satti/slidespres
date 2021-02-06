# import render_template function from the flask module
from flask import render_template, redirect, url_for, request

# import the app object from the ./application/__init__.py
from application.models import Slides
from application import app, db

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Golden Shoe Presentation')


"""
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hash_pw
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('activityadd'))
    return render_template('register.html', title='Register', form=form)
    

@app.route('/activityadd', methods=['GET', 'POST'])
@login_required
def activityadd():
    form = AddForm()
    if form.validate_on_submit():
        activityData = Activity(
            activityDesc=form.activityDesc.data
        )
        db.session.add(activityData)
        db.session.commit()
        act = Activity.query.filter_by(activityDesc=form.activityDesc.data).all()
        activRef = act[-1].id

        activitiesData = Activities(
            activity_ref=activRef,
            user_ref=current_user.id,
            ObjRating=form.objRating.data,
            JoyRating=form.joyRating.data
        )  
        db.session.add(activitiesData)
        db.session.commit()        
        return redirect(url_for('home'))    
    else:
        print(form.errors)    
    return render_template('activityadd.html', title='Add New Activity', form=form)
"""

@app.route('/slideDisplay', methods=['GET', 'POST'])
def slideDisplay():
    slideData = db.session.query(Slides).filter_by(slideID=1).all()
    return render_template('slideDisplay.html', title='Slide title', slideData=slideData)

"""
@app.route('/activitymd', methods=['GET', 'POST'])
@login_required
def activitymd():
    form = ModifyForm()
    data = db.session.query(Activities).first()
    if form.validate_on_submit():
        data.activityDesc=form.activityDesc.data
        data.ObjRating=form.objRating.data
        data.JoyRating=form.joyRating.data  
        db.session.commit()        
        return redirect(url_for('home'))
    elif request.method == 'GET':
        user = data.user_id
        form.activityDesc.data=data.activityDesc
        form.objRating.data=data.ObjRating
        form.objRating.data=data.ObjRating
        form.joyRating.data=data.JoyRating
        return render_template('activitymd.html', title='Modify Activity - Select user', form=form, user=user, data=data)
    else:
        print(form.errors)    
    return render_template('activitymd.html', title='Modify Activity')

@app.route('/activitydelete', methods=['GET', 'POST'])
@login_required
def activitydelete():
    form = DeleteForm()
    if form.validate_on_submit():
        data = Activities.query.first()
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        data = Activities.query.first()
        user = data.user_id
        form.activityDesc.data=data.activityDesc,
        form.objRating.data=data.ObjRating,
        form.joyRating.data=data.JoyRating
        return render_template('activitydelete.html', title='Delete Activity', form=form, user=user, data=data)
    else:
        print(form.errors)    
    return render_template('activitydelete.html', title='Delete Activity', form=form)

@app.route('/activitydelete/button', methods=["GET", "POST"])
@login_required
def activitydeleteButton(): 
    activity = Activities.query.first()
    db.session.delete(activity)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
    """
