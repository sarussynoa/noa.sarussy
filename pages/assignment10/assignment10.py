from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager

assignment10 = Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
    static_url_path='/pages/assignment10',
    template_folder='templates'
)


@assignment10.route('/assignment10', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    current_method = request.method

    if current_method == 'GET':
        return render_template('assignment10.html', action='select', users=dbManager.get_all_users(), res=None)

    elif current_method == 'POST':
        if request.form['type'] == 'insert':
            # insert query
            sql = 'insert into users (firstname, lastname, email) values (%s, %s, %s)'
            val = (request.form.get('firstname') or '', request.form.get('lastname') or '', request.form.get('email') or '')
            data = dbManager.commit(sql, val)
            return render_template('assignment10.html', action='insert', res=data, users=dbManager.get_all_users())

        elif request.form['type'] == 'update':
            # update query
            data, c = 0, 0
            sql = 'update users'
            val = ()
            for arg in request.form:
                if not request.form[arg] or arg == 'type' or arg == 'id':
                    continue
                c += 1
                if 'set' in sql:
                    sql += ','
                else:
                    sql += ' set'
                sql += f' {arg} = %s'
                val += (request.form[arg],)
            if c:
                sql += ' where id = %s'
                val += (request.form['id'],)
                data = dbManager.commit(sql, val)
            return render_template('assignment10.html', action='update', users=dbManager.get_all_users(), res=data)

        elif request.form['type'] == 'delete':
            # delete query
            sql = 'delete from users'
            val = ()
            for arg in request.form:
                if not request.form[arg] or arg == 'type':
                    continue
                if 'where' in sql:
                    sql += ' and'
                else:
                    sql += ' where'
                sql += f' {arg} = %s'
                val += (request.form[arg],)
            data = dbManager.commit(sql, val)
            return render_template('assignment10.html', action='delete', users=dbManager.get_all_users(), res=data)
