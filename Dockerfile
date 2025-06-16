# Use the Python version that matches your local machine
FROM python:3.12-slim

# Set environment variables to make Python run smoothly in Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a non-root user for better security (Hugging Face recommendation)
RUN useradd -m -u 1000 user
USER user

# Set the working directory inside the user's home folder
WORKDIR /home/user/app

# Copy and install dependencies
# The --chown flag ensures the 'user' has permission to use this file
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all your project files into the working directory
# The --chown flag gives the 'user' ownership of all your code
COPY --chown=user . .

# Run the 'collectstatic' command required by Django
RUN python manage.py collectstatic --no-input

# Tell Hugging Face that your app will be running on port 7860
EXPOSE 7860

# The command to start your Django application using the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "FER_deploy.wsgi"]