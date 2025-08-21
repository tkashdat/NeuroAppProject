# my base image using conda environment
FROM continuumio/miniconda3

# set working directory within the container
WORKDIR /app

# copy environment file into container to install dependencies
COPY neuro_datascience_env.yml /app/environment.yml

#create conda environment using file in app
RUN conda env create -f  /app/environment.yml

# Make the environment active by default
RUN echo "source activate myenv" > ~/.bashrc
ENV PATH=/opt/conda/envs/myenv/bin:$PATH

# currently set up for flask app, will change later****
COPY app.py /app
COPY templates/index.html /app/templates/

#tell the port number the container should expose (currently set for flask)****
EXPOSE 5000

#run the application (will change later)****
CMD ["python", "/app/app.py"]