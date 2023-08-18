# This file defines the Docker container that will contain the Crawler app.
# From the source image #python
FROM msellami/weather_etl:latest
# Identify maintainer
LABEL maintainer = "florencenkpedji9@gmail.com"
# Set the default working directory
WORKDIR /app/
COPY crawler.py requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["python","./crawler.py"]
# When the container starts, run this
ENTRYPOINT ["python","./crawler.py"]
