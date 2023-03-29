DROP DATABASE time_tracking_db;

CREATE DATABASE IF NOT EXISTS time_tracking_db;

USE time_tracking_db;

CREATE TABLE IF NOT EXISTS role(
    role_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name_role VARCHAR(25) NOT NULL,
    UNIQUE(name_role)
);

CREATE TABLE IF NOT EXISTS user(
    user_id BIGINT PRIMARY KEY AUTO_INCREMENT ,
    login VARCHAR(50) NOT NULL, 
    password VARCHAR(120) NOT NULL, 
    email VARCHAR(255) NOT NULL,
    role_id BIGINT,
    FOREIGN KEY (role_id) REFERENCES role(role_id) ON DELETE SET NULL, 
    CONSTRAINT UC_User UNIQUE (login, email)
);

CREATE TABLE IF NOT EXISTS category(
    category_id BIGINT PRIMARY KEY AUTO_INCREMENT ,
    name_category VARCHAR(40) NOT NULL, 
    UNIQUE (name_category)
);

CREATE TABLE IF NOT EXISTS activity(
    activity_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name_activity VARCHAR(100) NOT NULL,
    category_id BIGINT,
    FOREIGN KEY (category_id) REFERENCES category(category_id) ON DELETE RESTRICT, 
    UNIQUE (name_activity)
);

CREATE TABLE IF NOT EXISTS action(
    action_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name_action VARCHAR(55) NOT NULL,
    UNIQUE (name_action)
);

CREATE TABLE IF NOT EXISTS time_tracking(
    activity_id BIGINT,
    user_id BIGINT,
    action_id BIGINT,
    time_spent TIME,
    FOREIGN KEY (activity_id) REFERENCES activity(activity_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (action_id) REFERENCES action(action_id) ON DELETE CASCADE,
    PRIMARY KEY (activity_id, user_id, action_id)
);