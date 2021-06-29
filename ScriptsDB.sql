/**
  Crear con anterioridad la base de datos con el comando CREATE DATABASE neu_test
  SCRIPT DE CREACIÓN DE LA TABLA
 */

CREATE TABLE location (
   id serial PRIMARY KEY,
   id_country integer unique ,
   id_state integer unique ,
   id_city integer unique ,
   name char(255),
   population integer,
   country_id integer,
   state_id integer,
   FOREIGN KEY (country_id) REFERENCES location (id_country),
   FOREIGN KEY (state_id) REFERENCES location (id_state)
);


/**
  SCRIPT PARA AGREGAR LOS DATOS DE UN ARCHIVO .CSV, VERIFICAR LA RUTA DEL ARCHIVO, SEGÚN LA UBICACIÓN
  Se adjuntan los archivos, pues se hae modificación de extensión además de encoder
 */

COPY location(id_country, name)
FROM 'D:\Apps\Test\countries.csv'
DELIMITER ';'
CSV HEADER;


/**
  SCRIPT PARA AGREGAR LOS DATOS DE UN ARCHIVO .CSV, VERIFICAR LA RUTA DEL ARCHIVO, SEGÚN LA UBICACIÓN
 */

COPY location(id_state, name, country_id)
FROM 'D:\Apps\Test\states.csv'
DELIMITER ';'
CSV HEADER;

/**
  SCRIPT PARA AGREGAR LOS DATOS DE UN ARCHIVO .CSV, VERIFICAR LA RUTA DEL ARCHIVO, SEGÚN LA UBICACIÓN
 */

COPY location(id_city, name, state_id, population)
FROM 'D:\Apps\Test\cities.csv'
DELIMITER ';'
CSV HEADER;
