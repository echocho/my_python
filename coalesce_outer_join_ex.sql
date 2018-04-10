select coalesce(SP.shop_id, 'Unknown') as shop_id, 
coalesce(SP.shop_name, 'Unknown') as shop_name, 
P.product_id, 
P.product_name, 
P.sale_price
from ShopProduct as SP right outer join Product as P
on SP.product_id = P.product_id;