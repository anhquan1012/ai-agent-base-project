FROM python:3.12-slim

WORKDIR /server

COPY . .

RUN pip install .

CMD ["fastapi", "run", "server.py"]
