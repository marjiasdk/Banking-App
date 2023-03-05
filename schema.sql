-- This creates the database
CREATE DATABASE banking;

-- This goes into the database so you can use it
USE banking;

-- Creates a table named "userS", this is where all the data is stored which is used in the program
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  card_number VARCHAR(16),
  password VARCHAR(255),
  balance DECIMAL(10, 2)
);

-- You can add more data with the following code
-- (x, y, z) are the different parameters
INSERT INTO users (card_number, password, balance) VALUES 
  ('1234567890123456', 'password123', 1000.00),
  ('2345678901234567', 'letmein', 5000.00);
