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

# Get the NFT Category List
def get_nft_category_list():
    cursor = nft_conn.cursor()

    select_query = ("SELECT id, name FROM fc_nft_category WHERE deleted = 0")
    cursor.execute(select_query)
    rows = cursor.fetchall()

    category_list = []
    
    for row in rows:
        category = {}
        category["id"] = row[0]
        category["name"] = row[1]
        category_list.append(category)
    
    cursor.close()

    return category_list

def get_nft_items_by_category(category_id):
    cursor = nft_conn.cursor()

    select_query = ("SELECT nft_id, name, description, price, usdt_price, quantity, \
                    category_id, token_id FROM fc_nft_items WHERE onsell = 1 AND category_id = %d limit 3" 
                    % (category_id))
    cursor.execute(select_query)
    rows = cursor.fetchall()

    for row in rows:
        item = {}
        item["nft_id"] = row[0]
        item["name"] = row[1]
        #item["description"] = row[2]
        #item["price"] = row[3]
        #item["usdt_price"] = row[4]
        item["quantity"] = row[5]
        item["category_id"] = row[6]
        #item["token_id"] = row[7]
        print(item)
    
    cursor.close()

def get_nft_items():
    category_list = get_nft_category_list()
    print(category_list)
    for category in category_list:
        get_nft_items_by_category(category["id"])

if __name__ == "__main__":
    nft_conn = pymysql.connect(**nft_db_config)

    grmds_conn = pymysql.connect(**grmds_db_config)

    if nft_conn:
        get_nft_items()

    if grmds_conn:
        print("GRMDS connect successfully.")