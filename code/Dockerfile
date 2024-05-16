# ubuntu_python_fastapi.dockerfile
# Step 1. Download the ubuntu image
FROM ubuntu:latest

# Step 2. Update apt 
RUN apt update

# Step 3. Install python3 and python3-pip using apt
RUN apt install -y python3 python3-pip

# Step 4. Install fastapi and uvicorn with pip
# Uvicorn is a web server. It handles network communication - receiving requests from client applications such as users' 
# browsers and sending responses to them

RUN python3 -m pip install fastapi uvicorn

# Step 5: Copying python code inside the image
COPY ./hello_fastapi_requests.py /

# Step : Start the uvicorn command (uvicorn --host=0.0.0.0 --port=8000 hello_fastapi_docker:app)
# Here, we break down different parts of the uvicorn command (separated by spaces) and put them in a list 
CMD ["uvicorn", "--host=0.0.0.0", "--port=8080", "hello_fastapi_requests:company_app"]
