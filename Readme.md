# Flask API template for Kubernetes
At Oats, we use Flask extensively. This is one of the standard templates we use internally for building our Python and Flask powered APIs running on top of Kubernetes.

# Clone template

```
git clone https://github.com/tryoats/flask-api-template-for-kubernetes my-project
```


# Setting up development environment on Mac

First ensure you have the latest version of [VirtualBox](https://www.virtualbox.org/wiki/Downloads), [Docker Desktop For Mac](https://www.docker.com/products/docker-desktop, and [Homebrew](https://brew.sh/) installed.

Install Python, Kubectl, Minikube, and Postgres. 

```
brew install python
brew install kubernetes-cli
brew cask install minikube
brew install postgresql
brew install kubectx
```

or upgrade,

```
brew upgrade python
brew upgrade kubernetes-cli
brew cask upgrade minikube
brew upgrade postgresql
brew upgrade kubectx
```

Start Postgresql service, create a DB for local user, and connect.
```
brew services start postgresql
createdb -h localhost
psql -h localhost
```

Create a database which will be used for 
```
CREATE DATABASE yourdbname;
CREATE USER youruser WITH ENCRYPTED PASSWORD 'yourpass';
GRANT ALL PRIVILEGES ON DATABASE yourdbname TO youruser;
```

Database browser,

https://www.postgresql.org/ftp/pgadmin/pgadmin4/v4.11/macos/

# Running you code locally

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
export FLASK_APP=entry.py
export POSTGRES_USER=youruser
export POSTGRES_DB_NAME=yourdbname
export POSTGRES_PASSWORD=yourpass
export POSTGRES_HOST=localhost
export FLASK_CONFIG=development
export FLASK_ENV=development
```

After this following commands can be run,

```
flask run
flask db init
flask db migrate
flask db upgrade
```

Dangerous commands try only in development,

```
flask recreate_db
flask seed_db
```

# Minikube

```
cd project
minikube addons enable ingress
kubectl apply -f ./kubernetes/secret.yml
kubectl create -f ./kubernetes/flask-deployment.yml
kubectl create -f ./kubernetes/flask-service.yml
kubectl get pods
kubectl apply -f ./kubernetes/minikube-ingress.yml
```

Add entry to /etc/hosts file:

```
<MINIKUBE_IP> hello.world
```

# Kubernetes

```
kubectl apply -f ./kubernetes/secret.yml
kubectl create -f ./kubernetes/flask-deployment.yml
kubectl create -f ./kubernetes/flask-service.yml
kubectl get pods
kubectl apply -f ./kubernetes/gke-ingress.yml
```


# Refrence

https://mherman.org/presentations/flask-kubernetes/#63
https://testdriven.io/blog/running-flask-on-kubernetes/
https://github.com/testdrivenio/flask-vue-kubernetes
https://flask-migrate.readthedocs.io/en/latest/
https://blog.miguelgrinberg.com/post/migrating-from-flask-script-to-the-new-flask-cli
https://github.com/miguelgrinberg/flasky/blob/master/flasky.py
https://blog.theodo.com/2017/03/developping-a-flask-web-app-with-a-postresql-database-making-all-the-possible-errors/
