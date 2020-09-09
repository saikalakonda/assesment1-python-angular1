FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --trusted-host pypi.python.org autopep8 elasticsearch


COPY . .

CMD [ "python", "./run.py" ]
