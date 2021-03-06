FROM python:3.8

COPY . /todoapp
WORKDIR /todoapp

COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt



EXPOSE 5000

ENTRYPOINT [ "python", "app.py" ]