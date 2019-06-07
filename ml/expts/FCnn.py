# LOSS : cross entropy
# output activation: softmax
# hidden activation: sigmoid
import numpy as np
x = 'input'
g = {}
gw = {}
gb = {}
w = {}
b = {}
h = {}
h[0] = x
lr = 0.1
def backprop(y,yhat,num_layers=4):
    g[num_layers+1] = yhat - y
    for k in range(num_layers,0,-1):
        gw[k] = np.dot(g[k+1],h[k-1])
        gb[k] = g[k+1]

        w[k] = w[k] - lr*gw[k]
        b[k] = b[k] - lr*gb[k]

        g_hk_prev = np.dot(w[k],g[k+1])
        g[k] = np.dot(g_hk_prev,np.dot(a[k-1],1-a[k-1]))


