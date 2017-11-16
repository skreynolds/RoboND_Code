import tensorflow as tf
import numpy as np

###NOTE THIS WILL NOT WORK LOCALLY AS IT MAKES CALLS TO UNSUPPORTED FEATURE IN NEW TF###

def upsample(x):
    """
    Apply a two times upsample on x and return the result.
    :x: 4-Rank Tensor
    :return: TF Operation
    """
    # TODO: Use `tf.layers.conv2d_transpose`
    x_dims = x.get_shape().as_list()
    num_outputs = x_dims[3]
    kernel_size = 2*(x_dims[1])
    stride = (2,2)
    padding = 'SAME'
    return tf.contrib.layers.conv2d_transpose(x, num_outputs, (kernel_size, kernel_size), stride, padding)


x = tf.constant(np.random.randn(1, 4, 4, 3), dtype=tf.float32)
conv = upsample(x)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    result = sess.run(conv)

    print('Input Shape: {}'.format(x.get_shape()))
    print('Output Shape: {}'.format(result.shape))
