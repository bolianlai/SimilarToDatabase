import time
'''
实现一个类Database，其拥有四个接口：insert、delete、update、select，
各接口参数规范可以自由发挥，但需要分别实现保存数据、删除数据、更新数据、查询数据。
Database类中保存的所有数据都具有相同的数据结构（即类比关系型数据库中的表）。
不要求功能完善性和复杂度，可省略错误检查与异常处理，仅保证逻辑的正确性和体现思路即可。
'''

class Database(object):
    def __init__(self, fields):
        self.field = dict.fromkeys(fields)
        print('field:', self.field)
        self.data = list()

    def insert(self):
        insert_data = dict()
        for f in self.field:
            insert_data[f] = input('输入字段 {} 的数据: '.format(f))
        self.data.append({str(int(time.time())): insert_data})

    def delete(self):
        delete_id = input('输入要删除的数据的 id（时间戳）：')
        for i, v in enumerate(self.data):
            key, = v
            if delete_id == key:
                self.data.pop(i)

    def update(self):
        update_id = input('输入要更新的数据的 id（时间戳）：')
        for i, v in enumerate(self.data):
            key, = v
            if update_id == key:
                update_data = dict()
                for f in self.field:
                    update_data[f] = input('输入更新字段 {} 的数据: '.format(f))
                self.data[i][key] = update_data
                
    def select(self):
        select_id = input('输入要查询的数据的 id（时间戳）：')
        for i, v in enumerate(self.data):
            key, = v
            if select_id == key:
                print(self.data[i])


if __name__ == "__main__":
    field = input('定义数据结构，使用空格间隔多个字段：')
    fields = set(field.split(' '))
    database = Database(fields)
    
    while True:
        operate = input('可选操作：\n1、保存数据\n2、删除数据\n3、更新数据\n4、查询数据\n选择你要执行的操作：')
        if operate == '1':
            print('Tip：正在进行保存数据操作...\n')
            database.insert()
            pass
        elif operate == '2':
            print('Tip：正在进行删除数据操作...\n')
            database.delete()
            pass
        elif operate == '3':
            print('Tip：正在进行更新数据操作...\n')
            database.update()
            pass
        elif operate == '4':
            print('Tip：正在进行查询数据操作...\n')
            database.select()
            pass
        else:
            print('Tip：正在进行无效操作，请重新选择操作！\n')

        print('当前数据为：\n', database.data)