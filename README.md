# 32health


# Instructions to Run the API
cd processor
docker build -f DockerFile . -t 32health-backend-test
docker run -it -p 8000:8000 32health-backend-test
