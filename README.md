<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<!-- PROJECT LOGO -->
<div align="center">
  <h3 align="center">A ToDo application built using FastAPI, SQLAlchemy and a choice of either SQLite or MYSQL Databse for persisiting the Blogs.</h3>

  <p align="center">
    <br />
    <a href="https://fastapi.tiangolo.com"><strong>Explore the FastAPI docs »</strong></a>
    <br/>
  </p>
</div>

---

**Documentation**: <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a>

**Source Code**: <a href="https://github.com/erabhisheksingh/fastapi-blog-app" target="_blank">https://github.com/erabhisheksingh/fastapi-blog-app</a>

---

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. This project uses FastAPI to create and expose the APIs and SQLAlchemy to handle the ORM operations. The user also gets a choice to persist the data in either SQLite or MySQL Database.  

The key features are:

* **Fast**: Very high performance, due to FastAPI.
* **Choice of DB**: Choice of DB  
* **Fewer bugs**: Reduce about 40% of human (developer) induced errors. *
* **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (previously known as Swagger) and <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

---

## 🔧 Technologies & Tools
</br>
<p  align='left'>
<a href="https://github.com/erabhisheksingh/"><img src="https://img.shields.io/badge/-Python-white?logo=python&logoColor=blue&style=flat-square" alt="Python Badge"/></a>&nbsp;&nbsp;
<a href="https://github.com/erabhisheksingh/"><img src="https://img.shields.io/badge/-FastAPI-white?logo=fastapi&logoColor=#009999&style=flat-square" alt="FastAPI Badge"/></a>&nbsp;&nbsp;
<a href="https://github.com/erabhisheksingh/"><img src="https://img.shields.io/badge/-MySQL-white?logo=mysql&logoColor=blue&style=flat-square" alt="MySQL Badge"/></a>
<a href="https://github.com/erabhisheksingh/"><img src="https://img.shields.io/badge/-SQLite-white?logo=sqlite&logoColor=blue&style=flat-square" alt="SQLite Badge"/></a>&nbsp;&nbsp;
<a href="https://github.com/erabhisheksingh/"><img src="https://img.shields.io/badge/-Docker-white?logo=docker&logoColor=blue&style=flat-square" alt="Docker Badge"/></a>&nbsp;&nbsp;
</p>

---
## **Requirements**

Python 3.6+

FastAPI stands on the shoulders of giants:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> for the web parts.
* <a href="https://pydantic-docs.helpmanual.io/" class="external-link" target="_blank">Pydantic</a> for the data parts.

## Installation

```console
$ python -m venv venv

---> 100%
```

You will need to activate the Virtual environment using the below command

```console
$ source venv/bin/activate 

---> 100%
```

Then install the packages from the requirements.txt

```console
$ pip install -r requirements.txt

---> 100%
```

To create a Docker image using the Dockerfile, use the below command

```console
$ docker build --tag fastapi-blog-api:0.0.1 -f Dockerfile .  

```

To check the Docker image, use the below command

```console
$ docker container ls -a  

```

Then run the Docker container, use the below command

```console
$  docker run -p8000:8000 fastapi-blog-api:0.0.1 

```

**Note**:

### Check it

Open your browser at <a href="http://127.0.0.1:8000/blogs/all" class="external-link" target="_blank">http://127.0.0.1:8000/blogs</a>

You will see the JSON response as:

```JSON
[
    {
        "published": true,
        "title": "The Dark Knight",
        "body": "This blog is on Batman and his fight against Evil",
        "author": "Bruce Wayne",
        "id": 1
    }
]
```
</br>

---
You have an API that:

* Receives HTTP requests in the _paths_ `/blogs` and `/blogs/{id}`.
* The _paths_ take `GET`, `POST`, `PUT` and `DELETE` <em>operations</em> (also known as HTTP _methods_).
* The _path_ `/blogs/{id}` has a _path parameter_ `id` that should be an `int`.

---

### Interactive API docs
</br>

Now go to <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

### Alternative API docs

And now, go to <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>)

### Interactive API docs upgrade

Now go to <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

* The interactive API documentation will be automatically updated, including the new body:

* Click on the button "Try it out", it allows you to fill the parameters and directly interact with the API:

* Then click on the "Execute" button, the user interface will communicate with your API, send the parameters, get the results and show them on the screen:

### Alternative API docs upgrade

And now, go to <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

* The alternative documentation will also reflect the new query parameter and body:

## Optional Dependencies

Used by Pydantic:

* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - for faster JSON <abbr title="converting the string that comes from an HTTP request into Python data">"parsing"</abbr>.
* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email_validator</code></a> - for email validation.

Used by Starlette:

* <a href="https://requests.readthedocs.io" target="_blank"><code>requests</code></a> - Required if you want to use the `TestClient`.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - Required if you want to use the default template configuration.
* <a href="https://andrew-d.github.io/python-multipart/" target="_blank"><code>python-multipart</code></a> - Required if you want to support form <abbr title="converting the string that comes from an HTTP request into Python data">"parsing"</abbr>, with `request.form()`.
* <a href="https://pythonhosted.org/itsdangerous/" target="_blank"><code>itsdangerous</code></a> - Required for `SessionMiddleware` support.
* <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" target="_blank"><code>pyyaml</code></a> - Required for Starlette's `SchemaGenerator` support (you probably don't need it with FastAPI).
* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - Required if you want to use `UJSONResponse`.

Used by FastAPI / Starlette:

* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - for the server that loads and serves your application.
* <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - Required if you want to use `ORJSONResponse`.

You can install all of these with `pip install "fastapi[all]"`.

## License

This project is licensed under the terms of the MIT license.