UPDATE dish
SET name='仰望星空', data=jsonb_set(data, '{口味,美味}', '"真的?"')
WHERE name='仰望星空';
