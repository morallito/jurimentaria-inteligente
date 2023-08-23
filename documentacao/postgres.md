# Banco de dados 


O banco de dados está instalado em uma maquina rodando ubuntu server. Para checar o estado do banco de dados 
basta rodar o comando:

```
sudo systemctl status postgresql
```
Apos rodar tal comando, voce vai ver um prompt que se parece com:

```
● postgresql.service - PostgreSQL RDBMS
     Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; vendor preset: enabled)
     Active: active (exited) since Mon 2023-08-14 11:16:19 UTC; 22min ago
   Main PID: 900 (code=exited, status=0/SUCCESS)
        CPU: 755us

Aug 14 11:16:19 iagohomeserver systemd[1]: Starting PostgreSQL RDBMS...
Aug 14 11:16:19 iagohomeserver systemd[1]: Finished PostgreSQL RDBMS.
```


## Conectando ao banco de dados 

```
# Change the user to postgress user
user@user-pc:~$ sudo -i -u postgres
# Connect to the postgress database
postgres@user-pc:~$ psql
```

## Criando um novo usuario no postgress para seu app

```
# Change the user to postgress user
user@user-pc:~$ sudo -i -u postgres
# Connect to the postgress database
postgres@user-pc:~$ psql
# Create a new user
postgres=# CREATE USER escavador WITH PASSWORD 'escavador';
# Create a new database
postgres=# CREATE DATABASE mydatabase;
# Grant all privileges on database
postgres=# GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
# Exit the database
postgres=# \q
# Exit the postgres user
postgres@user-pc:~$ exit
```


Após estes passos, você pode conectar ao banco de dados usando o comando:

```
psql -h localhost -U myuser -d mydatabase
```


## Change the linux user back to root user (morallito)

To exit the postgress user and return to the root user, use the command:

```
postgres@user-pc:~$ exit
user@user-pc:~$ 
```


## Criando a tabela para armazenar os dados

```sql
    jurisprudence_table = """
    CREATE TABLE IF NOT EXISTS jurisprudence (
      id VARCHAR(255) PRIMARY KEY,
      judgment_date DATE,
      reporter_judge VARCHAR(255),
      publication_date DATE,
      court VARCHAR(255),
      publication TEXT,
      parties TEXT,
      menu TEXT,
      decision TEXT,
      theme TEXT,
      thesis TEXT,
      indexing TEXT,
      legislation TEXT,
      observation TEXT,
      doctrine TEXT,
      full_body_url TEXT
    );
    """ 
```

## Postgress  commands

### Connect to the database in psql 
  
  ``` 
  \c database_name
  ```

### List all databases

  ``` 
  \l
  ```

### Get all tables in a database public schema

  ``` 
  \dt
  ```
### get a taable schema 

  ``` 
  \d+ table_name
  ```