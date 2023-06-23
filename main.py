from flask import Flask, render_template, request, url_for, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_db.sqlite'
app.config['SQLALCHEMY_BINDS'] = {
        'db2': 'sqlite:///games_db.sqlite'

}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


class Games(db.Model):
    __bind_key__ = 'db2'
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(50))
    Ranking = db.Column(db.Float)
    Info = db.Column(db.String(20))


# with app.app_context():
#     db.create_all(bind_key='db2')


@app.route('/', methods=['POST', 'GET'])
def home():
    logmail = request.form.get('logmail')
    logpassword = request.form.get('logpassword')
    login_mail = Users.query.filter_by(email=logmail).first
    session['logmail'] = logmail
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    conf_pass = request.form.get('password1')
    if request.method == 'POST':
        if not name:
            if request.method == 'POST':
                logmail = request.form.get('logmail')
                logpassword = request.form.get('logpassword')
                login_mail = Users.query.filter_by(email=logmail).first()
                if login_mail:
                    if check_password_hash(login_mail.password, logpassword):
                        return redirect('/home')
                    else:
                        flash('Password is not correct!', category='error')
            return render_template('index.html')

        else:
            if len(email) > 0 and (len(password) > 0 and len(name) > 0):
                check_mail = Users.query.filter_by(email=email).first()
                new_user = Users(email=email, name=name, password=generate_password_hash(password, method="sha256"))
                if check_mail:
                    flash('Email is already registered', category='error')

                else:
                    if password == conf_pass:
                        db.session.add(new_user)
                        db.session.commit()
                        flash('Registered successfully!', category='success')
                    else:
                        flash('Password confrimation is not correct', category='error')

    return render_template('index.html')


@app.route('/list', methods=['POST', 'GET'])
def list():
    return render_template('list.html')


@app.route('/scrap', methods=['POST', 'GET'])
def scrap():
    if request.method == 'POST':
        game_name = request.form.get('gamegame')
        game_ranking = request.form.get('ranking1')
        game_info = request.form.get('info1')
        if len(game_info) > 0 and (len(game_ranking) > 0 and len(game_name) > 0):
            new_game = Games(Title=game_name, Ranking=game_ranking, Info=game_info)
            db.session.add(new_game)
            db.session.commit()

    return render_template('scrap.html')


@app.route("/logout",methods=['POST','GET'])
def logout():
    session['logmail'] = " "
    logmail = request.form.get('logmail')
    logpassword = request.form.get('logpassword')
    login_mail = Users.query.filter_by(email=logmail).first
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    conf_pass = request.form.get('password1')
    if request.method == 'POST':

        if not name:
            if request.method == 'POST':
                session['logmail'] = logmail
                logmail = request.form.get('logmail')
                logpassword = request.form.get('logpassword')
                login_mail = Users.query.filter_by(email=logmail).first()
                if login_mail:
                    if check_password_hash(login_mail.password, logpassword):
                        return redirect('/home')
                    else:
                        flash('Password is not correct!', category='error')
            return render_template('index.html')

        else:
            if len(email) > 0 and (len(password) > 0 and len(name) > 0):
                check_mail = Users.query.filter_by(email=email).first()
                new_user = Users(email=email, name=name, password=generate_password_hash(password, method="sha256"))
                if check_mail:
                    flash('Email is already registered', category='error')

                else:
                    if password == conf_pass:
                        db.session.add(new_user)
                        db.session.commit()
                        flash('Registered successfully!', category='success')
                    else:
                        flash('Password confrimation is not correct', category='error')

    return render_template('index.html')


@app.route('/home', methods=['POST', 'GET'])
def homee():
    games = db.session.execute(db.select(Games)
                               .order_by()).scalars()
    return render_template('home.html', games=games)




@app.route("/db",methods = ["POST",'GET'])
def database():
    return render_template('Db.html')

if __name__ == '__main__':
    app.run(debug=True)
