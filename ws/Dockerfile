FROM python:2.7.12

MAINTAINER Praveen Kumar Srinivasan "praveen.sxi@gmail.com"

# Set PYTHONUNBUFFERED so output is displayed in the Docker log
ENV PYTHONUNBUFFERED=1

# Expose The Port Number Of the App To The Host
EXPOSE 5000

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application's code
COPY . /app
WORKDIR /app
# Run the app
CMD [ "python", "app.py"]