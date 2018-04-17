#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def update_user(conn):
    userid="3fcde77916894498a1d8753d2bafd8ee"
    userid="a322c1b4a2e64ab887e8e4371edc8b59"
    user_parameters = {
                "default_project_id":"demo",
                "email":"manoj.hirway@packtpub.com",
                "is_enabled":True,
                "name":"packtpub",
                "pasword":"new_password",
    }

    conn.identity.update_user(userid,**user_parameters)

update_user(conn)
