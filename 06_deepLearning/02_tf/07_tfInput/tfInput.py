# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:49:51 2017

@author: Shane Reynolds
"""

# Solution is available in the other "solution.py" tab
import tensorflow as tf


def run():
    output = None
    x = tf.placeholder(tf.int32)

    with tf.Session() as sess:
        # TODO: Feed the x tensor 123
        output = sess.run(x, feed_dict={x: 123})

    return output

if __name__ == '__main__':
    test = run()