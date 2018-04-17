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
    volume_properties = {'size':'2', 'name':'packtpub-volume-2'}
    volume = conn.block_store.create_volume(**volume_properties)

def delete_volume(conn):
    volume_id = "3b064701-aaa7-418a-9df7-cad52bd549ee"
    conn.block_store.delete_volume(volume_id)

def create_snapshot(conn):
    snapshot_properties = {'volume_id':'3b064701-aaa7-418a-9df7-cad52bd549ee'}
    snapshot = conn.block_store.create_snapshot(**snapshot_properties)


def delete_snapshot(conn):
    snapshot_id = "91ac5916-0baa-469e-ac4e-e37b2a3880dc"
    conn.block_store.delete_snapshot(snapshot_id)


#create_snapshot(conn)
#delete_snapshot(conn)
#delete_volume(conn)
create_volume(conn)
