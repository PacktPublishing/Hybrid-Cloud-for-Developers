#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def find_user(conn):
    username="packtpub"
    user = conn.identity.find_user(username,ignore_missing=True)
    print (user)

find_user(conn)
