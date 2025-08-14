--So, users arent database specific, it lives at the postgres server level.
--Even if you drop the database, it will not drop the users.
--This script cleans up the users so that we can fully reset the database without requiring revert scripts running.
--Really meant for local development only, dont run reset or reseed on production.

BEGIN;


COMMIT;