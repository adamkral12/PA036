FROM python:3.6
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app
RUN pip install -r requirements.txt

# run the app
ENV PYTHONPATH .
ADD . /app/app
CMD python app/main.py