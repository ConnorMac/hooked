FROM python:3.6-alpine

COPY hooked.py hooked.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV FLASK_APP=hooked.py
EXPOSE 5001
CMD ["python", "hooked.py", "--host=0.0.0.0"]
