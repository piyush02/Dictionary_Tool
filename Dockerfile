# Use an Alpine Linux image as a base
FROM alpine:latest

# Set environment variables
ENV SERVE_PORT 5000

# Set the working directory in the container
WORKDIR /app

# Copy the compiled Python code into the container
COPY dist/dict_flask /app/dict_flask

# Make the script executable
RUN chmod +x /app/dict_flask

# Run the Python script when the container launches
CMD ["/app/dict_flask"]
