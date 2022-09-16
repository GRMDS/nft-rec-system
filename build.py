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

def get_nft_items_by_category(category_id, category_name):
    cursor = nft_conn.cursor()
    item_list = []
    select_query = ("SELECT nft_id, name, description, img_url, price, quantity, item_owner, \
                    category_id, token_id FROM fc_nft_items WHERE onsell = 1 AND category_id = %d \
                    limit 5" 
                    % (category_id))
    cursor.execute(select_query)
    rows = cursor.fetchall()

    for row in rows:
        item = {}
        item["nft_id"] = row[0]
        item["name"] = row[1]
        item["description"] = row[2]

        image_url = row[3]
        str_index = image_url.find("/static/upload")
        if str_index == 0:
            str_index = 14
        final_image_url = image_url[:str_index] + '/' + image_url[str_index:]
        item["img_url"] = final_image_url
        item["price"] = row[4]
        item["quantity"] = row[5]
        item["item_owner"] = row[6]
        item["category_id"] = row[7]
        item["token_id"] = row[8]
        item["category_name"] = category_name
        item_list.append(item)
    
    cursor.close()

    return item_list

def remove_recom_records():
    cursor = grmds_conn.cursor()
    del_query = "TRUNCATE dr_recom_nft_item"
    cursor.execute(del_query)
    grmds_conn.commit()
    cursor.close()


def get_nft_items():
    category_list = get_nft_category_list()
    item_all = []
    for category in category_list:
        item_list = get_nft_items_by_category(category["id"], category["name"])
        item_all.extend(item_list)
    return item_all

def create_recom_record(item_list):
    cursor = grmds_conn.cursor()
    
    for item in item_list:
        select_query = ("INSERT INTO dr_recom_nft_item (nft_id, name, description, img_url, price, quantity, item_owner, \
                    category_name, token_id) VALUES (%s, \"%s\", \"%s\", \"%s\", \"%s\", %s, \"%s\", \"%s\", %s) " 
                    % (item["nft_id"], item["name"], item["description"], item["img_url"], str(item["price"]), item["quantity"], item["item_owner"], item["category_name"], item["token_id"]))
        cursor.execute(select_query)
        grmds_conn.commit()
    cursor.close()
        

def update_recom_nft_items():
    item_list = get_nft_items()
    remove_recom_records()
    create_recom_record(item_list)

if __name__ == "__main__":
    nft_conn = pymysql.connect(**nft_db_config)

    grmds_conn = pymysql.connect(**grmds_db_config)

    if nft_conn and grmds_conn:
        update_recom_nft_items()