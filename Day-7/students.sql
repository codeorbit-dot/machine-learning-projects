-- Create Database
CREATE DATABASE IF NOT EXISTS ai_training;

USE ai_training;

-- Create Table
CREATE TABLE IF NOT EXISTS students(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    course VARCHAR(100),
    marks INT
);

-- Insert Data
INSERT INTO students(name, course, marks)
VALUES
('Tarun','Python',90),
('Rahul','SQL',85),
('Ravi','AI',95);

-- Display Data
SELECT * FROM students;