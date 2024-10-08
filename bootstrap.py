import numpy as np
from tqdm import tqdm

import time

def bootstrap_prob():
    np.random.seed(int(time.time()))
    # The sample of 10 observations(i.i.d random variables) from population with unknown μ.
    sample = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]

    # Set the number of resamples as 100000 
    no_of_resamples = 10000000

    # The list of means of resamples
    resample_means = []

    # Create resamples by bootstrap method and get the means of them.
    for _ in tqdm(range(no_of_resamples)):
        resample = np.random.choice(sample, 10)
        resample_means.append(np.mean(resample))

    # We use the mean of the resamples mean set as a reasonable estimated mean of population
    resonable_estimated_mean = np.mean(resample_means)

    # Record no of the diff in range (-4, 6)
    dif_in_range = 0
    for mean in resample_means:
        diff = mean - resonable_estimated_mean
        if -4 < diff and diff < 6:
            dif_in_range += 1
        else:
            continue
    
    # Calculate the probability by record/no of means
    probability = dif_in_range/no_of_resamples

    print(probability)


bootstrap_prob()
