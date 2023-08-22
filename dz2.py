<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Главная страница</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Мой сайт</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Главная</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">О нас</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <h1>Вебсайт</h1>
    <form action="">
        <div>
            <label for="textfield" class="lead">Логин</label>
            <input class="form-control" placeholder="Логин" type="text" id="textfield"><br>
        </div>
        <div>
            <label for="passfield" class="lead">Пароль</label>
            <input class="form-control" placeholder="Пароль" type="password" id="passfield"><br>
        </div>
        <div>
            <label for="textareafield" class="lead">Комментарий</label>
            <textarea class="form-control" placeholder="Введите комментарий" id="textareafield"></textarea><br>
        </div>
        <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" role="switch" id="checkfield">
            <label class="lead" for="checkfield">Согласен с политикой конфиденциальности</label>
        </div>
        <button type="button" class="btn btn-success">Войти</button>
    </form>
    <a href="page2.html">О сайте</a>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous"></script>
</body>
</html>
