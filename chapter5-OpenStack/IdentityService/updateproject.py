#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def update_project(conn):
    project_id = "8962c72f926d4d95b03a0d051d6a606f"
    project_desc = {
                "description":"This project is for packtpub authors",
                "isenabled" : True,
                "name":"packtpub_authors"
    }
    conn.identity.update_project(project_id, **project_desc)

update_project(conn)
