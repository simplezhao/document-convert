# command
TAG=1.2
IMAGE_NAME = document-convert
DOCKER_ID = simplezhao
ENV_FILE = env

.PHONY: help
help:
	@echo 'help'


.PHONY: build
build:
	@echo 'build image'
	docker build . -t $(IMAGE_NAME):$(TAG)

.PHONY: push
push:
	@echo 'push docker to docker hub'
	docker tag $(IMAGE_NAME):$(TAG) $(DOCKER_ID)/$(IMAGE_NAME):latest
	docker push $(DOCKER_ID)/$(IMAGE_NAME):latest

.PHONY: run
run:
	docker run --rm -it --name $(IMAGE_NAME) --env-file $(ENV_FILE) -p 5000:5000 $(IMAGE_NAME):$(TAG)
