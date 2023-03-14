import sys

from lab1.entity.user import User
from lab1.utills import encode
from lab1.factory import DB_Factory, Connection_Factory, DAO_Factory

dbms = sys.argv[1]

def run():
    db = DB_Factory.get_db(dbms)
    db.connect()

    cnx1 = Connection_Factory.get_cnx(dbms, db)

    # USER TABLE
    dao_user = DAO_Factory.get_dao(dbms).get_dao_implementation(cnx1, 'user')

    # select all
    users = dao_user.select_all()
    print('\nSelect all', *users, '\n', sep='\n')

    # find by id
    usr1 = dao_user.find_by_login('super_admin')
    print('Find by Id\n', usr1, '\n\n')

    # insert
    usr1 = User(4, 'new_user_3', encode('3333'), 'new_user3@gmail.com', 2)
    usr2 = User(5, 'new_user_4', encode('444444'), 'new_user4@gmail.com', 2)
    dao_user.insert([usr1, usr2])

    # update
    usr2 = dao_user.find_by_login(usr2.login)
    usr2.login = 'UPDATED_login' 
    dao_user.update([usr2])

    # delete
    dao_user.delete([usr1])

    # see the difference
    users = dao_user.select_all()
    print('Select all', *users, '\n', sep='\n')

    # TIME_TRACKING TABLE
    dao_activity = DAO_Factory.get_dao(dbms).get_dao_implementation(cnx1, 'activity')
    dao_time_track = DAO_Factory.get_dao(dbms).get_dao_implementation(cnx1, 'time_tracking')

    # show all users of particular activity
    activity = dao_activity.find_by_name('chess')
    time_trackings = dao_time_track.find_by_activity_id(activity.activity_id)
    users_id = [i.user_id for i in time_trackings]
    time_spent = [f'{i.time_spent.seconds // 3600}:{(i.time_spent.seconds // 60) % 60}:{i.time_spent.seconds % 60}' for i in time_trackings]
    print('Time spent by all users on chess:', *zip(users_id, time_spent), sep='\n')

    db.close()

if __name__ == '__main__':
    run()