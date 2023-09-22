from mysqlconnection import connectToMySQL

class User: 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.role = data['role']
        self.email = data['email']
        self.username = data['username']
        self.created_at = data['created-at']
        self.updated_at = data['updated-at']
        self.company = None
        self.note = None
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM user;"
        results = connectToMySQL('crm_db').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
