#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def create_user(conn):
    user_parameters = {
                "default_project_id":"demo",
                "email":"manoj.hirway@gmail.com",
                "is_enabled":True,
                "name":"packtpub1",
                "pasword":"secret",
    }

    conn.identity.create_user(**user_parameters)

create_user(conn)
