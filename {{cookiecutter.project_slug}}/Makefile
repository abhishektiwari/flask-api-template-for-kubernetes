REPO={{ cookiecutter.project_slug }}
ING={{ cookiecutter.project_slug }}-ingress
TIMESTAMP=tmp-$(shell date +%s )
NSPACE=development
DFILE=kubernetes/dev/deployment.yml
SFILE=kubernetes/dev/service.yml
IFILE=kubernetes/dev/ingress.yml
CFILE=kubernetes/dev/secret.yml
PVFPG=kubernetes/dev/persistent-volume.yml
PGPVC=kubernetes/dev/persistent-volume-claim.yml
PGDPL=kubernetes/dev/postgres-deployment.yml
PGSVC=kubernetes/dev/postgres-service.yml
VERSION=v1

.PHONY: mstart
mstart:
	minikube start --kubernetes-version v1.15.0 --disk-size='40000mb'
	kubectx minikube
	kubectl cluster-info
	minikube ip
	kubectl create namespace development
	kubens development

.PHONY: mstatus
mstatus:
	kubectx
	kubens
	kubectl cluster-info
	minikube status
	minikube ip

.PHONY: mstop
mstop:
	minikube stop

.PHONY: mdashboard
mdashboard:
	minikube dashboard

.PHONY: mdelete
mdelete:
	minikube stop
	minikube delete

.PHONY: update
update:  
	@eval $$(minikube docker-env) ;\
	docker image build -t $(REPO):$(TIMESTAMP) -f Dockerfile .
	kubectl set image -n $(NSPACE) deployment/$(REPO) *=$(REPO):$(TIMESTAMP)

.PHONY: apps
apps:
	@eval $$(minikube docker-env) ;\
	docker image build -t $(REPO):v1 -f Dockerfile .
	kubectl create -f $(DFILE)
	kubectl create -f $(SFILE)

.PHONY: delete
delete:
	kubectl delete namespace development

.PHONY: namespace
namespace:
	kubectl create namespace development
	kubens development

.PHONY: postgres
postgres:
	echo "Creating the volume..."
	kubectl apply -f $(PVFPG)
	kubectl apply -f $(PGPVC)
	echo "Creating the database credentials..."
	kubectl apply -f $(CFILE)
	echo "Creating the postgres deployment and service..."
	kubectl create -f $(PGDPL)
	kubectl create -f $(PGSVC)

.PHONY: ingress
ingress:
	kubectl create -f $(IFILE)

.PHONY: push
push: build
	docker tag $(REPO):$(VERSION) $(REPO):latest
	docker push $(REPO):$(VERSION)
	docker push $(REPO):latest

.PHONY: build
build:
	@eval $$(minikube docker-env -u);\
	docker image build -t $(REPO):$(VERSION) -f Dockerfile .
