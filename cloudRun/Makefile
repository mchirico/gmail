
build:
	gcloud builds submit --tag gcr.io/septapig/gmail --project septapig --timeout 35m23s
	gcloud run deploy gmail  --image gcr.io/septapig/gmail --platform managed \
              --platform managed --allow-unauthenticated --project septapig \
              --region us-east1 --port 8080 --max-instances 2  --memory 128Mi
