FROM python:3.9.10

RUN apt update  && yes | apt upgrade

COPY github_repo_scanner /home/github_repo_scanner
COPY setup.py /home/
COPY requirements.txt /home/

WORKDIR /home
RUN pip install -r requirements.txt
RUN python setup.py install

CMD ["start_github_repo_scanner"]