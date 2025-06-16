# Use the Python version that matches your local machine
FROM python:3.12-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a non-root user for security
RUN useradd -m -u 1000 user
USER user

# Set the working directory AND add the user's bin to the PATH
WORKDIR /home/user/app
# --- THIS IS THE FIX ---
ENV PATH="/home/user/.local/bin:${PATH}"
# --------------------

# Copy and install dependencies
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all your project files
COPY --chown=user . .

# Run collectstatic
RUN python manage.py collectstatic --no-input

# Expose the correct port
EXPOSE 7860

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "FER_deploy.wsgi"]