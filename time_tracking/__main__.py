from .tools import DB_Factory, Connection_Factory, DAO_Factory, encrypt
from .models import Category, Activity, User
from .properties import DBMS


def run():
    db = DB_Factory.get_db(DBMS)
    db.connect()

    with Connection_Factory.get_cnx(DBMS, db) as cnx:
        # user table

        dao_user = DAO_Factory.get_dao(DBMS).get_dao_implementation('user')
        users = dao_user.select_all(cnx)
        print('\nSelect all', *users, '\n', sep='\n')

        usr1 = dao_user.find_by_login(cnx, 'super_admin')
        print('Find by Id\n', usr1, '\n\n')

        usr1 = User(login='new_user_3', password=encrypt('3333', 'new_user_3'), email='new_user3@gmail.com', role_id=2)
        usr2 = User(login='new_user_4', password=encrypt('444444', 'new_user_4'), email='new_user4@gmail.com', role_id=2)
        dao_user.insert(cnx, [usr1, usr2])

        usr2 = dao_user.find_by_login(cnx, usr2.login)
        usr2.login = 'UPDATED_login'
        dao_user.update(cnx, [usr2])

        dao_user.delete(cnx, [usr1])

        users = dao_user.select_all(cnx)
        print('Select all', *users, '\n', sep='\n')

        # time_tracking table
        dao_activity = DAO_Factory.get_dao(DBMS).get_dao_implementation('activity')
        dao_time_track = DAO_Factory.get_dao(DBMS).get_dao_implementation('time_tracking')

        activity = dao_activity.find_by_name(cnx, 'chess')
        print(activity)
        time_trackings = dao_time_track.find_by_activity_id(cnx, activity.activity_id)

        time_by_users = [(t.user.login, str(t.time_spent)) for t in time_trackings]
        print('Time spent by all users on chess:', *time_by_users, sep='\n')

    db.close()

if __name__ == '__main__':
    run()