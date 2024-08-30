CREATE TABLE
	paises(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

SELECT id, descripcion 
FROM paises;