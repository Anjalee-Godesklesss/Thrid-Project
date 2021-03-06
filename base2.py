{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href='{% static 'css/bootstrap.css' %} '>
    <link rel="stylesheet" href='{% static 'css/bootstrap-css.map' %} '>
    <link rel="stylesheet" href='{% static 'css/bootstrap-css.min' %} '>
    <link rel="stylesheet" href='{% static 'css/bootstrap-min.css.map' %} '>
    <link rel="stylesheet" href='{% static 'css/bootstrap-grid-css' %} '>
    <link rel="stylesheet" href='{% static 'css/bootstrap-grid-css.map' %} '>
    <link rel="stylesheet" href='{% static 'css/bootstrap-grid-min.css' %} '>
    <link rel="stylesheet" href='{% static 'css/bootstrap-grid-min.css.map' %} '>
    <link rel="stylesheet" href='{% static 'css/bootstrap-reboot.css' %} '>
    <link rel="stylesheet" href='{% static 'css/bootstrap-reboot.css.map' %} '>
    <link rel="stylesheet" href='{% static 'css/bootstrap-reboot.min.css' %} '>
    <link rel="stylesheet" href='{% static 'css/bootstrap-reboot.min.css.map' %} '>



    <title>Static files</title>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
  </head>
  <body>
    <h1>Hello, world!</h1>
  {% block content %}

  {% for i in post %}
  <b>Title {{i.title}}<br>
  Description : {{i.description}}<br>
  Author : <i>{{i.author}}</i>
  Craeted_at :<b><h6>{{i.created_at}}</b></h6>

  {% endfor %}
  </body>
  <scrpit src="{% static 'js/bootstrap.bundle.js' %}"></scrpit>
  <scrpit src="{% static 'js/bootstrap.bundle.js.map' %}"></scrpit>
  <scrpit src="{% static 'js/bootstrap.bundle.min.js' %}"></scrpit>
  <scrpit src="{% static 'js/bootstrap.bundle.min.js.map' %}"></scrpit>
  <scrpit src="{% static 'js/bootstrap.bootstrap.js' %}"></scrpit>
  <scrpit src="{% static 'js/bootstrap.bootstrap.js.map' %}"></scrpit>
  <scrpit src="{% static 'js/bootstrap.bootstrap.min.js' %}"></scrpit>
  <scrpit src="{% static 'js/bootstrap.bootstrap.min.js.map' %}"></scrpit>

</html>