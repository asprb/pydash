FROM python:rc-alpine

WORKDIR /usr/src/pydash

COPY . .

RUN apk update

RUN pip3 install pip517
RUN python -m build .
RUN pip install dist/*.whl

EXPOSE 8712

CMD ["flask", "run"]