class UserViewModel:
    def __init__(self, data):
        self.userid = data.userid
        self.username = data.username
        self.phone_num = data.phone_num
        self.role = data.role
        self.gender = data.gender
        self.sign = data.sign
        self.avatar = data.avatar
        self.password = data._password
        self.birthday = data.birthday