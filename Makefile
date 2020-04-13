# You can change these for your project
project=gmail
tag=ai
gcpProject=mchirico
port=3000

docker-build:
	docker build --no-cache -t gcr.io/$(gcpProject)/$(project):$(tag) -f Dockerfile .

push:
	docker push gcr.io/$(gcpProject)/$(project):$(tag)


run:
	docker run --rm -it  gcr.io/$(gcpProject)/$(project):$(tag)

test:
	docker run --rm  -p $(port):$(port)  gcr.io/$(gcpProject)/$(project):$(tag) pytest
