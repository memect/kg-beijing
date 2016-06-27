DROP MATERIALIZED VIEW IF EXISTS stuff_calories;
CREATE MATERIALIZED VIEW stuff_calories AS
SELECT
	name,
	nullif(regexp_replace(data->>'热量', '[^\d]+', '', 'g'), '')::bigint as calories
FROM stuff
WHERE data ? '热量'
