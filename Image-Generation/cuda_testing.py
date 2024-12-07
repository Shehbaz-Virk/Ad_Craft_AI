import torch

# print(torch.__version__)
# print(torch.version.cuda)

import torch
print(torch.__version__)  # Should show something like 2.5.1+cu121
print(torch.version.cuda)  # Should show the CUDA version, e.g., 12.1
print(torch.cuda.is_available())  # Should return True
print(torch.cuda.get_device_name(0))  # Should display your GPU name
