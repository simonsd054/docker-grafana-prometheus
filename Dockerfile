#Deriving the latest base image
FROM python:latest


#Labels as key value pair
LABEL Maintainer="simon"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /home

#to COPY the remote file at working directory in container
COPY project_spend_cost.py ./
COPY project_cost_breakdown.py ./
COPY run.sh ./
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
RUN chmod +x run.sh
# RUN /bin/bash -c './run.sh'
CMD [ "/bin/bash", "./run.sh" ]