-- FUNCTION: weatherman.trigger_set_timestamp()

-- DROP FUNCTION weatherman.trigger_set_timestamp();

CREATE FUNCTION weatherman.trigger_set_timestamp()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
BEGIN
  NEW.last_updated = NOW();
  RETURN NEW;
END;
$BODY$;

ALTER FUNCTION weatherman.trigger_set_timestamp()
    OWNER TO "pgAdminUser";