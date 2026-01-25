SELECT P.product_id, IF(ROUND(SUM(P.price * U.units) / SUM(U.units), 2) IS NOT NULL, ROUND(SUM(P.price * U.units) / SUM(U.units), 2), 0) AS average_price FROM Prices P LEFT OUTER JOIN
UnitsSold U ON
(P.product_id = U.product_id AND P.start_date <= U.purchase_date AND U.purchase_date <= P.end_date)
GROUP BY P.product_id;