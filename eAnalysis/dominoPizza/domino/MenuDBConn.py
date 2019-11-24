import MySQLdb  # MySQLdb 설정


def menu_insert():
    # db 연결
    conn = MySQLdb.connect(host='192.168.0.59', user='scott', passwd='tiger', db='pythondb')

    # conn.set_character_set('utf-8')

    cur = conn.cursor()

    sql = "INSERT INTO menu (m_name,m_price,m_desc,c_id,m_quantity,m_img) VALUES('1',2,'3',4,5,'6')"

    # cur.execute(sql, (values.m_name, values.m_price, values.m_desc, values.c_id, values.m_quantity, values.m_img))
    cur.execute(sql)

    conn.commit()

    conn.close()

menu_insert()