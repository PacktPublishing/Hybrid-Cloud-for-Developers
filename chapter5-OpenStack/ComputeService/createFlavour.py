# Import the OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def create_flavor(conn):
    flavor_properties = {'name':'packtpub-flavor', 'disk':'1', 'ram':'2048', 'vcpus':'2'}
    conn.compute.create_flavor(**flavor_properties)

create_flavor(conn)
