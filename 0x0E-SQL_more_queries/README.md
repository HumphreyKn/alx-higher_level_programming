# MySQL CREATE USER
!MySQL Create User

**Summary**: you will learn how to use the MySQL `CREATE USER` statement to create a new user in the MySQL database server.
**Source**: https://www.mysqltutorial.org/mysql-administration/mysql-create-user/

Typically, MySQL creates the root user account during installation. This root user account has full privileges over the MySQL database server, giving it complete control over all databases, tables, users, and more.

It’s a good practice to use the root account for administrative functions exclusively. For other tasks, create a new user account and grant the necessary privileges.

This tutorial focuses on using the `CREATE USER` statement to create a new user in the MySQL database.

## Introduction to MySQL CREATE USER statement
-------------------------------------------

To create a new user in the MySQL database, you use the `CREATE USER` statement.

Here’s the basic syntax of the `CREATE USER` statement:

```SQL
CREATE USER [IF NOT EXISTS] account_name 
IDENTIFIED BY 'password';
```


*In this syntax*:

**First**, specify the account name after the `CREATE USER` keywords. The account name consists of two parts: `username` and `hostname`, separated by the `@` sign:

```SQL
username@hostname
```


The `username` is the name of the user while the `hostname` is the name of the host from which the user connects to the MySQL Server.

The `hostname` part of the account name is optional. If you omit the hostname, the user can connect from any host.

An account name without a hostname is equivalent to the following:

```SQL
username@%
```


If the `username` and `hostname` contains special characters, such as spaces or hyphens, you need to enclose the username and hostname separately in quotes, like this:

```SQL
'bob-cat'@'hostname'
```


