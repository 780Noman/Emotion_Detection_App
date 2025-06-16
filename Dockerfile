# Use the Python version that matches your local machine
FROM python:3.12-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and switch to a non-root user for security
RUN useradd -m -u 1000 user
USER user

# Set the working directory and add the user's bin to the PATH
WORKDIR /home/user/app
ENV PATH="/home/user/.local/bin:${PATH}"

# Copy and install Python dependencies from the corrected requirements file
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all your project files
COPY --chown=user . .

# Run the 'collectstatic' command required by Django
RUN python manage.py collectstatic --no-input

# Expose the correct port
EXPOSE 7860

# Command to start your Django application
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "FER_deploy.wsgi"]