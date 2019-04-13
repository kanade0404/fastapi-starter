CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE books (
    id INT NOT NULL AUTO_INCREMENT,
    isbn VARCHAR(13) NOT NULL,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    publisher VARCHAR(100) NOT NULL,
    cover VARCHAR(255) NOT NULL,
    publish_date INT,
    PRIMARY KEY (id)
);

CREATE TABLE comments (
    id INT NOT NULL AUTO_INCREMENT,
    content TEXT NOT NULL,

);