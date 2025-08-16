-- Deploy foo:1.000.0 to pg

BEGIN;

SELECT util.create_extension('citext');

SELECT util.create_role('middleware', FALSE);
SELECT util.create_role('foo_admin', TRUE);

CREATE SCHEMA IF NOT EXISTS foo;

CREATE TABLE IF NOT EXISTS foo.account_type (
    "type" CITEXT PRIMARY KEY
);
INSERT INTO foo.account_type ("type") VALUES ('user'), ('admin') ON CONFLICT DO NOTHING;

CREATE TABLE IF NOT EXISTS foo.accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    "type" CITEXT NOT NULL REFERENCES foo.account_types("type") DEFAULT 'user',
    "name" CITEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS foo.users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id UUID NOT NULL REFERENCES foo.accounts(id),
    "name" CITEXT NOT NULL UNIQUE,
    email CITEXT NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);


CREATE TABLE IF NOT EXISTS foo.event_type (
    "type" CITEXT PRIMARY KEY
);
INSERT INTO foo.event_type ("type") VALUES ('user_created'), ('user_updated'), ('user_deleted') ON CONFLICT DO NOTHING;

CREATE TABLE IF NOT EXISTS foo.event_status (
    "status" CITEXT PRIMARY KEY
);
INSERT INTO foo.event_status ("status") VALUES ('pending'), ('processing'), ('completed'), ('failed'), ('human_intervention') ON CONFLICT DO NOTHING;

CREATE TABLE IF NOT EXISTS foo.events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_type CITEXT NOT NULL REFERENCES foo.event_type("type"),
    "status" CITEXT NOT NULL REFERENCES foo.event_status("status") DEFAULT 'pending',
    payload JSONB NOT NULL,
    output_data JSONB,
    completed_at TIMESTAMPTZ,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    retries SMALLINT NOT NULL DEFAULT 0,
    deleted BOOLEAN NOT NULL DEFAULT FALSE
);


-- Attach the trigger to foo.events using util.create_trigger
SELECT util.create_trigger(
    'events_update_created_at',         -- trigger_name
    'foo.events',                       -- table_name
    'util.update_created_at',           -- function_name
    'BEFORE',                           -- timing
    'UPDATE'                            -- events
);

COMMIT;
