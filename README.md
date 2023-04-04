# Time tracking system
- **Author**: Volodymyr Rizun     
- **Group**: KI-02    

## About
Система Time-Tracking. Администратор закрепляет за пользователем      
Активность. У пользователя может быть одна или несколько Активностей.       
Пользователь отмечает кол-во затраченного времени на каждую активность.       
Пользователь может отправить запрос на добавление/удаление Активности.       

## Tech stack
| Tool      | Solution                           |
|-----------|------------------------------------|
| DBMS      | MySQL                              |
| Server    | Waitress (pure Python WSGI server) |
| Packaging | setuptools                         |
| Patterns  | DAO, Command, MVC (MTV in Python)  |    

## How to install & run
1. git clone https://github.com/konovaliuk/time_tracking.git 
2. cd time_tracking  
3. pip install venv  
4. python -m venv venv  
5. venv/Scripts/activate  
6. pip install -r requirements.txt  
7. waitress-serve --listen=*:8000 time_tracking:app   
8. Open http://127.0.0.1:8000/