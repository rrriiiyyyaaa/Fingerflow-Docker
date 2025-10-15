#!/bin/bash
docker build -t fingerflow_riya .


docker run -it -v $(pwd)/models:/home/models -v $(pwd)/db:/home/db fingerflow_riya python main.py