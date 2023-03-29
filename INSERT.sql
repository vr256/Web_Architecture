USE time_tracking_db;

INSERT INTO role (name_role)
VALUES ('user'),
	   ('admin');

INSERT INTO user (login, password, email, role_id)
VALUES ('super_admin', '$6$super0admin$YH56BG7Sx9aUr9p5vDdS9APKhpdG4IqvXv6oIjZNOhQkFe3yYEc1CBis.SRXgSXiAxO8GjU6BHFLo7mwtUpce0', 'admin@gmail.com', 2),
	   ('first_user', '$6$first0user$/WuckNXaAHXDPY.Jx/lOEl9wgWnBQ3alk5I8w7Jgg4OAVIvWGAFE5ynGpo2gHfgcAeXZ/Vg9Xxql3B5ZXzvC6/', 'user1@gmail.com', 1), 
	   ('second_user', '$6$second0user$6J0Y.BuAc53plIr3vyYdp2k/XC/P1ZShpAvTFRqVQhiGwOIe1138qLspLD5EkTV8RnbGLMvv3.UEyuq8nWqRy0', 'user2@gmail.com', 1);

INSERT INTO category (name_category)
VALUES ('learning'),
	   ('sport'),
	   ('board games');

INSERT INTO activity (name_activity, category_id)
VALUES ('SQL', 1),
       ('calculus', 1),
       ('probability theory', 1),
	   ('football', 2),
	   ('chess', 3),
 	   ('go', 3);

INSERT INTO action (name_action)
VALUES ('do nothing'),
         ('assign'),
         ('remove');

INSERT INTO time_tracking (activity_id, user_id, action_id, time_spent)
VALUES (1, 2, 1, '1:15:00'),
       (6, 2, 1, '0:35:00'),
       (4, 2, 1, '1:47:50'),
       (3, 2, 3, '0:25:00'),
       (2, 3, 1, '2:12:00'),
       (5, 3, 1, '3:30:00'),
       (6, 3, 1, '0:05:25'),
       (3, 1, 1, '0:55:00'),
       (5, 1, 1, '1:27:00'),
       (1, 3, 2, '0:00:00');


# Select preset
SELECT login, name_role, name_activity, name_category, time_spent, name_action
FROM time_tracking 
INNER JOIN user USING(user_id)
INNER JOIN activity USING(activity_id)
INNER JOIN category USING(category_id)
INNER JOIN role USING(role_id)
INNER JOIN action USING(action_id);