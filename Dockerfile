FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
RUN mkdir Templates
COPY produto.py /
COPY Templates/*  /Templates/
RUN chmod -R a+rwx Templates
CMD ["python","produto.py"]
