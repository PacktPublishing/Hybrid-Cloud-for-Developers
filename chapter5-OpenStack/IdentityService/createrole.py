#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")


def create_role(conn):
    role_desc = {
                "description":"This is a test role",
                "isenabled" : True,
                "name":"packtpub"
    }
    conn.identity.create_role(**role_desc)

create_role(conn)

