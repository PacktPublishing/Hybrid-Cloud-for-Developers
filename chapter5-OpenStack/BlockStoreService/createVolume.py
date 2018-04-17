#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")


def create_volume(conn):
    volume_properties = {'size':'2', 'name':'packtpub-volume'}
    volume = conn.block_store.create_volume(**volume_properties)

create_volume(conn)
