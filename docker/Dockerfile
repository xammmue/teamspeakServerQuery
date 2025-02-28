FROM python:3.13.2-bookworm

WORKDIR /usr/src/app

ADD ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD ./HostInfo.py .
ADD ./Client.py .
ADD ./ServerQuery.py .
ADD ./config.cfg .
ADD ./main.py .

CMD ["python", "main.py"]
