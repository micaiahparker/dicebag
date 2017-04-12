FROM python:3.6
ADD . /dicebag
WORKDIR /dicebag
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
