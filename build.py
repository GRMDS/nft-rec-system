import pymysql
#import logging

nft_db_config = {
    'user': 'analyst',
    'password': 'analyst',
    'host': '35.80.119.80',
    'database': 'testnft'
}

grmds_db_config = {
    'user': 'analyst',
    'password': 'analyst',
    'host': '54.189.68.146',
    'database': 'grmds054_druptest'
}

def get_nft_items():
    cursor = nft_conn.cursor()

    select_query = ("SELECT nft_id, name, description, price, usdt_price, quantity, \
                    category_id, token_id FROM fc_nft_items WHERE onsell = 1 limit 10")
    cursor.execute(select_query)
    rows = cursor.fetchall()

    for row in rows:
        item = {}
        item["nft_id"] = row[0]
        item["name"] = row[1]
        item["description"] = row[2]
        item["price"] = row[3]
        item["usdt_price"] = row[4]
        item["quantity"] = row[5]
        item["category_id"] = row[6]
        item["token_id"] = row[7]
        print(item)
    
    cursor.close()

if __name__ == "__main__":
    nft_conn = pymysql.connect(**nft_db_config)

    grmds_conn = pymysql.connect(**grmds_db_config)

    if nft_conn:
        get_nft_items()

    if grmds_conn:
        print("GRMDS connect successfully.")