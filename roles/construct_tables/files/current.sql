-- Table: weatherman.current

-- DROP TABLE weatherman.current;

CREATE TABLE weatherman.current
(
    current_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 100 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    location_id bigint,
    dt timestamp with time zone,
    sunrise timestamp with time zone,
    sunset timestamp with time zone,
    temp double precision,
    feels_like double precision,
    pressure bigint,
    humidity bigint,
    dew_point double precision,
    clouds integer,
    uvi double precision,
    visibility bigint,
    wind_speed double precision,
    wind_gust double precision,
    wind_deg integer,
    last_updated timestamp with time zone DEFAULT now(),
    date_created timestamp with time zone DEFAULT now(),
    CONSTRAINT current_pkey PRIMARY KEY (current_id)
)

TABLESPACE pg_default;

ALTER TABLE weatherman.current
    OWNER to "pgAdminUser";

-- Trigger: set_last_updated

-- DROP TRIGGER set_last_updated ON weatherman.location;

-- CREATE TRIGGER set_last_updated
--     BEFORE UPDATE 
--     ON weatherman.location
--     FOR EACH ROW
--     EXECUTE PROCEDURE weatherman.trigger_set_timestamp();