FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/app/

# Set working directory
WORKDIR /app/
RUN pip install --upgrade pip setuptools

RUN apt-get update && apt-get install \
      --no-install-recommends --no-install-suggests -y build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get autoremove -y \
    && apt-get clean

# Install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000
EXPOSE 8000

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]

# Run the application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]