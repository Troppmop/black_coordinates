k8s branch
# docker compose instructions (locally)
(must clarify env vars issue)

# minikube instructions (locally)
docker desktop must be opened if using the minikube docker image
minikube must be installed
kubectl must be installed 
both must be on path
to deploy locally:

minikube start
cd k8s
kubectl apply -f .
minikube service service-a-service 



# openshift instructions (remotely hosted)
openshift must be installed and on path
user must have a redhat openshift account environement
login using your token login command
to deploy to remote host:
goto k8s folder:
cd k8s
oc apply -f .
oc expose svc service-a-service

to view the deployment:
oc get route

check under host/port
copy and paste to browser
check to see if you need to change from https to http
add /docs to the end of the url to visit the fastapi docs
test the routes 