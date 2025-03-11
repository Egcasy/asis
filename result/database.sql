CREATE DATABASE student_results;

USE student_results;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20) NOT NULL,
    term VARCHAR(50) NOT NULL,
    result_pdf VARCHAR(255) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Insert default teacher login (password = "admin123")
INSERT INTO teachers (username, password) VALUES ('admin', SHA2('admin123', 256));
