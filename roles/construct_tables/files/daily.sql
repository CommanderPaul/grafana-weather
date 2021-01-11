-- Table: weatherman.daily

-- DROP TABLE weatherman.daily;

CREATE TABLE weatherman.daily
(
    daily_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 100 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    location_id bigint,
    dt timestamp with time zone,
    sunrise timestamp with time zone,
    sunset timestamp with time zone,
    temp_day double precision,
    temp_min double precision,
    temp_max double precision,
    temp_night double precision,
    temp_eve double precision,
    temp_morn double precision,
    feels_like_day double precision,
    feels_like_night double precision,
    feels_like_eve double precision,
    feels_like_morn double precision,
    pressure bigint,
    humidity bigint,
    dew_point double precision,
    wind_speed double precision,
    wind_deg integer,
    clouds integer,
    pop integer,
    uvi double precision,
    last_updated timestamp with time zone DEFAULT now(),
    date_created timestamp with time zone DEFAULT now(),
    CONSTRAINT daily_pkey PRIMARY KEY (daily_id)
)

TABLESPACE pg_default;

ALTER TABLE weatherman.daily
    OWNER to "pgAdminUser";

-- Trigger: set_last_updated

-- DROP TRIGGER set_last_updated ON weatherman.location;

-- CREATE TRIGGER set_last_updated
--     BEFORE UPDATE 
--     ON weatherman.location
--     FOR EACH ROW
--     EXECUTE PROCEDURE weatherman.trigger_set_timestamp();