# Import necessary libraries
import os
import sys
import subprocess
import platform
import webbrowser
import winreg

# Check if Docker and docker-compose are installed, and install them if necessary.
def check_docker():
    try:
        # Try to run Docker and docker-compose commands to check if they are installed.
        subprocess.run(['docker', '--version'], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['docker-compose', '--version'], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Docker and docker-compose are already installed.")
    except subprocess.CalledProcessError:
        # If Docker and/or docker-compose are not installed, install them (Linux-based systems).
        print("Docker and/or docker-compose are not installed. Installing...")
        subprocess.run(['sudo', 'apt', 'update'])
        subprocess.run(['sudo', 'apt', 'install', '-y',
                       'docker.io', 'docker-compose'])
        print("Docker and docker-compose installed successfully.")

# Create a new WordPress site with a given site name.
def create_wordpress_site(site_name):
    # Content for the docker-compose.yml file specifying the WordPress and MySQL services.
    # This file defines how the WordPress site will be set up using Docker containers.
    docker_compose_content = f'''
    # ... (content of the docker-compose.yml file) ...
    '''

    # Save the docker-compose.yml file in the current working directory.
    docker_compose_path = os.path.join(os.getcwd(), 'docker-compose.yml')
    with open(docker_compose_path, 'w') as docker_compose_file:
        docker_compose_file.write(docker_compose_content)

    # Start the Docker containers defined in the docker-compose.yml file.
    subprocess.run(['docker-compose', 'up', '-d'])
    print("WordPress site is up and running.")

# Add an entry in the hosts file to make the site accessible at http://site_name/.
def add_hosts_entry(site_name):
    # For Windows systems, try to modify the hosts file to add the new site entry.
    if platform.system() == "Windows":
        try:
            # Open the Windows Registry to access the hosts file configuration.
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", 0,
                                winreg.KEY_SET_VALUE) as key:
                # Get the existing hosts file content.
                existing_hosts = winreg.QueryValueEx(key, "DataBasePath")[0]

            # Append the new site entry to the existing hosts file content.
            if not site_name in existing_hosts:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", 0,
                                    winreg.KEY_SET_VALUE) as key:
                    new_hosts = existing_hosts + f"\n127.0.0.1 {site_name}"
                    # Update the hosts file with the new content.
                    winreg.SetValueEx(key, "DataBasePath", 0,
                                      winreg.REG_SZ, new_hosts)
        except Exception as e:
            print("Unable to update hosts file:", e)

# Enable the WordPress site by starting the Docker containers.
def enable_site(site_name):
    subprocess.run(['docker-compose', 'start'])
    print(f"WordPress site '{site_name}' is enabled.")

# Disable the WordPress site by stopping the Docker containers.
def disable_site(site_name):
    subprocess.run(['docker-compose', 'stop'])
    print(f"WordPress site '{site_name}' is disabled.")

# Delete the WordPress site by stopping containers and removing the docker-compose.yml file.
def delete_site(site_name):
    subprocess.run(['docker-compose', 'down', '-v'])
    docker_compose_path = os.path.join(os.getcwd(), 'docker-compose.yml')
    # Remove the docker-compose.yml file after stopping the containers.
    os.remove(docker_compose_path)
    print(f"WordPress site '{site_name}' is deleted.")

# Main function to handle different subcommands and execute the corresponding actions.
def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <subcommand> <site_name>")
        sys.exit(1)

    subcommand = sys.argv[1].lower()
    site_name = sys.argv[2]

    # Check if Docker and docker-compose are installed or install them if necessary.
    check_docker()

    if subcommand == 'create':
        # Create a new WordPress site and add it to the hosts file.
        create_wordpress_site(site_name)
        add_hosts_entry(site_name)
        print(f"WordPress site '{site_name}' is ready at http://{site_name}/")
        open_browser = input("Do you want to open it in the browser? (y/n): ")
        if open_browser.lower() == 'y':
            webbrowser.open(f'http://{site_name}/')

    elif subcommand == 'enable':
        # Enable an existing WordPress site by starting the containers.
        enable_site(site_name)

    elif subcommand == 'disable':
        # Disable an existing WordPress site by stopping the containers.
        disable_site(site_name)

    elif subcommand == 'delete':
        # Delete an existing WordPress site, stopping containers, and removing files.
        delete_site(site_name)

    else:
        # If an invalid subcommand is provided, print the supported subcommands.
        print("Invalid subcommand. Supported subcommands: create, enable, disable, delete.")
        sys.exit(1)

# Execute the main function when the script is run.
if __name__ == "__main__":
    main()
