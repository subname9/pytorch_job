import torch
import requests

# Ensure CUDA is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Generate two random 2048x2048 matrices
matrix1 = torch.rand(2048, 2048, device=device)
matrix2 = torch.rand(2048, 2048, device=device)

# Multiply the matrices
result = torch.matmul(matrix1, matrix2)

# Make an HTTP request
response = requests.get("http://174.138.72.98:3000/hello")
if response.status_code != 200:
    raise Exception(f"Failed to fetch data: Status code {response.status_code}")
