from apps.posts.queries import PostsQueries, CommentsQueries


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
        posts_id = int(input("Enter posts id: "))
        self.update(title,posts_id)


class CommentViews(CommentsQueries):
    def commentupdate(self):
        post_id = int(input("Enter id post: "))
        user_id = int(input("Enter id user: "))
        user_comment = input("Enter comment: ")
        self.update(post_id,user_id,user_comment)

    def commentadd(self):
        user_comment = input("Enter comment: ")
        post_id = int(input("Enter id post: "))
        user_id = int(input("Enter id user: "))
        self.add(user_comment,post_id,user_id)

