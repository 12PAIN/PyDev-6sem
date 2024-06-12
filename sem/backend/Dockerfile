FROM python:3.10 as base_python
ENV PYTHONUNBUFFERED=1
ENV DOCKER_BUILDKIT=1
WORKDIR /home

FROM base_python as libraries_installed
RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx
COPY requirements_docker.txt .
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements_docker.txt
RUN pip install -r requirements_docker.txt

FROM libraries_installed as app
RUN rm -rf /var/lib/apt/lists/*
COPY * .
EXPOSE 8000
CMD ["alembic",  "upgrade",  "head"]
CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]