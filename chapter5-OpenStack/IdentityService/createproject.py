#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def create_project(conn):
    project_desc = {
                "description":"This project is for packtpub readers",
                "isenabled" : True,
                "name":"packtpub_readers"
    }
    project = conn.identity.create_project(**project_desc)

create_project(conn)
