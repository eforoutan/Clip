FROM python:3.9-slim

RUN pip install geopandas

WORKDIR /app

COPY clip_shp.py /app/clip_shp.py

ENTRYPOINT [ "python3", "/app/clip_shp.py" ]