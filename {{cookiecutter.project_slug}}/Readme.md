# {{ cookiecutter.project_name }}

# Setting up development environment on Mac

First ensure you have the latest version of [VirtualBox](https://www.virtualbox.org/wiki/Downloads), [Docker Desktop For Mac](https://www.docker.com/products/docker-desktop), and [Homebrew](https://brew.sh/) installed.

Install Python, Kubectl, Minikube, and Postgres. 

```
brew install python
brew install kubernetes-cli
brew cask install minikube
brew install postgresql
brew install kubectx
brew install kustomize
```

or upgrade,

```
brew upgrade python
brew upgrade kubernetes-cli
brew cask upgrade minikube
brew upgrade postgresql
brew upgrade kubectx
brew upgrade kustomize
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

# Running your app and Postgres in local host
Create virtualenv,

```
python3 -m venv venv
```

Then activate virtualenv and install requirements,

```
source venv/bin/activate
pip install -r requirements-dev.txt
```

Set environment variables,
```
export FLASK_APP=entry.py
export POSTGRES_USER=youruser
export POSTGRES_DB_NAME=yourdbname
export POSTGRES_PASSWORD=yourpass
export POSTGRES_HOST=localhost
export FLASK_CONFIG=development
export FLASK_ENV=development
```

After this following commands can be run app,
```
python -m flask db init
python -m flask db migrate
python -m flask db upgrade
python -m flask run
```

⚠️ Comment out the `migrations/` pattern on the top of `.gitignore` file

⚠️ Dangerous custom commands try only in development,

```
flask recreate_db
flask seed_db
```

# Running your app and Postgres in Minikube

Start minikube,

```
make mstart
```

Add entry to `/etc/hosts` file:

```
<MINIKUBE_IP> {{ cookiecutter.dev_domain }}
```

Then create Postgress and Apps,

```
make postgres
make apps
```

Generate seed for database if required

```
kubectl get pods
kubectl exec app-XXXX flask seed_db
```

Recreate database if required

```
kubectl exec app-XXXX flask recreate_db
```

Rollout app update

```
make update
```

See logs for a pod,

```
kubectl get pods
kubectl logs -f app-XXXX
```

# Running your app and Postgres in Kubernetes cluster

```
TBA
```

# Postgress running on local host

Change conf if required and restart

```
nano /usr/local/var/postgres/postgresql.conf
brew services restart postgresql
```


Activate UUID extension,

```
psql -d yourdbname
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION pgcrypto
\df
DROP EXTENSION "uuid-ossp";
CREATE EXTENSION "uuid-ossp";
```

```
SELECT * FROM pg_available_extensions;
```