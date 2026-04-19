FROM python:3.12-slim

WORKDIR /app

#COPY required files
COPY requirements.txt .
COPY src/ ./src/

#Install requirements
RUN pip install --upgrade pip
RUN pip install awslambdaric
RUN pip install --no-cache-dir -r requirements.txt

#Make script readable and execuatble 
RUN chmod -R a+rX /app

#Command to run customer application
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric"]
CMD [ "src.lambda_function.lambda_handler"]