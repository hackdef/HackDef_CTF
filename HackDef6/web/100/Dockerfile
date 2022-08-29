FROM python:3.7

ARG project_dir=/projects/
ADD src/requirements.txt $project_dir
ADD src/flag $project_dir
WORKDIR $project_dir

RUN pip install -r requirements.txt
