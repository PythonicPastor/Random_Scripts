from concurrent.futures import ThreadPoolExecutor as tp
import numpy as np

funct1 = [np.random.randint(0,5)]
def funct2():
    print('hello world')



with tp() as e:
    responses = e.map(funct1, funct2)
