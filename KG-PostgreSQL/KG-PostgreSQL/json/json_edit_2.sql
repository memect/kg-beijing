UPDATE dish
SET name='仰望星空', data=jsonb_set(data, '{口味}', '"神奇"')
WHERE name='仰望星空';

/* 可以按照路径来设置，路径如果不存在则不会设置，也不会报错 */
