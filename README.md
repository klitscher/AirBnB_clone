# Description :building_construction:

HolbertonBnB is a currently the backend console of a  much larger project involving creating a version of AirBnB



## Classes :mortar_board:

HolbertonBnB uses the following classes:

|                                | BaseModel                            | FileStorage                          | User                                                 | State                     | City                      | Amenity                   | Place                                                                                                                                                                      | Review                            |
| ------------------------------ | ------------------------------------ | ------------------------------------ | ---------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` |                                      | Inherits from `BaseModel`                            | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel`                                                                                                                                                  | Inherits from `BaseModel`         |
| **PUBLIC INSTANCE METHODS**    | `save`<br>`to_dict`                  | `all`<br>`new`<br>`save`<br>`reload` | ...                                                  | ...                       | ...                       | ...                       | ...                                                                                                                                                                        | ...                               |
| **PUBLIC CLASS ATTRIBUTES**    |                                      |                                      | `email`<br>`password`<br>`first_name`<br>`last_name` | `name`                    | `state_id`<br>`name`      | `name`                    | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` |
| **PRIVATE CLASS ATTRIBUTES**   |                                      | `file_path`<br>`objects`             |                                                      |                           |                           |                           |                                                                                                                                                                            |                                   |

# Console :desktop_computer:

The console is a command line interpreter written in python. The console munipulates all classes used by this application.

### Using the console

This console can be run in both interactive and non-interactive mode. 

```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```

To use the HolbertonBnB console in interactive mode, run the 
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt:

```
$ ./console.py
(hbnb) 
```

To quit the console, enter the command `quit`, or input an EOF signal 
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```



# Console Commands

There are a few commands that can be combined with other information or Model names to interact with the files.



##### Create:

* Usage: `create <class>`

```bash
(hbnb) create BaseModel
f8e10029-278f-4fe7-b27b-af792787f35e //this is the ID number
```

Creates a new instance and ID base off of given class name

##### Show:

* Usage: `show <class> <id>` or `<class>.show(<id>)`

```bash
(hbnb) show BaseModel f8e10029-278f-4fe7-b27b-af792787f35e
[BaseModel] (f8e10029-278f-4fe7-b27b-af792787f35e) {'id': 'f8e10029-278f-4fe7-b27b-af792787f35e', 'created_at': '2019-07-03T13:25:15.322350', 'updated_at': '2019-07-03T13:25:15.322421'}
```

Prints the string representation of a class instance based on a given id.

##### Destroy:

* Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

```
(hbnb) destroy BaseModel f8e10029-278f-4fe7-b27b-af792787f35e
```

Deletes a class instance based on a given id. The storage file `instance.json` 
is updated as well.

##### All:

* Usage: `all` or `all <class>` or `<class>.all()`

```bash
(hbnb) all BaseModel
[<models.base_model.BaseModel object at 0x7f5671a9b400>]
(hbnb) all
[<models.user.User object at 0x7f56711d6320>, <models.user.User object at 0x7f56711c4f98>, <models.user.User object at 0x7f56711c4ef0>, <models.base_model.BaseModel object at 0x7f56711c4e48>, <models.user.User object at 0x7f56711c4d68>, <models.user.User object at 0x7f56711c4d30>, <models.user.User object at 0x7f56711c4cc0>, <models.user.User object at 0x7f56711c4c18>, <models.user.User object at 0x7f56711d63c8>, <models.user.User object at 0x7f56711c4f60>, <models.city.City object at 0x7f56711d6240>, <models.state.State object at 0x7f56711d6208>, <models.city.City object at 0x7f56711d61d0>, <models.state.State object at 0x7f56711d6198>, <models.city.City object at 0x7f56711d6160>, <models.place.Place object at 0x7f56711d6128>, <models.user.User object at 0x7f56711d6048>, <models.user.User object at 0x7f56711d6080>]

```

* Prints the string representations of all instances of a given class.

##### Count:

* Usage: `count <class>` or `<class>.count()`

```bash
(hbnb) count BaseModel
168
```

Counts the number of instances of the names class.

##### Update:

* Usage: `update <class> <id> <attribute name> "<attribute value>"` or
  
  `<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(<id>, <attribute dictionary>)`.

```bash
(hbnb) create User
f1c8029f-022d-4948-b085-42474dea7b2a
(hbnb) show User 2ba873fe-42f5-453c-a530-7d483cfc622b
[User] (2ba873fe-42f5-453c-a530-7d483cfc622b) {'id': '2ba873fe-42f5-453c-a530-7d483cfc622b', 'created_at': '2019-07-03T14:05:52.106552', 'updated_at': '2019-07-03T14:05:52.106624'}
(hbnb) update User 2ba873fe-42f5-453c-a530-7d483cfc622b pants onfire
(hbnb) show User 2ba873fe-42f5-453c-a530-7d483cfc622b
[User] (2ba873fe-42f5-453c-a530-7d483cfc622b) {'id': '2ba873fe-42f5-453c-a530-7d483cfc622b', 'created_at': '2019-07-03T14:05:52.106552', 'updated_at': '2019-07-03T14:07:33.600967', 'pants': 'onfire'}

```

Updates and adds an attribute to the dictionary of a instance of a class.



## Testing :wrench:

Unittests for the HolbertonBnB project are defined in the [tests](./tests) 
folder.










