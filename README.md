1. POST <http://192.168.1.143:3005/api/createUser>

{

`    `"name":"Andrey",

`    `"email": "andr@qweasd",

`    `"password":"fLSDfgfd123",

`    `"group": "isp-320p",

`    `"iq": "200"

}

![](https://github.com/P1tirim/Flask/blob/main/images/0.png)

Пользователь добавлен, 200

1. PUT <http://192.168.1.143:3005/api/modifyUser/0>

{

`   `"name":"Ruslan"

}

![](https://github.com/P1tirim/Flask/blob/main/images/1.png)

Пользователь изменен, 200

1. GET <http://192.168.1.143:3005/api/users>

![](https://github.com/P1tirim/Flask/blob/main/images/2.png)

Данные пользователя, 200

1. DELETE - http://192.168.1.143:3005/api/deleteUser/0

![](https://github.com/P1tirim/Flask/blob/main/images/3.png)

1. POST - <http://192.168.1.143:3005/api/createMusic>

{

`    `"name":"We will Rock You",

`    `"group":"Queen"

}

![](https://github.com/P1tirim/Flask/blob/main/images/4.png)

Музыка добавлена, 200

1. PUT <http://192.168.1.143:3005/api/modifyMusic/0>

![](https://github.com/P1tirim/Flask/blob/main/images/5.png)

Музыка изменена, 200

1. GET http://192.168.1.143:3005/api/musics

![](https://github.com/P1tirim/Flask/blob/main/images/6.png)

Данные музыки, 200

1. DELETE <http://192.168.1.143:3005/api/deleteMusic/0>

![](https://github.com/P1tirim/Flask/blob/main/images/7.png)

Музыка удалена, 200

![](https://github.com/P1tirim/Flask/blob/main/images/8.png)

