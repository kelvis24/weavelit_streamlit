# # Use an official Python runtime as a parent image
# FROM python:3.10-slim

# # Set the working directory to /app
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Make port 8501 available to the world outside this container
# EXPOSE 8501

# # Define environment variable
# ENV NAME World

# # Run app.py when the container launches
# CMD ["streamlit", "run", "rag_demo.py"]


FROM python:3.10-slim

WORKDIR /app

COPY . /app
COPY .env ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "rag_demo.py"]
