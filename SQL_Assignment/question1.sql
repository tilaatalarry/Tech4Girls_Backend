CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;

USE Tech4Girls_DB;

CREATE TABLE IF NOT EXISTS Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Users (username, email, created_at) 
VALUES
    ('ama', 'ama@example.com', '2024-11-01 10:30:00'),
    ('Abena', 'abena@example.com', '2024-11-02 12:00:00'),
    ('adjoa', 'adjoa@example.com', '2024-11-03 14:15:00');
