UPDATE dish
SET name='仰望星空', data=data || jsonb '{"口味": "奇葩"}'
WHERE name='仰望星空';

/* 缺陷是只能设置最上层 */
