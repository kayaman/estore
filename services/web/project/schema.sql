DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
  id         SERIAL,
  name       TEXT,
  email      TEXT,

  PRIMARY KEY (id)
);


DROP TABLE IF EXISTS categories CASCADE;
CREATE TABLE categories (
  id         SERIAL,
  name       TEXT,

  PRIMARY KEY (id)
);


DROP TABLE IF EXISTS products CASCADE;
CREATE TABLE products (
  id          SERIAL,
  name        TEXT,
  description TEXT,
  category_id INT,

  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id)
);


DROP TABLE IF EXISTS items CASCADE;
CREATE TABLE items (
  id         SERIAL,
  name       TEXT,
  price      FLOAT,
  product_id INT,

  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);


DROP TABLE IF EXISTS orders CASCADE;
CREATE TABLE orders (
  id         SERIAL,
  user_id    INT,

  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);



DROP TABLE IF EXISTS user_orders CASCADE;
CREATE TABLE user_orders (
  id         SERIAL,
  user_id    INT,
  order_id   INT,

  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (order_id) REFERENCES orders(id)
);

DROP TABLE IF EXISTS order_items CASCADE;
CREATE TABLE order_items (
  id         SERIAL,
  user_id    INT,
  item_id    INT,

  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (item_id) REFERENCES items(id)
);





INSERT INTO products (name, description, category_id) VALUES ('Product 1', 'fooobar 1', 1);
INSERT INTO products (name, description, category_id) VALUES ('Product 2', 'fooobar 2', 1);
