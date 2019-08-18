REPO=app
TIMESTAMP=tmp-$(shell date +%s )
NSPACE=development
DFILE=kubernetes/flask-deployment.yml
SFILE=kubernetes/flask-service.yml
IFILE=kubernetes/minikube-flask-ingress.yml
IFILE=kubernetes/minikube-flask-ingress.yml
VERSION=v1

.PHONY: mstart
mstart:
	minikube start --kubernetes-version v1.15.0
	kubectx minikube
	OUTPUT="$(minikube ip)"
	echo "🚀 Add following your /etc/hosts:${OUTPUT} mymachine.com"

.PHONY: mstatus
mstatus:
	kubectx
	kubens
	minikube status
	minikube ip

.PHONY: mstop
mstop:
	minikube stop

.PHONY: mdashboard
mdashboard:
	minikube dashboard

.PHONY: mclean
mclean:
	minikube stop
	minikube delete

.PHONY: update
update:  
	@eval $$(minikube docker-env) ;\
	docker image build -t $(REPO):$(TIMESTAMP) -f Dockerfile .
	kubectl set image -n $(NSPACE) deployment/$(REPO) *=$(REPO):$(TIMESTAMP)

.PHONY: delete
delete:
	kubectl delete -n $(NSPACE) deployment,service $(REPO)

.PHONY: create
create:
	@eval $$(minikube docker-env) ;\
	docker image build -t $(REPO):v1 -f Dockerfile .
	kubectl create -f $(DFILE)
	kubectl create -f $(SFILE)

.PHONY: ingress
ingress:
	kubectl create -f $(IFILE)

.PHONY: push
push: build
	docker tag $(REPO):$(VERSION) $(REPO):latest
	docker push $(REPO):$(VERSION)
	docker push $(REPO):latest

build:
	@eval $$(minikube docker-env -u);\
	docker image build -t $(REPO):$(VERSION) -f Dockerfile .
