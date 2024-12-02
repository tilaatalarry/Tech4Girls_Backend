-- use the database
USE Tech4Girls_DB;

-- Create the Posts table
CREATE TABLE Posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Insert sample data into the Posts table
INSERT INTO Posts (user_id, title, content, created_at) VALUES
(1, 'Ama’s first post', 'This is Ama’s first post content.', '2024-11-01 11:00:00'),
(2, 'Abena’s first post', 'This is Abena’s first post content.', '2024-11-02 13:00:00'),
(3, 'Adjoa’s first post', 'This is Adjoa’s first post content.', '2024-11-03 15:00:00');