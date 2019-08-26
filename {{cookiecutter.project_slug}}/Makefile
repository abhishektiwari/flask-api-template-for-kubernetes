AIMG={{ cookiecutter.project_slug }}
REPO={{ cookiecutter.docker_repo_prefix }}/{{ cookiecutter.project_slug }}
TIMESTAMP=tmp-$(shell date +%s )
NSPACE=development
DAPP=kubernetes/base-app/
DPGS=kubernetes/base-pgs/

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

.PHONY: mdash
mdashboard:
	minikube dashboard

.PHONY: mdelete
mdelete:
	minikube stop
	minikube delete

.PHONY: dupdate
dupdate:  
	@eval $$(minikube docker-env) ;\
	docker image build -t $(AIMG):$(TIMESTAMP) -f Dockerfile .
	kubectl set image -n $(NSPACE) deployment/$(AIMG) *=$(AIMG):$(TIMESTAMP)

.PHONY: ddeploy
ddeploy:
	@eval $$(minikube docker-env) ;\
	docker image build -t $(AIMG):v1 -f Dockerfile .
	kubectl apply -k $(DAPP)

.PHONY: ddspace
ddspa:
	kubectl delete namespace development

.PHONY: dcspace
dcspace:
	kubectl create namespace development
	kubens development

.PHONY: dpgs
dpgs:
	kubectl apply -k $(DPGS)

.PHONY: push
push:
	docker tag $(REPO):$(VERSION) $(AIMG):latest
	docker push $(REPO):$(VERSION)
	docker push $(REPO):latest

.PHONY: build
build:
	@eval $$(minikube docker-env -u);\
	docker image build -t $(REPO):$(VERSION) -f Dockerfile .
