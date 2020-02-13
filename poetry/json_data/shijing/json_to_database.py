'''将 json 转换到数据库'''
# https://shockerli.net/post/python3-pymysql/

import json
import pymysql

import os
print(os.getcwd())

# 连接数据库。假设数据库中已经建好了名为 poetry 的空数据库。
poetry = pymysql.connect(host='localhost',
                         port=3306,
                         user='django',
                         password='7788',
                         db='saba',
                         charset='utf8')
cursor = poetry.cursor()




# 转存《诗经》。
# 读取 shijing.json 到变量 shijing 中。
with open('./shijing.json', 'r', encoding='UTF-8') as f:
    shijing = json.load(f)

# 查看 shijing.json 中有哪些 key
# for k in shijing[0].keys():
#     print(k)

# 为 shijing 创建一个表。
# cursor.execute('''
#                create table shijing(id int not null auto_increment,
#                                     title varchar(32) not null,
#                                     chapter varchar(32) not null,
#                                     section varchar(32) not null,
#                                     content varchar(8000) not null,
#                                     primary key (id)
#                                    )
#                ''')


# 将数组写入数据库。
shijing_sql = ('insert into poetry_shijing (title, chapter, section, content, fixed_id)'
               + 'values (%s, %s, %s, %s, %s)')
shijing_values = [list(v.values()) for v in shijing]  # 将字典转换为数组

i = 0
for v in shijing_values:                              # 
    v[3] = '\n'.join(v[3])                            # 将数组转换为字符串
    i += 1                                            # 添加 fixed_id 字段
    v.append(i)
    
cursor.executemany(shijing_sql, shijing_values[:])  # 写入数据库
poetry.commit()                                      # 提交更改

    


