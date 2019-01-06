import unittest
import json
from app.tests.base import BaseTestCase


def register_user(self):

    return  self.client.post(
            '/user/',
            data=json.dumps(dict(
                email='amrtest@test.com',
                username='amrtest',
                password='amrtest'
            )),
            content_type='application/json'
        )


def login_user(self):

    return self.client.post(
            '/auth/login',
            data=json.dumps(dict(
                email='amrtest@test.com',
                password='amrtest'
            )),
            content_type='application/json'
        )


class TestAuth(BaseTestCase):

    def test_registered_ulogin(self):

        with self.client:

            user_resp = register_user(self)

            resp_data = json.loads(user_resp.data.decode())

            self.assertTrue(resp_data['Authorization'])
            self.assertEqual(user_resp.status_code, 201)

            login_resp = login_user(self)

            resp_data = json.loads(login_resp.data.decode())

            self.assertTrue(resp_data['Authorization'])
            self.assertEqual(login_resp.status_code, 200)

            logout_resp = self.client.post(
                '/auth/logout',
                headers=dict(Authorization='Bearer ' + json.loads(login_resp.data.decode())['Authorization'])
            )

            data = json.loads(logout_resp.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertEqual(logout_resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()

