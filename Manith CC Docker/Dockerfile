# Use a smaller base image
FROM python:3.9-alpine

# Set working directory inside the container
WORKDIR /home/data

# Copy local files to container
COPY . /home/data

# Copy the Python script and text files
COPY scripts.py /home/data/scripts.py
COPY IF.txt /home/data/IF.txt
COPY AlwaysRememberUsThisWay.txt /home/data/AlwaysRememberUsThisWay.txt

# Install any Python dependencies (if applicable)
# RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container starts
CMD ["python", "/home/data/scripts.py"]
