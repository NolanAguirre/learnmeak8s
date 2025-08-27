-- Deploy foo:0.1.0 to pg


--things in this file are generally usful utilities that can be used during everyday interactions with the database
--they are not schema changing functions like 0.0.0, they opearte on the data of the database, not the schema
BEGIN;

-- Create a generic trigger function to update created_at if the new and old records are distinct
CREATE OR REPLACE FUNCTION util.update_created_at()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW IS DISTINCT FROM OLD THEN
        NEW.created_at = NOW();
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;



COMMIT;
