UPDATE dish
SET name='仰望星空', data='{"人数": 10, "时间": "30分钟", "口味": {"奇葩": "满分", "神奇": "尚可"}}'
WHERE name='仰望星空';

/* 获取第一层，返回jsonb结果 */

SELECT name, data->'口味' AS 口味
FROM dish
WHERE name='仰望星空'

/* 获取第一层，字符串，返回text结果 */

SELECT name, data->>'口味' AS 口味
FROM dish
WHERE name='仰望星空'

/* 获取第一层，jsonb，然后再获取第二层，返回text结果 */

SELECT name, data->'口味'->>'奇葩' AS 口味
FROM dish
WHERE name='仰望星空'

/* 路径获取，返回jsonb结果 */

SELECT name, data#>'{口味,奇葩}' AS 口味
FROM dish
WHERE name='仰望星空'

/* 路径获取，返回text */

SELECT name, data#>>'{口味,奇葩}' AS 口味
FROM dish
WHERE name='仰望星空'
