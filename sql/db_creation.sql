use techshop;

CREATE TABLE employee (
  userId varchar(20),
  firstName VARCHAR(20) NOT NULL,
  lastName VARCHAR(20) NOT NULL,
  email VARCHAR(45) NOT NULL,
  phoneNumber INT,
  jobTitle VARCHAR(20),
  PRIMARY KEY (userId)
);

CREATE TABLE customer (
  userId varchar(20),
  firstName VARCHAR(20) NOT NULL,
  lastName VARCHAR(20) NOT NULL,
  email VARCHAR(45) NOT NULL,
  phoneNumber INT,
  addressOne VARCHAR(20) NOT NULL,
  addressTwo VARCHAR(20) NOT NULL,
  city VARCHAR(20) NOT NULL,
  state CHAR(2) NOT NULL,
  zipCode INT NOT NULL,
  PRIMARY KEY (userId)
);

CREATE TABLE product (id INT AUTO_INCREMENT,
  productName VARCHAR(250) NOT NULL,
  price DECIMAL(13,2) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE purchase (
  product_id INT,
  customer_id VARCHAR(20),
  purchaseDate DATE NOT NULL,
  purchaseTime TIME NOT NULL,
  totalCost DECIMAL(13, 2) NOT NULL,
  PRIMARY KEY (product_id, customer_id),
  FOREIGN KEY (product_id) REFERENCES product(id),
  FOREIGN KEY (customer_id) REFERENCES customer(userId)
);
