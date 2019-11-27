import messages
from user import User


def read_file_data(filename: str):
    file = open(filename, 'r')
    return file.readlines()


def transform_file_data(file_data: list):
    matrix_users = [list(user.split(',')[:-1]) for user in file_data]
    return [User(user) for user in matrix_users]


def find_user(username: str):
    user_list = transform_file_data(read_file_data('users.txt'))
    return [user for user in user_list if user.username == username][0]


def check_password(user: User, password: str):
    return user.password == password


def show_user_info(user: User):
    print(user.to_collection())


def login():
    username = input(messages.INPUT_USERNAME)
    password = input(messages.INPUT_PASSWORD)

    user = find_user(username)

    if not user:
        print(messages.BAD_USERNAME)
        return None

    if check_password(user, password):
        show_user_info(user)
        return user
    else:
        print(messages.BAD_PASSWORD)
        return None


if __name__ == '__main__':
    logged_user = None

    while not logged_user:
        logged_user = login()
