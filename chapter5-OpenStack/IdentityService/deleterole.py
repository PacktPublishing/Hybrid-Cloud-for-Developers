#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")


def delete_role(conn):
    role_id = "ce5156690f4c48bda5b5b9041325e493"
    role_id = "672cd2f468544563ad6c3748bc1577c7"
    conn.identity.delete_role(role_id, ignore_missing=True)

delete_role(conn)
