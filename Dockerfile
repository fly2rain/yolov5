# Start FROM Nvidia PyTorch image https://ngc.nvidia.com/catalog/containers/nvidia:pytorch
FROM nvcr.io/nvidia/pytorch:20.08-py3

# Install dependencies
RUN pip install --upgrade pip
# COPY requirements.txt .
# RUN pip install -r requirements.txt
RUN pip install gsutil

# Create working directory
RUN mkdir -p  /app
WORKDIR   /app

# Copy contents
#COPY .  /app

EXPOSE 22