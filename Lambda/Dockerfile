FROM public.ecr.aws/lambda/python:3.11

# Copy folder contents (.) to Lambda root folder
COPY . ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]

# FROM ubuntu:latest
#
# # apt-get `-y` flag for default 'y' response to continue installation
# RUN apt-get update && apt-get install -y python3 python3-pip
#
# COPY . .
# RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install flask
#
# WORKDIR /sentimental
# ENV FLASK_APP=main.py
# EXPOSE 8080
# CMD ["flask", "run", "--host", "0.0.0.0"]
#
# # build Docker image: `docker build -t snelbestel .` # -t assigns tag (name)
# # run Docker image on port 8080: `docker run -p 8080:8080 sentimental` # -p use manually-set ports, map to exposed container's ports