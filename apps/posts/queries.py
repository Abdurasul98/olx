from core.database import execute_query


class PostsQueries:
    @staticmethod
    def show():
        query_post = """SELECT * FROM posts;"""
        data = execute_query(query=query_post, fetch="all")
        for row in data:
            print(row)

    @staticmethod
    def add(title,description,price):
        try:
            query_post = """
                    INSERT INTO posts (title,description,price,is_active,created_at) 
                    VALUES (%s, %s, %s, %s,CURRENT_TIMESTAMP);
                            """
            params = (title, description, price, True)

            execute_query(query=query_post, params=params)
            print("Posted")
        except Exception as e:
            print(e)

    @staticmethod
    def update(title,posts_id):
        try:
            query_post = """
                    UPDATE posts SET title = %s WHERE id = %s;
                                """
            params = (title, posts_id)

            execute_query(query=query_post, params=params)
            print("Update")
        except Exception as e:
            print(e)

    @staticmethod
    def delete(product_name):
        try:
            query_post = """
                    DELETE FROM posts WHERE title = %s;
                                    """
            params = (product_name,)

            execute_query(query=query_post, params=params)
            print("Product deleted")
        except Exception as e:
            print(e)