
-- Create a login user that will be used by our Python application
-- NOTE: We modified /etc/postgresql/11/main/pg_hba.conf to perform peer based authentication with our
--		 Linux user and the 'python' Postgres role.
CREATE ROLE retail_db_manager;

CREATE ROLE python LOGIN;
