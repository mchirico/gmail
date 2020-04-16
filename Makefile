
build:
	docker build --no-cache -t gcr.io/septapig/gmail -f Dockerfile .
	#gcloud builds submit --tag gcr.io/septapig/gmail --project septapig --timeout 35m23s

run:
	docker run -p 8080:8080 --env PORT=8080  --rm -it gcr.io/septapig/gmail

push:
	docker push gcr.io/septapig/gmail

pull:
	docker pull gcr.io/septapig/gmail


deploy:
	gcloud builds submit --tag gcr.io/septapig/gmail --project septapig --timeout 35m23s
	gcloud run deploy gmail  --image gcr.io/septapig/gmail --platform managed \
              --platform managed --allow-unauthenticated --project septapig \
              --region us-east1 --port 8080 --max-instances 2  --memory 128Mi
