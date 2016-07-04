SELECT
	dish_stuff.name,
	string_agg(stuff, ','),
	sum(g),
	sum(calories),
	sum(g / 100.0 * calories) AS result
FROM dish_stuff JOIN stuff_calories
ON dish_stuff.stuff = stuff_calories.name
WHERE dish_stuff.name = '华夫饼'
GROUP BY dish_stuff.name
