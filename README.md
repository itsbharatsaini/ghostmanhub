# ghostmanhub
Your ML model can always use a bump inaccuracy. It never hurts and in most practical cases you actually need it! But as always, getting what you want is easier said than done.

Most people will go with the default advice: get more data…. But what if you can’t..?

Most of the time we need to change the model several times to find the best accuracy model manually. You need to do this automatically by integrating Jenkins, Docker, and ML. This utilizes a lot of time and man work for making a machine learning or deep learning model.

Steps to be followed
1. Create a Docker image
In that image Python3 and Keras or NumPy installed using Dockerfile.

Create a file with filename "Dockerfile"








Add alt text
No alt text provided for this image
To build that docker file use this command:

$ docker build -t <image_name:version> <docker_file_path>
In case you want to use a pre-created image than, Here it is https://hub.docker.com/u/ghostmanhub or you can pull directly by:

$ docker pull ghostmanhub/mlops:latest


2. Create Git repo
Git Automation by creating a post-commit file in .git/hooks/ folder and put the following code inside it.

#!/bin/bash

git push -u origin master
Make a git repo..!!

$ mkdir ghostmanhub
$ cd ghostmanhub
$ git init

Create a main.py python file.








Add alt text
No alt text provided for this image







Add alt text
No alt text provided for this image
Create a main_tweak.py python file.








Add alt text
No alt text provided for this image







Add alt text
No alt text provided for this image
The above codes will save the model in the dir with file extension ''.model'' and accuracy in the ''result.txt" file.

GitHub repository link: https://github.com/itsbharatsaini/ghostmanhub

2. Create Jenkins jobs
Create a job chain of job1, job2, job3, job4, and job5 using the build pipeline plugin in Jenkins.








Add alt text
No alt text provided for this image
Job1: Pull the Github repo automatically when some developers push the repo to Github.







Add alt text
No alt text provided for this image







Add alt text
No alt text provided for this image


Job2: By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the software required for the CNN processing).







Add alt text
No alt text provided for this image







Add alt text
No alt text provided for this image







Add alt text
No alt text provided for this image


Job3: Train your model and predict accuracy or metrics.







Add alt text
No alt text provided for this image







Add alt text
No alt text provided for this image
Job4: if metrics accuracy is less than 80%, then tweak the machine learning model architecture.







Add alt text
No alt text provided for this image







Add alt text
XXXXXXXXXXXXXXXXXXXXXX
Job5: Retrain the model or notify that the best model is being created.







Add alt text
No alt text provided for this image







Add alt text
No alt text provided for this image
Job6: for the monitor if the container where the app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left.







Add alt text
No alt text provided for this image
