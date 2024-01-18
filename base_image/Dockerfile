FROM python:3.9-slim

# Update package list and install Firefox ESR
RUN apt-get update && \
    apt-get install -y curl firefox-esr=115.6.0esr-1~deb12u1 && \
    rm -rf /var/lib/apt/lists/*

# Install geckodriver
RUN curl -o geckodriver.tar.gz -sSL https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux-aarch64.tar.gz \
    && tar -xzf geckodriver.tar.gz -C /usr/local/bin \
    && rm geckodriver.tar.gz

# Copy your application files
COPY ./app/ /app/

WORKDIR /app

# Install Python dependencies
RUN pip3 install -r requirements.txt

EXPOSE 8080

# Set the entrypoint for your application
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