In addition to the single quote (`'`), you can use backticks ( `` ` ``) or double quotation mark (`"`).

**Second**, specify the password for the user after the `IDENTIFIED BY` keywords.

The `IF NOT EXISTS` option creates a new user only if it does not already exist. If the user exists, the statement issues a warning.

Note that the `CREATE USER` statement creates a new user without any privileges. To grant privileges to the user, you use the `GRANT` statement.

### MySQL CREATE USER example
-----------------------------

**First**, establish a connection to the MySQL Server using the mysql client tool with the root user account:

```
mysql -u root -p
```


Enter the password for the `root` account and press `Enter`:

```
Enter password: ********
```


**Second**, show the users on the current MySQL Server:

```
SELECT
  user 
FROM 
  mysql.user;
```


Here is the output:

```
+------------------+
| user             |
+------------------+
| mysql.infoschema |
| mysql.saession   |
| mysql.sys        |
| root             |
+------------------+    
```


**Third**, create a new user named `bob`:

```
create user bob@localhost 
identified by 'Secure1pass!';
```


**Fourth**, show all users again:

```
select user from mysql.user;
```


The output will be:

```
+------------------+
| user             |
+------------------+
| bob              |
| mysql.infoschema |
| mysql.session    |
| mysql.sys        |
| root             |
+------------------+
5 rows in set (0.00 sec)Code language: JavaScript (javascript)
```


The output indicates that the user with the name `bob` has been created successfully.

**Fifth**, open a second session and log in to the MySQL database server with the user `bob`:

```
mysql -u bob -p
```


Input the password for `bob` and press `Enter`:

```
Enter password: ********
```


**Sixth**, show the databases that `bob` has access:

```
show databases;
```


Here is the list of databases that `bob` can access:

```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| performance_schema |
+--------------------+
2 rows in set (0.01 sec)Code language: JavaScript (javascript)
```


**Seventh**, go to the session of the user `root` and create a new database called `bobdb`:

```
create database bobdb;
```


**Eight**, select the database `bobdb`:

```
use bobdb;
```


**Ninth**, create a new table called `todos`:

```
create table todos(
   id int auto_increment primary key,
   title varchar(255) not null,
   completed bool default false
);
```


**Tenth**, grant all privileges to the `bobdb` to `bob`:

```
grant all privileges on bobdb.* to bob@localhost;
```


Note that you will learn how to grant privileges to a user in the `GRANT` tutorial.

**Eleventh**, go to bob’s session and display all the databases:

```
show databases;
```


Now, `bob` can see the `bobdb`:

```
+--------------------+
| Database           |
+--------------------+
| bobdb              |
| information_schema |
| performance_schema |
+--------------------+
3 rows in set (0.00 sec)Code language: JavaScript (javascript)
```


**Twelfth**, select the database `bobdb`:

```
use bobdb;
```


**Thirteenth**, show the tables from the `bobdb` database:

```
show tables;
```


The user `bob` can see the `lists` table:

```
+-----------------+
| Tables_in_bobdb |
+-----------------+
| todos           |
+-----------------+
1 row in set (0.00 sec)Code language: JavaScript (javascript)
```


**Fourteenth**, insert a row into the `todos` table:

```
insert into todos(title) 
values('Learn MySQL');
```


**Fifteenth**, query data from the `lists` table:

```
select * from todos;
```


This is the output:

```
+----+-------------+-----------+
| id | title       | completed |
+----+-------------+-----------+
|  1 | Learn MySQL |         0 |
+----+-------------+-----------+
1 row in set (0.00 sec)Code language: JavaScript (javascript)
```


So the user `bob` can do everything with the `bobdb` database.

Finally, disconnect from the MySQL Server from both sessions:

```
exit
```


# MySQL GRANT
**Summary**: you will learn how to use the MySQL `GRANT` statement to assign privileges to user accounts.
**Source**: https://www.mysqltutorial.org/mysql-administration/mysql-grant/

Introduction to the MySQL GRANT statement
-----------------------------------------

The `CREATE USER` statement creates a user account with no privileges. It means that the user account can log in to the MySQL Server, but cannot do anything such as selecting a database and querying data from tables.

To enable the user account to work with database objects, you need to grant it privileges. You use the `GRANT` statement to assign one or more privileges to the user account.

Here’s the basic syntax of the `GRANT` statement:

```
GRANT privilege [,privilege],.. 
ON privilege_level 
TO account_name;
```


In this syntax:

*   First, specify one or more privileges after the `GRANT` keyword. If you grant multiple privileges, you need to separate privileges by commas.
*   Second, specify the `privilege_level`, which determines the extent to which the privileges apply. More information on privilege levels will be provided shortly.
*   Third, specify the account name of the user you want to grant privileges after the `TO` keyword.

Notice that to use the `GRANT` statement, you must have the `GRANT OPTION` privilege and the privileges that you are granting. If the system variable `read_only` is enabled, you need to have the `SUPER` privilege to execute the `GRANT` statement.

MySQL privilege levels
----------------------

MySQL supports the following privilege levels:

!MySQL Grant - Privilege Levels

### Global Privileges

**Global privileges** apply to all databases in a MySQL Server. To assign all global privileges, you use the `*.*` syntax, for example:

```
GRANT SELECT 
ON *.* 
TO bob@localhost;
```


The account user `bob@localhost` can manage all databases of the current MySQL Server.

### Database privileges

**Database privileges** apply to all objects in a particular database. To assign database-level privileges, you use the `ON database_name.*` syntax, for example:

```
GRANT INSERT 
ON classicmodels.* 
TO bob@localhost;
```


In this example, `bob@localhost` can manage all objects in the `classicmodels` database.

### Table privileges

**Table privileges** apply to all columns in a table. To assign table-level privileges, you use the `ON database_name.table_name` syntax. For example:

```
GRANT DELETE 
ON classicmodels.employees 
TO bob@localhsot;
```


In this example, `bob@localhost` can manage rows from the `employees` table in the `classicmodels` database.

If you skip the database name, MySQL uses the default database or issues an error if there is no default database.

### Column privileges

**Column privileges** apply to individual columns within a table. You must specify the column or columns for each privilege. For example:

```
GRANT 
   SELECT (employeeNumner,lastName, firstName,email), 
   UPDATE(lastName) 
ON employees 
TO bob@localhost;
```


In this example, `bob@localhost` can select data from four columns:

*   `employeeNumber`
*   `lastName`
*   `firstName`
*   `email`

And updates only the `lastName` column in the `employees` table.

### Stored routine privileges

**Stored routine privileges** apply to stored procedures and stored functions. For example:

```
GRANT EXECUTE 
ON PROCEDURE CheckCredit 
TO bob@localhost;
```


In this example, `bob@localhost` can execute the stored procedure `CheckCredit` in the current database.

### Proxy user privileges

**Proxy user privileges** allow one user to be a proxy for another. The proxy user gets all the privileges of the proxied user. For example:

```
GRANT PROXY 
ON root 
TO alice@localhost;
```


In this example, `alice@localhost` assumes all privileges of the user `root`.

MySQL GRANT statement examples
------------------------------

Typically, you use the `CREATE USER` statement to create a new user account first and then use the `GRANT` statement to grant privileges to the user.

First, create a new user named `super@localhost` by using the following `CREATE USER` statement:

```
CREATE USER super@localhost 
IDENTIFIED BY 'Secure1Pass!';
```


Second, show the privileges assigned to `super@localhost` user by using the `SHOW GRANTS` statement:

```
SHOW GRANTS FOR super@localhost;
```


Output:

```
+-------------------------------------------+
| Grants for super@localhost                |
+-------------------------------------------+
| GRANT USAGE ON *.* TO `super`@`localhost` |
+-------------------------------------------+
1 row in set (0.00 sec)Code language: JavaScript (javascript)
```


The `USAGE` means that the `super@localhost` can log in to the database but has no privilege.

Third, grant all privileges in all databases in the current database server to `super@localhost`:

```
GRANT ALL 
ON classicmodels.* 
TO super@localhost;
```


Fourth, use the `SHOW GRANTS` statement again:

```
SHOW GRANTS FOR super@localhost;
```


Output:

```
+------------------------------------------------------------------+
| Grants for super@localhost                                       |
+------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `super`@`localhost`                        |
| GRANT ALL PRIVILEGES ON `classicmodels`.* TO `super`@`localhost` |
+------------------------------------------------------------------+
2 rows in set (0.00 sec)Code language: JavaScript (javascript)
```


Permissible privileges for the GRANT statement
----------------------------------------------

The following table illustrates all permissible privileges that you can use for the `GRANT` and `REVOKE` statement:



* Privilege: Global
  * Meaning: Database
  * Level: Table
  * Column
  * Stored Routine
  * Proxy
* Privilege: ALL [PRIVILEGES]
  * Meaning: Allow the user to alter and drop stored procedures or stored functions.
  * Level: 
* Privilege: ALTER
  * Meaning: Allow the user to use the ALTER TABLE statement
  * Level: X
  * X
  * X
* Privilege: ALTER ROUTINE
  * Meaning: Allow the user to create databases and tables
  * Level: X
  * X
  * X
* Privilege: CREATE
  * Meaning: Allow the user to create stored procedures and stored functions
  * Level: X
  * X
  * X
* Privilege: CREATE ROUTINE
  * Meaning: Allow the user to create a temporary table by using CREATE TEMPORARY TABLE statement
  * Level: X
  * X
* Privilege: CREATE TABLESPACE
  * Meaning: Allow the user to create, alter, or drop tablespaces and log file groups
  * Level: X
* Privilege: CREATE TEMPORARY TABLES
  * Meaning: Allow the user to use the CREATE USER, DROP USER, RENAME USER, and REVOKE ALL PRIVILEGES statements.
  * Level: X
  * X
* Privilege: CREATE USER
  * Meaning: Allow the user to create or modify the view.
  * Level: X
* Privilege: CREATE VIEW
  * Meaning: Allow the user to use DELETE statement
  * Level: X
  * X
  * X
* Privilege: DELETE
  * Meaning: Allow the user to execute stored routines
  * Level: X
  * X
  * X
* Privilege: DROP
  * Meaning: Allow the user to drop database, table, and view
  * Level: X
  * X
  * X
* Privilege: EVENT
  * Meaning: Allow the user to use events for the Event Scheduler.
  * Level: X
  * X
* Privilege: EXECUTE
  * Meaning: Allow the user to drop the database, table, and view
  * Level: X
  * X
  * X
* Privilege: FILE
  * Meaning: Allow the user to have privileges to grant or revoke privileges from other accounts.
  * Level: X
* Privilege: GRANT OPTION
  * Meaning: Allow the user to create or drop indexes.
  * Level: X
  * X
  * X
  * X
  * X
* Privilege: INDEX
  * Meaning: Allow the user to create or drop indexes.
  * Level: X
  * X
  * X
* Privilege: INSERT
  * Meaning: Allow the user to use the INSERT statement
  * Level: X
  * X
  * X
  * X
* Privilege: LOCK TABLES
  * Meaning: Allow the user to query to see where the master or slave servers are
  * Level: X
  * X
* Privilege: PROCESS
  * Meaning: Allow the user to see all processes with SHOW PROCESSLIST statement.
  * Level: X
* Privilege: PROXY
  * Meaning: Enable user proxying.
  * Level: 
* Privilege: REFERENCES
  * Meaning: Allow user to create a foreign key
  * Level: X
  * X
  * X
  * X
* Privilege: RELOAD
  * Meaning: Allow the user to use FLUSH statement
  * Level: X
* Privilege: REPLICATION CLIENT
  * Meaning: Allow the user to query to see where master or slave servers are
  * Level: X
* Privilege: REPLICATION SLAVE
  * Meaning: Allow the user to use replicate slaves to read binary log events from the master.
  * Level: X
* Privilege: SELECT
  * Meaning: Allow the user to use SELECT statement
  * Level: X
  * X
  * X
  * X
* Privilege: SHOW DATABASES
  * Meaning: Allow user to show all databases
  * Level: X
* Privilege: SHOW VIEW
  * Meaning: Allow the user to use SHOW CREATE VIEW statement
  * Level: X
  * X
  * X
* Privilege: SHUTDOWN
  * Meaning: Allow user to use mysqladmin shutdown command
  * Level: X
* Privilege: SUPER
  * Meaning: Allow the user to use other administrative operations such as CHANGE MASTER TO, KILL, PURGE BINARY LOGS, SET GLOBAL, and mysqladmin command
  * Level: X
* Privilege: TRIGGER
  * Meaning: Allow the user to use TRIGGER operations.
  * Level: X
  * X
  * X
* Privilege: UPDATE
  * Meaning: Allow the user to use the UPDATE statement
  * Level: X
  * X
  * X
  * X
* Privilege: USAGE
  * Meaning: Equivalent to “no privileges”
  * Level: 
