from apps.posts.queries import PostsQueries


class PostsViews(PostsQueries):
    def productadd(self):
        title = input("Enter title: ")
        description = input("Enter description: ")
        price = int(input("Enter price: "))
        self.add(title,description,price)

    def productdelete(self):
        product_name = input("Enter product for delete: ")
        self.delete(product_name)

    def productupdate(self):
        title = input("Enter title: ")
        posts_id = int(input("Enter posts id"))
        self.update(title,posts_id)


