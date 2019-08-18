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
Create virtualenv,
```
python3 -m venv venv
```

```
source venv/bin/activate
pip install -r requirements-dev.txt
```

```
export FLASK_APP=entry.py
export POSTGRES_USER=youruser
export POSTGRES_DB_NAME=yourdbname
export POSTGRES_PASSWORD=yourpass
export POSTGRES_HOST=host.docker.internal
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

⚠️ Comment out the `migrations/` pattern on the top of `.gitignore` file

⚠️ Dangerous custom commands try only in development,

```
flask recreate_db
flask seed_db
```

# Minikube

```
make mstart
```

Add entry to `/etc/hosts` file:

```
<MINIKUBE_IP> mymachine.com
```

Also add following into your local `/etc/hosts` file,

```
127.0.0.1 host.docker.internal
127.0.0.1 kubernetes.docker.internal
```

# Kubernetes

```

```

# Postgress running on host

Change connecition to accept from anywhere i.e. `listen_addresses = '*'`,

```
nano /usr/local/var/postgres/postgresql.conf
brew services restart postgresql
```

