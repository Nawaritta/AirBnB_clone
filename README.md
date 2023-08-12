# The Console:

AirBnB_clone Alx School project

### Description:

The Airbnb clone project is a remake of the famous [_AirBnB_](airbnb.com) website, and it is split into multiple parts, the first of them being **The Console**.  
The console is an interface that is meant for the developer which makes interactions with the stored data more convenient.

### Usage:

##### Starting the command-line interpreter:

To start the console, run the `console.py` file, using either one the these commands:

```bash
$ ./console.py
$ python3 console.py
```

You can make sure you are inside the console once you see the following prompt

    (hbnb)

##### Available commands:

|command | usage | description|
|:------:|:------|:-----------|
|help    |`help` |shows commands and their function|
|quit    |`quit` |exits the console immediately|
|create  |`create <class_name>`|creates and saves a new instance of `class_name`|
|show    |`show <class_name> <id>`|shows the string representation of an already existing instance|
|destroy |`destroy <class_name> <id>`|deletes an instance from the _json_ data file|
|all     |`all [class_name]`|shows all the existing instances in the _json_ data file (optionaly showing only instance of `class_name`)|
|update  |`update <class_name> <id> <field_name> <value>`|updates a field of an existing instance and saves the changes to the _json_ data file|

##### Examples:

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help create
Creates and saves a new instance
(hbnb) create User
9042c6c4-f1f3-492c-9070-9e92f0c4e74d
(hbnb) show User 9042c6c4-f1f3-492c-9070-9e92f0c4e74d
[User] (9042c6c4-f1f3-492c-9070-9e92f0c4e74d) {'id': '9042c6c4-f1f3-492c-9070-9e92f0c4e74d', 'created_at': datetime.datetime(2023, 8, 12, 16, 41, 53, 177397), 'updated_at': datetime.datetime(2023, 8, 12, 16, 41, 53, 181090)}
(hbnb) create Place
b37d688e-33f0-4b1a-a6c4-e38bc7425aa3
(hbnb) all
["[User] (6f5fe2b4-5d91-4172-b184-d825dc623cac) {'id': '6f5fe2b4-5d91-4172-b184-d825dc623cac', 'created_at': datetime.datetime(2023, 8, 12, 16, 14, 10, 749688), 'updated_at': datetime.datetime(2023, 8, 12, 16, 14, 10, 749718)}", "[User] (9042c6c4-f1f3-492c-9070-9e92f0c4e74d) {'id': '9042c6c4-f1f3-492c-9070-9e92f0c4e74d', 'created_at': datetime.datetime(2023, 8, 12, 16, 41, 53, 177397), 'updated_at': datetime.datetime(2023, 8, 12, 16, 41, 53, 181090)}", "[Place] (b37d688e-33f0-4b1a-a6c4-e38bc7425aa3) {'id': 'b37d688e-33f0-4b1a-a6c4-e38bc7425aa3', 'created_at': datetime.datetime(2023, 8, 12, 16, 42, 30, 468727), 'updated_at': datetime.datetime(2023, 8, 12, 16, 42, 30, 471022)}"]
(hbnb) all User
["[User] (6f5fe2b4-5d91-4172-b184-d825dc623cac) {'id': '6f5fe2b4-5d91-4172-b184-d825dc623cac', 'created_at': datetime.datetime(2023, 8, 12, 16, 14, 10, 749688), 'updated_at': datetime.datetime(2023, 8, 12, 16, 14, 10, 749718)}", "[User] (9042c6c4-f1f3-492c-9070-9e92f0c4e74d) {'id': '9042c6c4-f1f3-492c-9070-9e92f0c4e74d', 'created_at': datetime.datetime(2023, 8, 12, 16, 41, 53, 177397), 'updated_at': datetime.datetime(2023, 8, 12, 16, 41, 53, 181090)}"]
(hbnb) count User
2
(hbnb) update Place b37d688e-33f0-4b1a-a6c4-e38bc7425aa3 name "Morocco"
(hbnb) show Place b37d688e-33f0-4b1a-a6c4-e38bc7425aa3
[Place] (b37d688e-33f0-4b1a-a6c4-e38bc7425aa3) {'id': 'b37d688e-33f0-4b1a-a6c4-e38bc7425aa3', 'created_at': datetime.datetime(2023, 8, 12, 16, 42, 30, 468727), 'updated_at': datetime.datetime(2023, 8, 12, 16, 43, 29, 829700), 'name': 'Morocco'}
(hbnb) destroy Place b37d688e-33f0-4b1a-a6c4-e38bc7425aa3
(hbnb) all
["[User] (6f5fe2b4-5d91-4172-b184-d825dc623cac) {'id': '6f5fe2b4-5d91-4172-b184-d825dc623cac', 'created_at': datetime.datetime(2023, 8, 12, 16, 14, 10, 749688), 'updated_at': datetime.datetime(2023, 8, 12, 16, 14, 10, 749718)}", "[User] (9042c6c4-f1f3-492c-9070-9e92f0c4e74d) {'id': '9042c6c4-f1f3-492c-9070-9e92f0c4e74d', 'created_at': datetime.datetime(2023, 8, 12, 16, 41, 53, 177397), 'updated_at': datetime.datetime(2023, 8, 12, 16, 41, 53, 181090)}"]
(hbnb) quit
```

##### Exiting the console:

There are three ways in which you can terminate the *console*:

  - Using the `quit` command:

        (hbnb) quit

  - Sending an *EOF* signal using `Ctrl+d`

        (hbnb) ^D

  - Interrupting using `Ctrl+c` **(not recommended)**

        (hbnb) ^C

### Authors:

[**Amine Tahiri Alaoui**](https://github.com/Blxee) _email: hexninja10@gmail.com_  
[**Nora Ben Haddou**](https://github.com/Nawaritta) _email: Nor.Benhaddou@gmail.com_
