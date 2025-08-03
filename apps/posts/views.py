from core.database import execute_query


class PostsViews:
    @staticmethod
    def postproduct():
        title = input("Enter title: ")
        description = input("Enter description: ")
        price = int(input("Enter price: "))

        query_post = """
            INSERT INTO posts (title,description,price,is_active,created_at) 
            VALUES (%s, %s, %s, %s,CURRENT_TIMESTAMP);
        """
        params = (title,description,price,True)

        execute_query(query=query_post,params=params)
        print("Posted")