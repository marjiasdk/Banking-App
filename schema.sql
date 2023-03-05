CREATE DATABASE banking;

USE banking;

CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  card_number VARCHAR(16),
  password VARCHAR(255),
  balance DECIMAL(10, 2)
);

INSERT INTO users (card_number, password, balance)
VALUES 
  ('1234567890123456', 'password123', 1000.00),
  ('2345678901234567', 'letmein', 5000.00);
