from nbp.test_case.models import function
import pymysql


def main():
    cyberaudit_conf_db = pymysql.connect()

    path = r''
    sheet_info = function.read_data(
        0,
        path
    )

    sql_list = []

    for row in sheet_info:
        sql_list.append(f'''
            UPDATE `comp_knowledge` 
            SET `content` = '{row[2]}' 
            WHERE `standard_id` = 1007 AND `name` = '{row[0]}'
        ''')

    try:
        with cyberaudit_conf_db.cursor() as cursor:
            for sql in sql_list:
                cursor.execute(sql)
        cyberaudit_conf_db.commit()
    except:
        cyberaudit_conf_db.rollback()
    finally:
        cyberaudit_conf_db.close()


if __name__ == '__main__':
    pass
