# Mybookreview
> **Mybookreview** is an application made for 1influencers.com to show my skills with python, flask and panda not to mention i still have a lot to learn in python. My courses at school were mainly focused up till know has been c# so this was a great experience and a small challange but.
> 
# 2. Intro
I am proud to present my first fullstack application made in python, flask and pandas.\
As css framework i choose for bootstrap because i wased to working with it. 
I used the mvc tree structure to enhance infrastructure and soc.


# 3. About the application
This crud application is made so you can easy write a book review, you can share this with all other users that have signed in.\
When you write a review you get assitance from the google api by giving you your search history of books on the application.

# 4. Installation

This app requires Python 3+ to run, so install that first


1. install a virutal enviroment or update and creating one

 
```python
py -m pip install --upgrade pip
py -m pip install --user virtualenv
py -m venv env

```


**1. Run a virtual enviroment to setup dependencies activate the enviroment using scripts in project file** 
```cd to env folder
.\env\Scripts\activate
```

**2. Install the dependencies:**

```python
pip install -r requirements.txt 
```

**3. Run:**

```python
python manage.py
```

## 4.1. Backend Test
## 4.2. Theoretical Test
1. How does one combine two Pandas dataframes?
   > Pandas have a build in functions to handle with this you can combine 2 dataframes by concatenating using the **concat** function. 
   With this function you have a parameter where you can decide instead of concatenating the 2 dataframes to join them using Inner en Outer Join.
   The concat function appends the first frame with the second one, but you can also use the append function to do the same! 
   This is what I used during this project. 
2. What is the difference between a local variable and a global variable?
   > - A local variable can only be accessible in their local variables or environment, meaning you can access a local variable defined or initialized in a function but not outside this scope.
   > - A global variable can be as the name implies use it everywhere in the file outside and inside a scope
3. How does one create a copy of a dataframe using Pandas?
   >You can do this using the build in dataframe function:\
      **DataFrame.copy(deep=True)**
   >- When deep=True (default), a new object will be created with a copy of the calling object’s data and indices. Modifications to the data or indices of the copy will not be reflected in the >original object (see notes below).
   >- When deep=False, a new object will be created without copying the calling object’s data or index (only references to the data and index are copied). Any changes to the data of the original will be reflected in the shallow copy (and vice versa).
   >
   > *Parameters: 
   > deepbool, default True
   > Make a deep copy, including a copy of the data and the indices. With deep=False neither the indices nor the data are copied.*\
   > **Returns copySeries or DataFrame Object type matches caller.**
   
1. How does one handle concurrent requests in Flask?
   > Solving this problem is a quite easy work to do, you only need put threaded=True in your script so it will handle each requests in different thread.
   >
   > ```
   > app.run(host = HOST, port = PORT, threaded = True)
   > ```
   >

   
2. What is a Replica Set in MongoDB?
   >A replica set in MongoDB is a group of mongod processes that maintain the same data set. Replica sets provide redundancy and high availability, and are the basis for all production deployments
   ![Schematic view of replica set ](https://www.mongodb.com/docs/manual/images/replica-set-read-write-operations-primary.bakedsvg.svg "Schematic view of replica set").
3. What is a Transaction in a database context?
   > A logical unit that is independently executed for data retrieval or updates, this is very plain explained, but it should consist of respecting these principles being:
   > 1. Atomicity
   > 2. Consistency
   > 3. Isolation
   > 4. Durability\
   >**If a database consists and applies these principles we can talk about transactional data**.

   
## 4.3. Practical Test
Create an application using Python, Flask and SQL to register and authenticate an user.
The user must have an unique email address and the password must have at least 8
characters.
The application must consult an external API, such as PokeAPI(https://pokeapi.co/), use
Pandas to process the data and save it in a MongoDB database. The CRUD endpoints
for this part of the application must be accessible only to a previously authenticated user
existing in the SQL database. All endpoints must return a JSON response with status,
data, message and HTTP code.
The project must be added to a public repository on Github and shared with the person
responsible for the selection. The README.md file must contain the answers for the
theoretical test, as well as the instructions necessary to execute the project.
The code must be well documented and follow good development practices

# 5. Notes and remarks
## 5.1. Features for the future!
- [ ] Preview of review using dataframe not only writen review, make a mix of both worlds! (Mixing maybe JS with python?)
- [ ] Like functionality fix bugs!
- [ ] Fix delete bug fixes!
- [ ] Add relationship between books and reviews so each review can be traced in database
- [ ] Add delete functionality for books and to improve useer experience search hisory
- [ ] Update current system that you can make a list that you have read (maybe in combination with current system based on early searches!)

## 5.2. *Some minor bugs*
 - *Like feature is not working properly but stores the like in database, will get updated on future releases.*
 - *Redirect keeps showing reponse page on redirect and i just want to pass the reponse with it.*
 - *Delete won't appear because passed id changed and object changed so atributes probably changed and can't reconise id.* 


