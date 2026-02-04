SELECT P1.product_id, IFNULL(
    (SELECT P2.new_price FROM Products P2
    WHERE P2.product_id = P1.product_id
    AND P2.change_date <= "2019-08-16"
    ORDER BY P2.change_date DESC
    LIMIT 1)
, 10) AS price FROM Products P1
GROUP BY P1.product_id;