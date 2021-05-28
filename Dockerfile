FROM python:3.9.5-slim-buster
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "gunicorn", "chatbot:app", "--bind", "0.0.0.0:5000" ]