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
limit 100;
