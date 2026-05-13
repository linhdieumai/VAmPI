FROM python:3.11-alpine AS builder
RUN apk --update add bash g++ nano 
COPY ./requirements.txt /vampi/requirements.txt
WORKDIR /vampi
RUN pip install --only-binary :all: -r requirements.txt

# Build a fresh container, copying across files & compiled parts
FROM python:3.11-alpine
COPY . /vampi
WORKDIR /vampi
COPY --from=builder /usr/local/lib /usr/local/lib
COPY --from=builder /usr/local/bin /usr/local/bin
ENV vulnerable=1
ENV tokentimetolive=60

USER non-root ENTRYPOINT ["python"]
USER non-root CMD ["app.py"]
