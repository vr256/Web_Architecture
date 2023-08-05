# Time tracking system
 

## Tech stack
| Tool      | Solution                           |
|-----------|------------------------------------|
| DBMS      | MySQL                              |
| Server    | Django Development Server          |
| ORM       | Django ORM                         |
| Patterns  | DAO, Command, MTV                  |    

## How to install & run
1. `git clone https://github.com/vr256/software_architecture.git`
2. `cd software_architecture` 
3. `git checkout remotes/origin/django`
4. `pip install venv`  
5. `python -m venv venv`  
6. `venv/Scripts/activate`  
7. `pip install -r requirements.txt`  
8. `python time_tracking/manage.py runserver`