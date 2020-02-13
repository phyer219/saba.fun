
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
ci_values = []
for i in range(0, 21050, 1000):  # 依次读取文件
    with open('./ci.song.%i.json'%i, 'r', encoding='UTF-8') as f:
        ci = json.load(f)
    ci_values += [list(v.values()) for v in ci]  # 将读出的将字典转换为数组, 然
    # 后累加

# print(len(ci_values))           # 查验个数是否正确
# 将数组写入数据库。
ci_sql = ('insert into poetry_ci (author, paragraphs, rhythmic, tags, fixed_id)'
               + 'values (%s, %s, %s, %s, %s)')


i = 0
for v in ci_values:                              # 
    v[1] = '\n'.join(v[1])                            # 将数组转换为字符串
    i += 1                                            # 添加 fixed_id 字段
    if len(v)==3:                                     # 缺少 tags 字段的添加为空
        v.append('')

    if isinstance(v[3], list):  # tags 有时候也是数组
        v[3] = ' '.join(v[3])                            # 将数组转换为字符串
        
    v.append(i)

cursor.executemany(ci_sql, ci_values[:])  # 写入数据库
poetry.commit()                                      # 提交更改

    


