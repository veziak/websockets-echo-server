FROM python:3.13

RUN  pip install --upgrade pip
RUN mkdir /app
COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py
RUN pip install -r /app/requirements.txt
CMD python3 /app/main.py
