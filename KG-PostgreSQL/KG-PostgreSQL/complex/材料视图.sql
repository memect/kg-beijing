DROP MATERIALIZED VIEW IF EXISTS dish_stuff;

CREATE MATERIALIZED VIEW dish_stuff AS
SELECT name, stuff, nullif(g, '')::bigint as g
	FROM (
	(
		SELECT
			name,
			jsonb_array_elements(stuff)->>'名称' AS stuff,
			jsonb_array_elements(stuff)->>'用量' AS detail,
			regexp_replace(jsonb_array_elements(stuff)->>'用量', '[^\d]+', '', 'g') AS g
		FROM (
			SELECT name, data->'辅料' AS stuff
			FROM dish
			WHERE data ? '辅料'
		) temp1
	)
	UNION
	(
		SELECT
			name,
			data->>'主料名称' AS stuff,
			data->>'主料用量' AS detail,
			regexp_replace(data->>'主料用量', '[^\d]+', '', 'g') AS g
		FROM dish
		WHERE data ? '主料名称'
		AND data ? '主料用量'
	)
) temp2;
