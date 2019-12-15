FROM python:3.5
# RUN pip install Flask==0.11.1
RUN pip install Flask==0.11.1 redis==2.10.5
RUN useradd -ms /bin/bash bawa
USER bawa
WORKDIR /app
COPY app /app
CMD ["python", "app.py"] 
