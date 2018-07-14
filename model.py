"""

Model predicting script.

"""


import tensorflow as tf
import numpy as np


def scale_image(images):
    """Scale the images to [0, 1]."""
    result = []
    for subimage in images:
        current = []
        for row in subimage:
            line = []
            for value in row:
                line.append(np.float32(value/255))
            current.append(line)
        result.append(np.array(current))
    return result


def one_hot_y(list_y):
    """One hot encode the y variable."""
    result = []
    for value in list_y:
        answer = [0]*10
        answer[value] = 1
        result.append(np.float32(answer))
    return result


x3 = scale_image(test2)

x1 = scale_image(res1)
x2 = scale_image(res2)
xss = x1 + x2
labs = label + label2

my_y = np.array(one_hot_y(labs))
my_x = np.array(xss)


def nn(x):
    """Neural Network."""
    x_tensor = tf.reshape(x, [-1, 33, 33, 1])

    # Layer 1
    w_conv1 = weight_var([5, 5, 1, 32])
    b_conv1 = bias_var([32])

    h_conv1 = tf.nn.relu(conv(x_tensor, w_conv1) + b_conv1)
    h_pool1 = max_pool(h_conv1)

    # Layer 2
    w_conv2 = weight_var([5, 5, 32, 64])
    b_conv2 = bias_var([64])

    h_conv2 = tf.nn.relu(conv(h_pool1, w_conv2) + b_conv2)
    h_pool2 = max_pool(h_conv2)

    # Fully connected
    w_fc1 = weight_var([9*9*64, 1024])
    b_fc1 = bias_var([1024])

    h_pool2_flat = tf.reshape(h_pool2, [-1, 9*9*64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w_fc1) + b_fc1)

    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    W_fc2 = weight_var([1024, 10])
    b_fc2 = bias_var([10])

    y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

    return y_conv, keep_prob


def weight_var(shape):
    """Get a weight variable from shape."""
    weights = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(weights)


def bias_var(shape):
    """Get a bias variable from shape."""
    bias = tf.constant(0.1, shape=shape)
    return tf.Variable(bias)


def conv(x, W):
    """Convolution layer."""
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool(x):
    """2d max pooling."""
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                          padding='SAME')


x = tf.placeholder(tf.float32, [None, 33, 33])

# Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, 10])

# Build the graph for the deep net
y_conv, keep_prob = nn(x)

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv, 0), tf.argmax(y_, 0))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))



with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        batch = np.random.choice(len(xss), size=50)
        if i % 20 == 0:
            train_accuracy = accuracy.eval(feed_dict={
                 x: my_x[batch], y_: ny_y[batch], keep_prob: 0.99})
            print('step %d, training accuracy %g' % (i, train_accuracy))
        train_step.run(feed_dict={x: my_x[batch], y_: ny_y[batch], keep_prob: 0.5})
