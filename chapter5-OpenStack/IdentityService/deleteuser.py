#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")


def delete_user(conn):
    userid="dc985ff4f159490b95ea2c96a6b35368"
    conn.identity.delete_user(userid,ignore_missing=True)

delete_user(conn)
