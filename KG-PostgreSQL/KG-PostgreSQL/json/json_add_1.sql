UPDATE dish
SET name='仰望星空', data=data || jsonb '{"口味": "奇葩"}'
WHERE name='仰望星空';
