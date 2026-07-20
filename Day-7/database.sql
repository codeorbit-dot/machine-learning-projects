CREATE DATABASE ai_training;

USE ai_training;

CREATE TABLE students(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    course VARCHAR(100),
    marks INT
);