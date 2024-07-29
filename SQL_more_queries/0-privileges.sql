-- Lists all privileges of the users user_0d_1 and user_0d_2


SELECT USER ();
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2';

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
