from flask import Flask, render_template, url_for, session, request, redirect

from pages.assignment10.assignment10 import assignment10

from utilities.db.db_manager import dbManager
import json

app = Flask(__name__)
app.secret_key = "mySecretKey"
app.register_blueprint(assignment10)

users = [{'firstname': 'noa', 'lastname': 'sarussy', 'email': 'noasarussy@gmail.com'},
         {'firstname': 'asaf', 'lastname': 'lotz', 'email': 'asaflotz@gmail.com'},
         {'firstname': 'moti', 'lastname': 'luhim', 'email': 'motiluhim@gmail.com'},
         {'firstname': 'avi', 'lastname': 'ron', 'email': 'aviron@gmail.com'}]


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/contacts-list', methods=['GET'])
def contact_list():
    return render_template('contacts-list.html')


@app.route('/assignment8', methods=['GET'])
def assignment8():
    return render_template('template.html', title='Hobbies')


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    current_method = request.method
    if current_method == 'GET':
        if 'firstname' in request.args:
            username = request.args['firstname']
            lastname = request.args['lastname']
            email = request.args['email']
            if not username and not lastname and not email:
                return render_template('assignment9.html', search=True, users=users)
            res = []
            for user in users:
                if username in ['', user['firstname']] and lastname in ['', user['lastname']] and email in ['', user[
                    'email']]:
                    res.append(user)
            if res:
                return render_template('assignment9.html', search=True, found=True, res=res)
            else:
                return render_template('assignment9.html', search=True, found=False)
        else:
            return render_template('assignment9.html')

    elif current_method == 'POST':
        if request.form['username']:
            session['username'] = request.form['username']
            session['isLogged'] = True
        return render_template('assignment9.html')


@app.route('/logout', methods=['GET'])
def logout():
    session['username'] = ''
    session['isLogged'] = False
    return redirect(url_for('assignment9'))


@app.route('/assignment11/users', methods=['GET'])
def ass11():
    return json.dumps(dbManager.get_all_users())


@app.route('/assignment11/users/selected/<int:user_id>', methods=['GET'])
def ass11_selected(user_id):
    u = dbManager.get_user(user_id)
    if len(u) > 0:
        return json.dumps(u[0])
    else:
        return json.dumps({"error": "user not found"})


@app.route('/assignment11/users/selected', methods=['GET'])
def ass11_selected_none():
    u = dbManager.get_all_users()
    if len(u) > 0:
        return json.dumps(u[-1])
    else:
        return json.dumps({"error": "no users in database"})


if __name__ == '__main__':
    app.run('localhost', 5555, debug=True)
