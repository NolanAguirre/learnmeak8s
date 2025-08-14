-- Deploy foo:1.000.0 to pg

BEGIN;

SELECT util.create_extension('citext');




SELECT util.create_role('middleware', FALSE);
SELECT util.create_role('foo_admin', TRUE);






CREATE SCHEMA IF NOT EXISTS foo;
CREATE TABLE IF NOT EXISTS foo.users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS foo.accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES foo.users(id),
    account_name TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);











COMMIT;
