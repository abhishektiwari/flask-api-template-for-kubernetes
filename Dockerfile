FROM python:3.7-slim

# install netcat
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

ENV FLASK_APP entry.py
ENV FLASK_CONFIG development

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
COPY ./requirements-prod.txt /usr/src/app/requirements-prod.txt
RUN pip install -r requirements-prod.txt


# Copy files
COPY . /usr/src/app/
RUN chmod 755 entrypoint.sh



# run-time configuration
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]