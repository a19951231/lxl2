from api.test_project.test_django_restful import UserTest,GroupTest
import unittest

class Yl_jk(unittest.TestCase):
    def api_user(self):
        #这些没用的
        self.a=UserTest()
        self.a.test_1()
        self.a.test_001_no_auth2()
        self.a.test_002_add_user3()
        self.a.test_003_update_user4()
        self.a.test_004_delete_user5()
        self.a.test_005_get_user6()
    def api_groups(self):
        self.a=GroupTest()
        self.a.test_001_group_developer1()
        self.a.test_002_add_group2()
        self.a.test_003_update_group3()
        self.a.test_004_delete_group4()

if __name__ == '__main__':
    unittest.main()
