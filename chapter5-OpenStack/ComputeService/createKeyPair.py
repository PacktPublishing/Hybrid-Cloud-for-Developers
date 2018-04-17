# Import the OpenStack connection class from the SDK
from openstack import connection
import os

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")


def create_keypair(conn): 
    keypair_name = "packtpub-keypair"    # The name of the keypair to be created
    private_key_file = "private.key"     # The name of the file that stores the private key
    keypair = conn.compute.find_keypair(keypair_name)

    if not keypair:
        keypair = conn.compute.create_keypair(name=keypair_name)  # Create a keypair

        with open(private_key_file, 'w') as filehandle:    
            filehandle.write("%s" % keypair.private_key)     # Write the private key to a file 
            os.chmod(private_key_file, 0o400)                # Change the permission of the key file

    return keypair

print create_keypair(conn)
