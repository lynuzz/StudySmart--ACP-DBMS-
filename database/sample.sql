
CREATE DATABASE studysmart;

CREATE TABLE user (
  id INT NOT NULL AUTO_INCREMENT,
  username varchar(50) NOT NULL,
  password varchar(200) NOT NULL,
  role varchar(10) NOT NULL DEFAULT 'user',
  email varchar(150) DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE task (
  id INT NOT NULL AUTO_INCREMENT,
  title varchar(200) NOT NULL,
  subject varchar(100) NOT NULL,
  deadline datetime NOT NULL,
  status ENUM('Pending', 'Completed') DEFAULT 'Pending',
  user_id INT NOT NULL,
  PRIMARY KEY (id),
  KEY user_id (user_id),
  FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE
);

ALTER TABLE user AUTO_INCREMENT = 1; 
ALTER TABLE task AUTO_INCREMENT = 1; 

INSERT INTO user (id, username, password, role, email) 
VALUES 
(1, 'Lynus Kenzley', '12345', 'user', '24-36497@g.batstate-u.edu.ph'), 
(2, 'Kenz', '54321', 'user', 'lynuskenzleydaang@gmail.com');


INSERT INTO task (id, title, subject, deadline, status, user_id) 
VALUES 
(3, 'Documentation', 'DBMS', '2025-12-15 12:00:00', 'Pending', 1),
(4, 'Sytem Web', 'ACP', '2025-12-15 12:00:00', 'Completed', 1), 
(5, 'Final Examination', 'ACP&DBMS', '2025-12-16 17:00:00', 'Pending', 2);

SELECT * FROM user;

UPDATE task
SET subject = 'DBMS & OOP'
WHERE title = 'Documentation';

DELETE FROM task
WHERE title = 'Final Examination';

SELECT 
    t.title AS task_title, 
    u.username AS owner_name
FROM 
    task t
JOIN 
    user u ON t.user_id = u.id;

SELECT 
    status, 
    COUNT(*) AS total_tasks
FROM 
    task
GROUP BY 
    status;

SELECT 
    username
FROM 
    user
WHERE 
    id NOT IN (SELECT user_id FROM task);
