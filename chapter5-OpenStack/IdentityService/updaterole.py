#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def update_role(conn):
    role_id = "672cd2f468544563ad6c3748bc1577c7"
    role_id = "672cd2f468544563ad6c3748bc1577c7"
    role_id = "bbeb6e60ea814fe481587a2b96ea749f"
    role_desc = {
                "description":"This is an updated test role",
                "isenabled" : False,
                "name":"packtpub"
    }
    conn.identity.update_role(role_id, **role_desc)

update_role(conn)

