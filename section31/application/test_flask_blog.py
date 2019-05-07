import os
import flask_blog
import unittest
import tempfile
from flask_blog.scripts.db import InitDB

class TestFlaskBlog(unittest.TestCase):

    def setUp(self):
        self.db_fd, flask_blog.DATABASE = tempfile.mkstemp()
        self.app = flask_blog.app.test_client()
        InitDB().run()


    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flask_blog.DATABASE)


    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)


    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('john', 'due123')
        assert 'Login successful'.encode() in rv.data
        rv = self.logout()
        assert 'Logged Out'.encode() in rv.data
        rv = self.login('admin', 'default')
        assert 'User name is different'.encode() in rv.data
        rv = self.login('john', 'defaultx')
        assert 'Password is different'.encode() in rv.data

if __name__ == '__main__':
    unittest.main()