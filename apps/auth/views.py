from core.database import execute_query


class RegisterView:
    def send_code(self):
        pass

    def check_code(self):
        pass
    @staticmethod
    def register():
        full_name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        password = input("Enter password: ")
        query = """
            INSERT INTO users (full_name,phone_number,password,is_active) 
            VALUES (%s,%s,%s,%s);
        """
        params = (full_name,phone_number,password,True)

        execute_query(query= query,params=params)
        print("Registred")


class LoginView:
    def login(self):
        pass


class Logout:
    def logout(self):
        pass