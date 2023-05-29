CREATE DATABASE empresa;
CREATE TABLE area(id SERIAL NOT NULL PRIMARY KEY,
				 nombre TEXT NOT NULL,
				 piso NUMERIC NOT NULL );

INSERT INTO areas (id, nombre, piso) VALUES
(DEFAULT,'Marketing',2),
(DEFAULT,'Sistemas',3),
(DEFAULT,'Contabilidad',1);

CREATE TABLE empleados(id SERIAL NOT NULL PRIMARY KEY,
					   nombre TEXT NOT NULL,
					   apellido TEXT NOT NULL,
					   email TEXT NOT NULL UNIQUE,
					   area_id NUMERIC 
					  );