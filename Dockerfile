FROM python
RUN pip freeze
COPY requirement.txt /requirement.txt
RUN pip install -r /requirement.txt
COPY . /
RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]

