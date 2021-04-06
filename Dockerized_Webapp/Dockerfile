FROM python:3.6-slim
COPY webapp_housing.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./forest_reg.pkl /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python", "webapp_housing.py"]