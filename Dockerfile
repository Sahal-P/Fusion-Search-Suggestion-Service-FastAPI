FROM python:3

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN pip install pymongo bson

# RUN docker build -t my-fastapi-app .
# RUN docker run -d --name my-app -p 80:80 my-fastapi-app



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]