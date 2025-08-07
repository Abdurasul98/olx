import logging

from apps.admin.queries import AdminQueries
from apps.auth.views import RegisterView, LogoutView, LoginView
from apps.messages.views import MessageView
from apps.posts.queries import PostsQueries
from apps.posts.views import PostsViews
from core.utils import main_menu, get_user_option, execute_tables, user_menu, message_menu, admin_menu

logging.basicConfig(level=logging.INFO, filename='logs.log')
logger = logging.getLogger(__name__)


class Menu:
    def main_menu(self):
        option = get_user_option(menu=main_menu, max_option=4)
        if option == "1":
            return self.main_menu()
        elif option == "2":
            result = RegisterView().register()
            if not result:
                print("Something get wrong, try again later")
        elif option == "3":
            role = LoginView().login()
            if role == "user":
                return self.user_menu()
            else:
                return self.admin_menu()

        elif option == "4":
            exit()

        return self.main_menu()

    def user_menu(self):
        option = get_user_option(menu=user_menu , max_option=6)

        if option == "1":
            PostsQueries().show()
        elif option == "2":
            if MessageView().show_all_users():
                option = get_user_option(message_menu, max_option=2)
                if option == "1":
                    MessageView().send_message()
            return self.user_menu()
        elif option == "3":
            PostsViews().productadd()
        elif option == "4":
            PostsViews().productupdate()
        elif option == "5":
            PostsViews().productdelete()
        elif option == "6":
            LogoutView().logout_all()
            return self.main_menu()
        return self.user_menu()

    def admin_menu(self):
        option = get_user_option(menu=admin_menu, max_option=4)

        if option == "1":
            AdminQueries().count_users()

        elif option == "2":
            AdminQueries().count_posts()

        elif option == "3":
            AdminQueries().get_users()

        elif option == "4":
            return self.main_menu()
        return self.admin_menu()


if __name__ == '__main__':
    execute_tables()
    LogoutView.logout_all_users()
    Menu().main_menu()
