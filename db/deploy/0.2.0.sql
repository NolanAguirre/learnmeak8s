-- Deploy foo:0.2.0 to pg
--all code in this file is required for postgraile to run
--these changes are required because of the tightened security from 0.0.0
BEGIN;

GRANT EXECUTE ON FUNCTION current_setting(TEXT) TO PUBLIC;

COMMIT;
