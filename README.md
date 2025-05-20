select gds2.Retailer_code, gds2.Retailer_code , count(distinct gp.Product)
from (select *
		from go_retailers gr 
		where gr.Country = "France") gr, 
	(select *
		from go_retailers gr 
		where gr.Country = "France") gr2  , go_daily_sales gds, go_daily_sales gds2, go_products gp
where year (gds2.`Date`) = year (gds.`Date`) and year(gds2.`Date`) = 2015
and gr.Retailer_code < gr2.Retailer_code and gds.Retailer_code = gr.Retailer_code and gds2.Retailer_code = gr2.Retailer_code 
and gp.Product_number = gds.Product_number and gp.Product_number = gds2.Product_number
group by gds.Retailer_code, gds2.Retailer_code  
