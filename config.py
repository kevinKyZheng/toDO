import os
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
basedir = os.path.abspath(os.path.dirname(__file__))
# 注意此处是URI 不要写错 写成URL
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')