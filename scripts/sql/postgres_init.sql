CREATE ROLE airflow WITH LOGIN SUPERUSER PASSWORD 'airflow';
CREATE DATABASE airflow
    WITH 
    OWNER = airflow
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE ROLE data_lake WITH LOGIN SUPERUSER PASSWORD 'data_lake';
CREATE DATABASE data_lake
    WITH 
    OWNER = data_lake
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE ROLE staging WITH LOGIN SUPERUSER PASSWORD 'staging';
CREATE DATABASE staging
    WITH 
    OWNER = staging
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
    
CREATE ROLE warehouse WITH LOGIN SUPERUSER PASSWORD 'warehouse';
CREATE DATABASE warehouse
    WITH 
    OWNER = warehouse
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
     
CREATE ROLE redash WITH LOGIN SUPERUSER PASSWORD 'redash';
CREATE DATABASE redash
    WITH 
    OWNER = redash
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE EXTENSION IF NOT EXISTS dblink WITH SCHEMA public;