from core.database import execute_query


class AdminQueries:
    @staticmethod
    def get_users():
        try:
            query = """SELECT id,full_name,phone_number, is_active FROM users;"""
            users = execute_query(query=query, fetch="all")
            for user in users:
                print(user)
        except Exception as e:
            print(e)



    @staticmethod
    def count_users():
        try:
            query = """SELECT COUNT(*) FROM users;"""
            result = execute_query(query=query, fetch="one")
            print(f"Total users: {result[0]}")
        except Exception as e:
            print(e)

    @staticmethod
    def count_posts():
        try:
            query = """SELECT COUNT(*) FROM posts;"""
            result = execute_query(query=query, fetch="one")
            print(f"Total posts: {result[0]}")
        except Exception as e:
            print(e)