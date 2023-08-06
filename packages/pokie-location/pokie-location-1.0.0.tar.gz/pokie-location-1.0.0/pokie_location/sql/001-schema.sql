-- iso3166 country list
CREATE TABLE country
(
    id_country CHAR(2) PRIMARY KEY,
    name       VARCHAR(255) NOT NULL
);


CREATE TABLE timezone
(
    id_timezone  VARCHAR PRIMARY KEY,
    fk_country   CHAR(2) REFERENCES country
);

