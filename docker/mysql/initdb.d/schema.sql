CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_active BIT(1) NOT NULL DEFAULT b'0',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_DATE,
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
    user INT NOT NULL,
    book INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (id),
    FOREIGN KEY (user) REFERENCES users(id),
    FOREIGN KEY (book) REFERENCES books(id)
);

CREATE TABLE tokens (
    user INT NOT NULL,
    access_token VARCHAR(255) NOT NULL,
    token_expires TIMESTAMP NOT NULL,
    FOREIGN KEY (user) REFERENCES users(id)
);