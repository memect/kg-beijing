UPDATE dish
SET name='仰望星空', data='{"人数": 10, "时间": "30分钟", "口味": {"奇葩": "满分", "神奇": "尚可"}}'
WHERE name='仰望星空';

/* 判断是否包含，返回boolean结果 */

SELECT name, data @> '{"人数":10}'
FROM dish
WHERE name='仰望星空'

/* 判断是否包含，返回boolean结果 */

SELECT name, '{"人数":10}' <@ data
FROM dish
WHERE name='仰望星空'

/* 判断是否包含，返回boolean结果 */

SELECT name, data ? '口味'
FROM dish
WHERE name='仰望星空'

/* 判断是否包含，或，返回boolean结果 */

SELECT name, data ?| array['口味', '质地']
FROM dish
WHERE name='仰望星空'

/* 判断是否包含，与，返回boolean结果 */

SELECT name, data ?& array['口味', '质地']
FROM dish
WHERE name='仰望星空'
