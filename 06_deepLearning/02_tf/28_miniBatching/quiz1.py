# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 11:48:36 2017

@author: Shane Reynolds
"""

import math
def batches(batch_size, features, labels):
    """
    Create batches of features and labels
    :param batch_size: The batch size
    :param features: List of features
    :param labels: List of labels
    :return: Batches of (Features, Labels)
    """
    assert len(features) == len(labels)
    # TODO: Implement batching
    # Get the total number of full batches
    num_full_batches = len(features) // batch_size
    
    # Get the size of the final batch
    final_batch_size = len(features) - (num_full_batches*batch_size)
    
    # Initialise the returned batch list
    batch_list = []
    
    for batch_num in range(num_full_batches):
        # Create the features and labels batch components
        features_batch = features[batch_num:batch_num + batch_size]
        labels_batch = labels[batch_num:batch_num + batch_size]
        
        # Create the batch instance
        batch = [features_batch, labels_batch]
        
        # Append the batch to the batches list
        batch_list.append(batch)
    
    if final_batch_size != 0:
        # Create the final feature and labels batch
        final_feat_batch = features[-final_batch_size:]
        final_lab_batch = labels[-final_batch_size:]
        
        # Create the final batch instance
        final_batch = [final_feat_batch, final_lab_batch]
        
        # Append the final batch to the batches list
        batch_list.append(final_batch)
    
    return batch_list

''' This is an entirely better way to implement this code
    take note of the use of the range function with steps
    to help with the irregular sample size (i.e. a sample
    size that isn't an integer multiple exactly with the 
    required batch size)
    
import math
def batches(batch_size, features, labels):
    """
    Create batches of features and labels
    :param batch_size: The batch size
    :param features: List of features
    :param labels: List of labels
    :return: Batches of (Features, Labels)
    """
    assert len(features) == len(labels)
    # TODO: Implement batching
    output_batches = []
    
    sample_size = len(features)
    for start_i in range(0, sample_size, batch_size):
        end_i = start_i + batch_size
        batch = [features[start_i:end_i], labels[start_i:end_i]]
        output_batches.append(batch)
        
    return output_batches
'''