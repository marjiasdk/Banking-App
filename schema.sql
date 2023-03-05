-- This creates the database
CREATE DATABASE banking;

-- This goes into the database so you can use it
USE banking;

-- Creates a table named "users", this is where all the data is stored which is used in the program
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  card_number VARCHAR(16),
  password VARCHAR(255),
  balance DECIMAL(10, 2)
);

-- You can add more data with the following code
-- (x, y, z) are the different parameters
INSERT INTO users (name, card_number, password, balance) VALUES
('John Smith', '1234567890123', 'password123', 1000.00),
('Jane Doe', '2345678901234', 'password456', 500.00),
('Bob Johnson', '3456789012345', 'password789', 250.00),
('Sarah Lee', '4567890123456', 'passwordabc', 100.00),
('David Kim', '5678 901234567', 'passworddef', 50.00);