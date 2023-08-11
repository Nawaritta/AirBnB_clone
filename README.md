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

##### Exiting the console:

There are three ways in which you can terminate the *console*:

  - Using the `quit` command:

        (hbnb) quit

  - Sending an *EOF* signal using `Ctrl+d`

        (hbnb) ^D

  - Interrupting using `Ctrl+c` **(not recommended)**

        (hbnb) ^C

### Authors:

[Amine Tahiri Alaoui](hexninja10@gmail.com)
[Nora Ben Haddou](Nor.Benhaddou@gmail.com)
