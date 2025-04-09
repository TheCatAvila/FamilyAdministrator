CREATE TABLE IF NOT EXISTS family (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    created_at DATETIME NOT NULL
    );

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(256) NOT NULL,
    register_date DATETIME NOT NULL,
    family_selected_id INT,
    FOREIGN KEY (family_selected_id) REFERENCES family(id)
);

CREATE TABLE IF NOT EXISTS family_role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS user_family (
    user_id INT NOT NULL,
    family_id INT NOT NULL,
    role_id INT NOT NULL,
    PRIMARY KEY (user_id, family_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (family_id) REFERENCES family(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES family_role(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS expense_category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    family_id INT NOT NULL,
    FOREIGN KEY (family_id) REFERENCES family(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS expense_subcategory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    budget DECIMAL(13, 2) NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES expense_category(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10,2) NOT NULL,
    description VARCHAR(255),
    category_id INT NOT NULL,
    subcategory_id INT,
    family_id INT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES expense_category(id) ON DELETE CASCADE,
    FOREIGN KEY (subcategory_id) REFERENCES expense_subcategory(id) ON DELETE SET NULL,
    FOREIGN KEY (family_id) REFERENCES family(id) ON DELETE CASCADE
);