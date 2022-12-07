import unittest

# Import Flask's test client
#from flask.testing import FlaskClient


from app import home
from app import login
from app import logout
from app import register
from app import registernew
from app import registernew1
from app import passenger_ride_details


# This code implements the unit test functionality


class app(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testhome(self): 
        self.assertEqual(home(render_template),'true','home page is tested successfully')

    def testlogin(self): 
        self.assertEqual(login(render_template),'true','login page is tested successfully')

    def testlogout(self):
        self.assertEqual(logout(redirect),'true','logout page is tested successfully')
        
    def testregister(self): 
        self.assertEqual(register(render_template),'true','register page is tested successfully')

    def testregisternew(self):
        self.assertEqual(registernew(render_template),'true','registernew page is tested successfully')

    def testregisternew1(self):
        self.assertEqual(registernew1(render_template),'true','registernew1 page is tested successfully')
    
    def testpassenger_ride_details(self):
        self.assertEqual(passenger_ride_details(render_template),'true','passenger_ride_details page is tested successfully')

    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
