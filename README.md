<h1 align="center">AIRBnB CLONE</h1>

---
<p align="center">
<a target="_blank" href="https://www.github.com/"><img src="https://github.com/josephynaina/AirBnB_clone/blob/master/images/logo.png?raw=true"></a>
</p>
The goal of the project is to deploy on your server a simple copy of the AirBnB website.

At complition it will have
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

# The console
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

<p align="center">
<a target="_blank" href="https://www.github.com/josephynaina/AirBnB_clone/"><img src="https://github.com/josephynaina/AirBnB_clone/blob/master/images/image.png?raw=true"></a>
</p>

# Web static
- learn HTML/CSS
- create the HTML of your application
- create template of each object

# MySQL storage
- replace the file storage by a Database storage
- map your models to a table in database by using an O.R.M.

# Web framework - templating
- create your first web server in Python
- make your static HTML file dynamic by using objects stored in a file or database

# RESTful API
- expose all your objects stored via a JSON web interface
- manipulate your objects via a RESTful API

# Web dynamic
- learn JQuery
- load objects from the client side by using your own RESTful API

# THE COMMAND INTERPRETER

 Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
