FROM python:3.10.13-alpine

WORKDIR /app

COPY . /app/

RUN python3 -m pip install -r requirements.txt

ENV API_KEY="AIzaSyCUxMiitzSTQhal-znPdoa8DR6cNp6Xk_w"

RUN pip install flask

EXPOSE 80

CMD ["python", "app/server.py"]