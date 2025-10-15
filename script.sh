#!/bin/bash
docker build -t fingerflow_riya .


docker run -it \
-v ./models:/home/models \
-v ./db:/home/db \
-v ./scripts:/home/scripts \
fingerflow_riya \
python scripts/main_riya.py