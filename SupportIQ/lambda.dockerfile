FROM python:3.11-slim

WORKDIR /app

#Copy required files
COPY requirements.txt /app/
COPY src/inference.py /app/src
COPY src/lambda_func.py /app/src

#Install dependencies
RUN pip install awslambdaric
RUN pip install -r requirements.txt

#Set lambda function 
CMD ["awslambdaric","lambda_func.lamda_function"]