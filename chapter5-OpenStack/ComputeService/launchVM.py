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


def create_vm(conn):
    server_name = "packt-pub-vm"              # The name to be given to the launched VM
    image_name = "cirros-0.3.5-x86_64-disk"   # The glance image name to be used
    flavor_name = "m1.small"                  # The flavor to be used
    network_name = "private"                  # The network to be used to connect to

    image = conn.compute.find_image(image_name)        # Locate the image 
    flavor = conn.compute.find_flavor(flavor_name)     # Locate the flavor 
    network = conn.network.find_network(network_name)  # Locate the network
    keypair = create_keypair(conn)                     # Create a keypair

    # Launch the virtual machine
    server = conn.compute.create_server(
        name=server_name, image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}], key_name=keypair.name)

    # Wait for the virtual machine to launch
    server = conn.compute.wait_for_server(server)

create_vm(conn)
