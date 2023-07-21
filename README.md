# Devops Task
### Create a command-line script, preferably in Bash, PHP, Node, or Python to perform the following tasks:

#### Check if docker and docker-compose is installed on the system. If not present, install the missing packages.
#### The script should be able to create a WordPress site using the latest WordPress Version. Please provide a way for the user to provide the site name as a command-line argument.
#### It must be a LEMP stack running inside containers (Docker) and a docker-compose file is a must.
#### Create a /etc/hosts entry for example.com pointing to localhost. Here we are assuming the user has provided example.com as the site name.
#### Prompt the user to open example.com in a browser if all goes well and the site is up and healthy.
#### Add another subcommand to enable/disable the site (stopping/starting the containers)
#### Add one more subcommand to delete the site (deleting containers and local files).

# Python Script

This script allows you to easily manage WordPress sites using Docker containers. It provides functionalities to create, enable, disable, and delete WordPress sites. Follow the instructions below to install and use the script effectively.

## Prerequisites

Before using this script, ensure you have the following prerequisites:

1. Docker: Make sure you have Docker installed on your system. You can download and install Docker from the official website: https://www.docker.com/get-started

2. Python: This script is written in Python, so ensure you have Python 3.x installed on your system.

## Installation

1. Clone the repository or download the script `wordpress_site_manager.py` to your local machine.

2. Open a terminal (command prompt on Windows) and navigate to the directory containing the script.

3. Install the required Python packages by running the following command:

```bash
pip install subprocess
pip install webbrowser

## Usage
The script accepts different subcommands to perform specific actions on WordPress sites. The available subcommands are:
```bash
create: Create a new WordPress site.

enable: Start the containers of an existing WordPress site.

disable: Stop the containers of an existing WordPress site.

delete: Delete an existing WordPress site.
```
To use the script, follow the syntax:

```bash
python wordpress_site_manager.py <subcommand> <site_name>

```
Replace <subcommand> with one of the supported subcommands and <site_name> with the desired name for your WordPress site

## Examples
### To create a new WordPress site with the name my_wordpress_site, run:
```bash
python wordpress_site_manager.py create my_wordpress_site
```
### To enable an existing WordPress site with the name my_wordpress_site, run:
```bash
python wordpress_site_manager.py enable my_wordpress_site
```
### To disable an existing WordPress site with the name my_wordpress_site, run:
```bash
python wordpress_site_manager.py disable my_wordpress_site
```

### To delete an existing WordPress site with the name my_wordpress_site, run:
```bash
python wordpress_site_manager.py delete my_wordpress_site
```

