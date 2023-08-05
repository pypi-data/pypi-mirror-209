import os

project_id = os.environ.get('PROJECT_ID')
slack_login_url = os.environ.get('SLACK_LOGIN_URL')
background_jobs_topic = os.environ.get('BACKGROUND_JOBS_TOPIC')
background_jobs_subscriber = os.environ.get('BACKGROUND_JOBS_SUBSCRIBER')
mongo_connection_string = os.environ.get('MONGO_CONNECTION_STRING')
smtp_host = os.environ.get('SMTP_HOST')
smtp_login = os.environ.get('SMTP_LOGIN')
smtp_password = os.environ.get('SMTP_PASSWORD')
k8namespace = os.environ.get('K8_NAMESPACE')
k8config = os.environ.get('KUBE_CONFIG_DEFAULT_LOCATION')
backend_uri = os.environ.get('BACKEND_URI')
aggregator_topic = os.environ.get('AGGREGATOR_TOPIC')
google_app_credentials = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
portal_url = os.environ.get('PORTAL_URL')
push_gateway_url = os.environ.get('PUSH_GATEWAY_URL')
environment = os.environ.get('ENVIRONMENT')
write_analytics = os.environ.get("WRITE_ANALYTICS", "true").lower() == "true"
