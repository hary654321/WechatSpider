import sqlite3

class SQLiteManager:
    def __init__(self, db_name):
        """
        初始化 SQLite 管理器
        :param db_name: 数据库文件名
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """
        连接到 SQLite 数据库
        """
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        """
        关闭数据库连接
        """
        if self.conn:
            self.conn.close()

    def create_table(self):
        """
        创建 users 表
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_user(self, name, age, email):
        """
        插入用户数据
        :param name: 用户姓名
        :param age: 用户年龄
        :param email: 用户邮箱
        """
        self.cursor.execute('''
            INSERT INTO users (name, age, email)
            VALUES (?, ?, ?)
        ''', (name, age, email))
        self.conn.commit()

    def select_all_users(self):
        """
        查询所有用户数据
        :return: 用户数据列表
        """
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def update_user_age(self, user_id, new_age):
        """
        更新用户年龄
        :param user_id: 用户 ID
        :param new_age: 新的年龄
        """
        self.cursor.execute('''
            UPDATE users
            SET age = ?
            WHERE id = ?
        ''', (new_age, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        """
        删除用户数据
        :param user_id: 用户 ID
        """
        self.cursor.execute('''
            DELETE FROM users
            WHERE id = ?
        ''', (user_id,))
        self.conn.commit()

# 使用示例
if __name__ == "__main__":
    db = SQLiteManager("example.db")
    db.connect()
    db.create_table()

    # 插入数据
    db.insert_user("Alice", 25, "alice@example.com")
    db.insert_user("Bob", 30, "bob@example.com")

    # 查询数据
    users = db.select_all_users()
    print("所有用户数据：")
    for user in users:
        print(user)

    # 更新数据
    db.update_user_age(1, 26)

    # 查询更新后的数据
    users = db.select_all_users()
    print("更新后的用户数据：")
    for user in users:
        print(user)

    # 删除数据
    db.delete_user(2)

    # 查询删除后的数据
    users = db.select_all_users()
    print("删除后的用户数据：")
    for user in users:
        print(user)
