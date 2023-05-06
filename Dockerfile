FROM python:3.7-buster

WORKDIR /home/

# Download models
RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1v091s0eY4_VOLU9BqDXVSaZcFnA9qJPl' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1v091s0eY4_VOLU9BqDXVSaZcFnA9qJPl" -O CoreNet.weights && rm -rf /tmp/cookies.txt
RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1wdGZKNNDAyN-fajjVKJoiyDtXAvl-4zq' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1wdGZKNNDAyN-fajjVKJoiyDtXAvl-4zq" -O FineNet.h5 && rm -rf /tmp/cookies.txt
RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1dfQDW8yxjmFPVu0Ddui2voxdngOrU3rc' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1dfQDW8yxjmFPVu0Ddui2voxdngOrU3rc" -O CoarseNet.h5 && rm -rf /tmp/cookies.txt
RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1alvw_kAyY4sxdzAkGABQR7waux-rgJKm' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1alvw_kAyY4sxdzAkGABQR7waux-rgJKm" -O ClassifyNet_6_classes.h5 && rm -rf /tmp/cookies.txt

RUN apt update && apt dist-upgrade -y
RUN apt update && apt install ffmpeg libsm6 libxext6  -y
RUN apt update && apt install -y python3-opencv

COPY requirements.txt ./requirements.txt
RUN pip --no-cache-dir install --upgrade pip && \
    pip --no-cache-dir install -r requirements.txt


COPY *.tif ./
COPY main.py ./

