FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
RUN mkdir Templates
COPY app3.py /app.py
COPY Templates/*  /Templates/
RUN chmod -R a+rwx Templates
CMD ["python","app.py"]