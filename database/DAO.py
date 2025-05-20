from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getDifferentCountry():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """select distinct gr.Country 
                    from go_retailers gr """

        cursor.execute(query)
        for row in cursor:
            res.append(row['Country'])
        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """select distinct year(`Date`) as anno
                        from go_daily_sales g"""

        cursor.execute(query)

        for row in cursor:
            print(row['anno'])
            res.append(row['anno'])

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getNodes(country):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """select *
                    from go_retailers gr 
                    where gr.Country = %s """

        cursor.execute(query, (country,))

        for row in cursor:
            res.append(Retailer(**row))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getArchi(country, anno, idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """select gds.Retailer_code as r1, gds2.Retailer_code as r2, count(distinct gp.Product) as peso
                    from (select *
                            from go_retailers gr 
                            where gr.Country = %s) gr, 
                        (select *
                            from go_retailers gr 
                            where gr.Country = %s) gr2  , go_daily_sales gds, go_daily_sales gds2, go_products gp
                    where year (gds2.`Date`) = year (gds.`Date`) and year(gds2.`Date`) = %s
                    and gr.Retailer_code < gr2.Retailer_code and gds.Retailer_code = gr.Retailer_code and gds2.Retailer_code = gr2.Retailer_code 
                    and gp.Product_number = gds.Product_number and gp.Product_number = gds2.Product_number
                    group by gds.Retailer_code, gds2.Retailer_code    """

        cursor.execute(query, (country, country, anno))

        for row in cursor:
            res.append((idMap[row['r1']], idMap[row['r2']], row['peso']))

        cursor.close()
        conn.close()
        return res