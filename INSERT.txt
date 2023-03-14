USE time_tracking_db;

INSERT INTO role (name_role)
VALUES ('user'),
	   ('admin');

INSERT INTO user (login, password, email, role_id)
VALUES ('super_admin', '$2b$12$XK3mWVuexo3okE8j5FYWU.pS2QEepg6xoRt6mkIxUOC8ZO9es6dsG', 'admin@gmail.com', 2),
	   ('first_user', '$2b$12$YSJnEewd4UmfcZ/qcXDPzOX/M.L2MRQoJd56kn4Fmxe2aJrEdv0.q', 'user1@gmail.com', 1), 
	   ('second_user', '$2b$12$4cDj2mBFhCW/1OEPCDdvyebmmGY6Ua1SsvTJYiwuWO7TTEgcBxT7a', 'user2@gmail.com', 1);

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