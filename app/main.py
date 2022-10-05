from flask import Flask, request

app = Flask(__name__)

users = []
musics = []


class User(object):

    def __init__(self, name, email, password, group, iq):
        self.name = name
        self.email = email
        self.password = password
        self.group = group
        self.iq = iq


class Music(object):

    def __init__(self, name, group):
        self.name = name
        self.group = group


@app.route('/')
def routes():
    s = "http://192.168.1.143:3005/api/users - получить всех пользователей <br/> " \
        "http://192.168.1.143:3005/api/createUser - создать пользователя <br/> " \
        "http://192.168.1.143:3005/api/modifyUser/ - изменить данные пользователя <br/> " \
        "http://192.168.1.143:3005/api/deleteUser/ - удалить пользователя <br/> " \
        "http://192.168.1.143:3005/api/musics - Получить всю музыку <br/> " \
        "http://192.168.1.143:3005/api/createMusic - создать музыку <br/> " \
        "http://192.168.1.143:3005/api/modifyMusic/ - изменить музыку <br/> " \
        "http://192.168.1.143:3005/api/deleteMusic/ - удалить пользователя"
    return s

@app.route('/api/users')
def GET_Users():
    s = ''
    for u in users:
        user = u.name + " " + u.email + " " + u.password + " " + u.group + " " + u.iq
        s += user + "<br/>"

    return s, 200


@app.route('/api/musics')
def GET_Music():
    s = ''
    for m in musics:
        music = m.name + " " + m.group
        s += music + "<br/>"

    return s, 200


@app.route('/api/createUser', methods=['POST'])
def CreateUser():
    if request.method == 'POST':
        data = request.get_json()

        name = None
        email = None
        password = None
        group = None
        iq = None

        if data:
            if 'name' in data:
                name = data['name']
            else:
                return 'Не указоно имя', 400
            if 'email' in data:
                email = data['email']
            else:
                return 'Не указана почта', 400
            if 'password' in data:
                password = data['password']
            else:
                return 'Не указан пароль', 400
            if 'group' in data:
                group = data['group']
            else:
                return 'Не указана группа', 400
            if 'iq' in data:
                iq = data['iq']
            else:
                return 'Не указан iq', 400
        else:
            return 'Нет данных', 400

        if name and email and password and group and iq:
            user = User(name, email, password, group, iq)
            users.append(user)
            return 'Пользователь добавлен', 200
    return 'Данный запрос не поддерживается'


@app.route('/api/createMusic', methods=['POST'])
def CreateMusic():
    if request.method == 'POST':
        data = request.get_json()

        name = None
        group = None

        if data:
            if 'name' in data:
                name = data['name']
            else:
                return 'Не указоно имя', 400
            if 'group' in data:
                group = data['group']
            else:
                return 'Не указана группа', 400
        else:
            return 'Нет данных', 400

        if name and group:
            music = Music(name, group)
            musics.append(music)
            return 'Музыка добавлена', 200
    return 'Данный запрос не поддерживается'


@app.route('/api/modifyUser/<int:id>', methods=['PUT'])
def ModifyUser(id):
    if len(users) < id:
        return 'Пользователя с таким id нет', 400

    data = request.get_json()

    if data:
        if 'name' in data:
            users[id].name = data['name']
        if 'email' in data:
            users[id].email = data['email']
        if 'password' in data:
            users[id].password = data['password']
        if 'group' in data:
            users[id].group = data['group']
        if 'iq' in data:
            users[id].iq = data['iq']
    else:
        return 'Пустые данные', 400
    return 'Пользователь изменен', 200


@app.route('/api/modifyMusic/<int:id>', methods=['PUT'])
def ModifyMusic(id):
    if len(musics) < id:
        return 'Музыки с таким id нет', 400

    data = request.get_json()

    if data:
        if 'name' in data:
            musics[id].name = data['name']
        if 'group' in data:
            musics[id].group = data['group']
    else:
        return 'Пустые данные', 400
    return 'Музыка изменена', 200


@app.route('/api/deleteUser/<int:id>', methods=['DELETE'])
def deleteUser(id):
    if len(users) < id:
        return 'Пользователя с таким id нет', 400

    users.pop(id)
    return 'Пользователь удален', 200


@app.route('/api/deleteMusic/<int:id>', methods=['DELETE'])
def deleteMusic(id):
    if len(musics) < id:
        return 'Музыки с таким id нет', 400

    musics.pop(id)
    return 'Музыка удалена', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3005')


