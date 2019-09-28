# SyncIP

This repository contains the code to synchronize the local public IP address with my host entries on GoDaddy.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The following applications need to be installed on the local computer in order to run the project locally:

| Application | Minimum Version |                                       Link |
| ----------- | :-------------: | -----------------------------------------: |
| Python      |     3.7.3 +     |  [Link](https://www.python.org/downloads/) |
| Docker      |    19.03.2 +    | [Link](https://www.docker.com/get-started) |

### Development

Once you installed all the required prerequisites, you can now proceed with the deployment of the development environment by completing the following steps:

1. Execute the below command to download the repository to the local machine:

    `git clone https://github.com/jfmainville/syncip.git`

2. Navigate to the directory:

    `cd syncip`

3. You can now run the following command to start the development environment:

    `docker-compose up --build`

4. When the development environment is no longer required, you can execute the below command to shutdown the environment:

    `docker-compose down`
