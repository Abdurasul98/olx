import logging

from apps.auth.views import RegisterView, LogoutView, LoginView
from apps.posts.queries import PostsQueries
from apps.posts.views import PostsViews
from core.utils import main_menu, get_user_option, execute_tables, user_menu

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
            user = LoginView().login()
            if user:
                return self.user_menu()
            print("Invalid phone number or password")
        elif option == "4":
            exit()

        return self.main_menu()

    def user_menu(self):
        option = get_user_option(menu=user_menu , max_option=4)

        if option == "1":
            PostsQueries().show()
        elif option == "2":
            PostsViews().productadd()
        elif option == "3":
            PostsViews().productupdate()
        elif option == "4":
            PostsViews().productdelete()
        return self.user_menu()

    def admin_menu(self):
        pass


if __name__ == '__main__':
    execute_tables()
    LogoutView.logout_all_users()
    Menu().main_menu()
