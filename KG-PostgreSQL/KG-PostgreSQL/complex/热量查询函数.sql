DROP FUNCTION IF EXISTS find_dish_calories(text);

CREATE OR REPLACE FUNCTION
find_dish_calories (dish_name text)
RETURNS TABLE
(name text, stuff text, weight numeric, calories numeric)
AS $$
SELECT
	dish_stuff.name as name,
	string_agg(stuff, ',') as stuff,
	sum(g) as weight,
	sum(g / 100.0 * calories) AS calories
FROM dish_stuff JOIN stuff_calories
ON dish_stuff.stuff = stuff_calories.name
WHERE dish_stuff.name = dish_name
GROUP BY dish_stuff.name
$$ LANGUAGE SQL;

select * from find_dish_calories('华夫饼');
select * from find_dish_calories('南瓜饼');
select * from find_dish_calories('红烧排骨');
