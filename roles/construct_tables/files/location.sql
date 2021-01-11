-- Table: weatherman.location

-- DROP TABLE weatherman.locaton;

CREATE TABLE weatherman.location
(
    location_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 100 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    lat double precision,
    lon double precision,
    timezone text COLLATE pg_catalog."default",
    timezone_offset bigint,
    last_updated timestamp with time zone DEFAULT now(),
    date_created timestamp with time zone DEFAULT now(),
    CONSTRAINT location_pkey PRIMARY KEY (location_id)
)

TABLESPACE pg_default;

ALTER TABLE weatherman.location
    OWNER to "pgAdminUser";

-- Trigger: set_last_updated

-- DROP TRIGGER set_last_updated ON weatherman.location;

CREATE TRIGGER set_last_updated
    BEFORE UPDATE 
    ON weatherman.location
    FOR EACH ROW
    EXECUTE PROCEDURE weatherman.trigger_set_timestamp();