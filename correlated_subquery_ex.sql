create view AvgPriceByType as 
select product_id, 
	   product_name,
	   product_type,
	   sale_price,
	   (select avg(sale_price)
	      from Product as P2
	     where P1.product_type = P2.product_type
	     group by P2.product_type) as avg_sale_price
from Product as P1;

select * from AvgPriceByType;