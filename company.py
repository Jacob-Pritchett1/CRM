from mysqlconnection import connectToMySQL

class Company:
  def __init__(self, data):
    self.id = data['id']
    self.company_nmae = data['company_name']
    self.phone_number = data['phone_number']
    self.point_of_contact = data['point_of_contact']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.user = None
  @classmethod
  def get_all_companies(cls):
    query = 'SELECT * FROM company;'
    results = connectToMySQL('crm_db').query_db(query)
    companies = []
    for company in results:
      companies.append(cls(company))
    return companies
