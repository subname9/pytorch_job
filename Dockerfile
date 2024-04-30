FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

# Install requests package
RUN pip install requests
COPY . .
RUN 
CMD ["python", "job.py"]