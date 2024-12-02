-- use the database
USE Tech4Girls_DB;

-- Create the Courses table
CREATE TABLE Courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100)
);

-- Create the User_Courses table for the many-to-many relationship
CREATE TABLE User_Courses (
    user_id INT,
    course_id INT,
    PRIMARY KEY (user_id, course_id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

-- Insert sample data into the Courses table
INSERT INTO Courses (course_name) VALUES
('Database Design'),
('Web Development'),
('Machine Learning');

-- Insert sample data into the User_Courses table
INSERT INTO User_Courses (user_id, course_id) VALUES
(1, 1), -- Ama enrolled in Database Design
(1, 2), -- Ama enrolled in Web Development
(2, 2), -- Abena enrolled in Web Development
(2, 3), -- Abena enrolled in Machine Learning
(3, 1), -- Adjoa enrolled in Database Design
(3, 3); -- Adjoa enrolled in Machine Learning