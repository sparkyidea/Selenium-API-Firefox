FROM sparkyidea/selenium-api-firefox:latest

# Copy your application files
RUN rm -rf /app
COPY ./app/ /app/

WORKDIR /app

# Install Python dependencies
RUN pip3 install -r requirements.txt && \
    rm requirements.txt

EXPOSE 8080

# Set the entrypoint for your application
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]