#!/usr/bin/env bash
if [ ! -z ${DEPLOY_PROD} ] && $DEPLOY_PROD; then
    echo "Deploy is not local, is prod environments"
    gunicorn -c setup.py oficinadocker:app     
else
    echo "Environment not defined or is False";
    export FLASK_APP=oficinadocker
    flask run --host=0.0.0.0 
fi