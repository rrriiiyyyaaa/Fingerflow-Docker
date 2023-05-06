#!/bin/bash
docker build -t fingerflow .
docker run -it fingerflow python main.py
