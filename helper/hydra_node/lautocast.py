import torch
import os

lowvram = True if os.environ.get('LOWVRAM') == "1" else False
medvram = True if os.environ.get('MEDVRAM') == "1" else False
dtype = torch.float32 if os.environ.get('DTYPE', 'float32') else torch.float16


print("using dtype: " + os.environ.get('DTYPE', 'float32'))
