# Docker ROS Base Image

This is a Docker Image.

**Requirements :**
-Docker Desktop(for Windows or Mac)
-Docker Engine (for Linux)

## Getting basic auth credentials

In case of getting the error "no basic auth credentials"

- Go to https://github.com/settings/tokens

- Generate new token

- Name it

- Check write:packages

- Generate token

- Save it on your computer !

Now you need to login to the repo with your token, open a terminal :

    docker login docker.pkg.github.com -u <UserNameOfYourGitHub>

Password is your freshly generated token. You can now start to pull the image


## Getting Started to work !

First clone this image :
    
    sudo docker pull docker.pkg.github.com/yncreahdf-robotics/flotte_m2_2020-2021-superviseur/xenialrosmysql:latest

Then build the image using Docker

    docker build --tag ros:mykinetic .
(Dot is important !)

Next go to your wanted directory and pull your repo from your branche to one directory.

    git pull <yourrepo>

Check if you have build your network:

    docker network ls

If you have a network called ros skip the next step if not do:

    docker network create ros

Then check with:

    docker network ls

Move to your the directory that contain your "workspace" folder

    cd <path>

Finally run your image

    sudo docker run --rm -it --net ros -e ROS_MASTER_URI=http://roscore:11311 -e WORKSPACE_NAME=workspace -v $(pwd)/workspace:/home/workspace -w /home/workspace docker.pkg.github.com/yncreahdf-robotics/flotte_m2_2020-2021-superviseur/xenialrosmysql:latest

You are now in your docker container running your programs and nodes.
You can modify the files directly from the shared folder "workspace" that you have pulled from github and use docker as your developpement environnement.

## Save your work
First commit your work:

    git commit

Push your local repository containing the "workspace" folder to your branch

    git push <your repo>





sudo docker login https://docker.pkg.github.com -u USERNAME -p PASSWORD


Now you are ready for next section.

