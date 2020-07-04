gunicorn  main:app -k uvicorn.workers.UvicornWorker -b :10240 --daemon 
