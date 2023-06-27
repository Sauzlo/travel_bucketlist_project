DROP TABLE cities;
DROP TABLE countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    rating INT CHECK (rating > 0 AND < 6),
    visited BOOLEAN
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);