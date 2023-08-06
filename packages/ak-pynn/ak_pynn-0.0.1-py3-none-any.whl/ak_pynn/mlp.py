'''
This is the complete code of MultiLayer Neural Network

Developed by: 
    - Ankit Kohli (Student at Delhi University)
    - ankitkohli181@gmail.com (mail)

Have fun!

'''

import numpy as np
import random
import time
import math
from utils import *
from tqdm import tqdm

class instance_variables:
    def __init__(self):
        super(instance_variables, self).__init__()
        self.weights = []
        self.bias = []
        self.Vdb = []
        self.Vdw = []
        self.Mdw = []
        self.Mdb = []
        self.derivatives_w = []
        self.derivatives_b = []
        self.regularization = None
        self.activations = []
        self.node_values = []
        self.dropout_nodes = []
        self.layers = []

class Weight_Initalizer(instance_variables):
    def __init__(self):
        super(Weight_Initalizer, self).__init__()
        self.weight_initializers_method = {
            'random_uniform': self.random_uniform,
            'random_normal': self.random_normal,
            'glorot_uniform': self.glorot_uniform,
            'glorot_normal': self.glorot_normal,
            'he_uniform': self.he_uniform,
            'he_normal': self.he_normal
        }

    def random_uniform(self, seed=None, args=dict()):
        minval = -0.05
        maxval = 0.05
        for key, value in args.items():
            if (key == 'minval'):
                minval = value
            elif (key == 'maxval'):
                maxval = value
            elif (key == 'seed'):
                np.random.seed(seed)

        for i in range(1,len(self.layers)):
            self.weights[i-1] = np.random.uniform(minval, maxval, size=(self.layers[i]['nodes'], self.layers[i-1]['nodes']))
    
    def random_normal(self, args=dict()):
        for key, value in args.items():
            if (key == 'seed'):
                np.random.seed(value)
        for i in range(1,len(self.layers)):
            self.weights[i-1] = np.random.randn(self.layers[i]['nodes'], self.layers[i-1]['nodes'])

    def glorot_uniform(self, args=dict()):
        for key, value in args.items():
            if (key == 'seed'):
                np.random.seed(value)
        for i in range(1,len(self.layers)):
            limit = np.sqrt(6 / (self.layers[i]['nodes'] + self.layers[i-1]['nodes']))
            vals = np.random.uniform(-limit, limit,size=(self.layers[i]['nodes'], self.layers[i-1]['nodes']))
            self.weights[i-1] = vals

    def glorot_normal(self, args=dict()):
        for key, value in args.items():
            if (key == 'seed'):
                np.random.seed(value)
        for i in range(1,len(self.layers)):
            limit = np.sqrt(2 / (self.layers[i]['nodes'] + self.layers[i-1]['nodes']))
            vals = np.random.randn(self.layers[i]['nodes'], self.layers[i-1]['nodes'])*limit
            self.weights[i-1] = vals

    def he_uniform(self, seed=None, args=dict()):
        for key, value in args.items():
            if (key == 'seed'):
                np.random.seed(value)
        for i in range(1,len(self.layers)):
            limit = np.sqrt(6 / (self.layers[i-1]['nodes']))
            vals = np.random.uniform(-limit, limit,size=(self.layers[i]['nodes'], self.layers[i-1]['nodes']))
            self.weights[i-1] = vals

    def he_normal(self, args=dict()):
        for key, value in args.items():
            if (key == 'seed'):
                np.random.seed(value)
        for i in range(1,len(self.layers)):
            vals = np.random.randn(
                self.layers[i]['nodes'], self.layers[i-1]['nodes']) * np.sqrt(2/(self.layers[i-1]['nodes']))
            self.weights[i-1] = vals


class Optimizers(Weight_Initalizer):
    def __init__(self):
        super(Optimizers, self).__init__()
        self.epsilon = 1e-07
        self.momentum = 0.9
        self.beta = 0.9
        self.beta1 = 0.9
        self.beta2 = 0.999
        self.optimizer_function = {
            'momentum': self.Momentum,
            'gradient_descent': self.gradient_descent,
            'AdaGrad': self.AdaGrad,
            'RMSprop': self.RMSprop,
            'Adam': self.Adam
        }

    def get_gradients(self, layer):
        derivatives_w = None
        derivatives_b = None
        if (self.regularization == 'L2_norm'):
            derivatives_w = self.derivatives_w[layer] + (2*self.penalty*self.weights[layer])
        elif (self.regularization == 'L1_norm'):
            derivatives_w = self.derivatives_w[layer]+self.penalty
        else:
            derivatives_w = self.derivatives_w[layer]

        derivatives_b = self.derivatives_b[layer].flatten()
        return derivatives_w, derivatives_b

    def gradient_descent(self, learningRate=0.001):
        for i in range(len(self.layers)-1):
            dw, db = self.get_gradients(i)
            self.weights[i] -= (dw * learningRate)
            self.bias[i] -= (db * learningRate)

    def Momentum(self, learningRate=0.001):
        for i in range(len(self.layers)-1):
            dw, db = self.get_gradients(i)
            self.Vdw[i] = (self.momentum*self.Vdw[i]) + (dw*learningRate)
            self.Vdb[i] = (self.momentum*self.Vdb[i]) + (db*learningRate)
            self.weights[i] -= self.Vdw[i]
            self.bias[i] -= self.Vdb[i]

    def AdaGrad(self, learningRate=0.001):
        for i in range(len(self.layers)-1):
            dw, db = self.get_gradients(i)
            self.Vdw[i] = self.Vdw[i]+(dw**2)
            self.Vdb[i] = self.Vdb[i]+(db**2)
            self.weights[i] -= (learningRate*( dw/np.sqrt(self.Vdw[i]+self.epsilon)))
            self.bias[i] -= (learningRate*(db/np.sqrt(self.Vdb[i]+self.epsilon)))

    def RMSprop(self, learningRate=0.001):
        for i in range(len(self.layers)-1):
            dw, db = self.get_gradients(i)
            self.Vdw[i] = self.beta*self.Vdw[i]+(1-self.beta)*(dw**2)
            self.Vdb[i] = self.beta*self.Vdb[i]+(1-self.beta)*(db**2)
            self.weights[i] -= (learningRate*( dw/np.sqrt(self.Vdw[i]+self.epsilon)))
            self.bias[i] -= (learningRate*(db/np.sqrt(self.Vdb[i]+self.epsilon)))

    def Adam(self, learningRate=0.001):
        for i in range(len(self.layers)-1):
            dw, db = self.get_gradients(i)
            self.Mdw[i] = self.beta1*self.Mdw[i]+(1-self.beta1)*dw
            self.Vdw[i] = self.beta2*self.Vdw[i]+(1-self.beta2)*(dw**2)
            m_dw = self.Mdw[i]/(1-self.beta1)
            v_dw = self.Vdw[i]/(1-self.beta2)
            self.weights[i] -= (learningRate*(m_dw/np.sqrt(v_dw+self.epsilon)))

            self.Mdb[i] = self.beta1*self.Mdb[i]+(1-self.beta1)*db
            self.Vdb[i] = self.beta2*self.Vdb[i]+(1-self.beta2)*(db**2)
            m_db = self.Mdb[i]/(1-self.beta1)
            v_db = self.Vdb[i]/(1-self.beta2)
            self.bias[i] -= (learningRate*(m_db/np.sqrt(v_db+self.epsilon)))
            
    
class MultiLayerNeuralNetwork(Optimizers):
    def __init__(self):
        super(MultiLayerNeuralNetwork, self).__init__()
        self.history = {'Losses': [], 'Weights': [],'Biases': []}
        self.loss_functions = {
            "mae": mae,
            "mse": mse,
            "binary_cross_entropy": binary_cross_entropy,
            "categorical_cross_entropy": categorical_cross_entropy
        }
        self.loss_function_grads = {
            "mae": MAE_grad,
            "mse": MSE_grad,
            "binary_cross_entropy": BCE_grad,
            "categorical_cross_entropy": CCE_grad
        }
        
        self.activation_functions = {
            "sigmoid": sigmoid,
            "softplus": softplus,
            "softmax": softmax,
            "relu": relu,
            "leaky_relu": leaky_relu,
            "elu": elu,
            "tanh": tanh,
            "linear": linear
        }

    def show_summary(self):
        print(f'''
        {'( MODEL SUMMARY )'.center(80)}
        
        ==================================================================================
        {"Layer".center(20)}{"Activation Function".center(20)}{"Output Shape".center(20)}{"Params".center(20)}
        ==================================================================================''')
        p_sum=0

        for i in range(len(self.layers)):
            p_sum+=self.layers[i]['params']
            print(f'''
        {self.layers[i]['type'].center(20)}{str(self.layers[i]['activation_function']).center(20)}{str(self.layers[i]['output_shape']).center(20)}{str(int(self.layers[i]['params'])).center(20)}
        ----------------------------------------------------------------------------------''')
        
        print(f'''
        ==================================================================================

        Total Params (trainable) - {int(p_sum)}
        __________________________________________________________________________________
        ''')
    
    def add_layer(self, nodes=3, activation_function='linear', input_layer=False, output_layer=False, dropouts=False, dropout_fraction=None, **kwargs):
        if (input_layer is True):           
            self.n_inputs = nodes
            self.layers.append({'nodes': nodes, 'activation_function': 'linear', 'dropouts': False,'type':'Input','output_shape':(None,nodes),'batch_norm':None,'params':0})
        elif (output_layer is not False):
            self.n_outputs = nodes
            self.layers.append({'nodes': nodes, 'activation_function': activation_function, 'dropouts': False,'type':'Output','output_shape':(None,nodes),'batch_norm':None,'params':0})
        else:
            self.layers.append({'nodes': nodes, 'activation_function': activation_function,'dropouts': dropouts, 'dropout_fraction': dropout_fraction,'type':'Dense','output_shape':(None,nodes),'batch_norm':None,'params':0})


    def compile_model(self, loss_function='mse', weight_initializer='glorot_uniform',optimizer="RMSprop", show_summary=True, **kwargs):
        self.loss_func = loss_function
        self.optimizer = optimizer
        self.weight_initializer=weight_initializer
        for i in range(1,len(self.layers)):
            self.Vdw.append(np.zeros((self.layers[i]['nodes'], self.layers[i-1]['nodes'])))
            self.Mdw.append(np.zeros((self.layers[i]['nodes'], self.layers[i-1]['nodes'])))
            self.weights.append(np.random.rand(self.layers[i]['nodes'], self.layers[i-1]['nodes']))
            self.derivatives_w.append(np.zeros((self.layers[i]['nodes'], self.layers[i-1]['nodes'])))
            self.bias.append(np.zeros(self.layers[i]['nodes']))
            self.Vdb.append(np.zeros(self.layers[i]['nodes']))
            self.Mdb.append(np.zeros(self.layers[i]['nodes']))
            self.dropout_nodes.append(np.zeros(self.layers[i]['nodes'], dtype=bool))
            self.derivatives_b.append(np.zeros(self.layers[i]['nodes']))

            if (self.layers[i]['dropouts'] == True):
                self.add_dropouts(i, self.layers[i]['dropout_fraction'])

            if i>0:
                self.layers[i]['params']+=self.layers[i]['nodes']


            self.layers[i]['params']+=(self.layers[i]['nodes']*self.layers[i-1]['nodes'])

        self.weight_initializers_method[self.weight_initializer](kwargs)

        for key, value in kwargs.items():
            if (key == 'momentum'):
                self.momentum = value
            elif (key == 'epsilon'):
                self.epsilon = value
            elif (key == 'beta'):
                self.beta = value
            elif (key == 'beta1'):
                self.beta1 = value
            elif (key == 'beta2'):
                self.beta2 = value

        if(show_summary):
            self.show_summary()

    def add_dropouts(self, layer, fraction):
        drop_size = np.ceil(fraction*self.layers[layer]['nodes'])
        node_id = random.sample(range(self.layers[layer]['nodes']), int(drop_size))
        for j in node_id:
            self.dropout_nodes[layer][j-1] = True

    def add_regularization(self, name='L1_norm', penalty=0.1):
        self.penalty = penalty
        self.regularization = name


    def check_encoding(self, X):
        return ((X.sum(axis=1)-np.ones(X.shape[0])).sum() == 0)

    def forward_propagate(self, x):
        """
        Performs forward propagation on Batch input
        Input: x- ndarray (Input data)
        
        Returns: ndarray - activations of last Layer
        """
        self.activations[0] = x
        self.node_values[0] = x
        for i in range(1, len(self.layers)):
            self.node_values[i] = np.dot(self.activations[i-1], self.weights[i-1].T)+self.bias[i-1]
            self.activations[i] = self.activation_functions[self.layers[i]['activation_function']](self.node_values[i])
            if (self.layers[i]['dropouts'] == True):
                self.activations[i][np.where(self.dropout_nodes[i])] = 0
                self.node_values[i][np.where(self.dropout_nodes[i])] = 0

        return self.activations[len(self.layers)-1]

    def back_propagate(self, y, p):

        """
        Performs Back propagation on Batch input

        Input: p- predictions (N, k) ndarray (N: no. of samples, k: no. of output nodes)
               y- targets (N, k) ndarray (N: no. of samples, k: no. of output nodes)

        Returns: None

        """

        error = float('inf')
        error=self.loss_function_grads[self.loss_func](y,p)
        for i in reversed(range(len(self.derivatives_w))):
            delta_w = None
            func_name = self.layers[i+1]['activation_function']
            activation_func = self.activation_functions[func_name]
            if (func_name=="softmax"):
                 delta_w= softmaxTimesVector(error,activation_func(self.activations[i+1], derive=True))
            else:
                 delta_w = error*activation_func(self.activations[i+1], derive=True)
            self.derivatives_w[i] = np.dot(delta_w.T,self.activations[i])/self.batch_size
            self.derivatives_b[i] = np.sum(delta_w,axis=0)/self.batch_size
            error = np.dot(delta_w,self.weights[i])

    def fit(self, x, y, learning_rate=0.001, epochs=50, batch_size=32, show_loss=False, early_stopping=False, patience=2,shuffle=False):
        loss = float('inf')
        total_time=0
        patience_count = 0
        self.batch_size=batch_size
        if len(y.shape)==1:
            y=y.reshape(-1,1)
        else:
            if self.check_encoding(y) is False:
                print("ERROR: please use one-hot-encoded targets")
                return

        if show_loss is False:
            epoch_range=tqdm(range(1,epochs+1),desc="Training progress :")
        else:
            epoch_range=range(1,epochs+1)

        for i in epoch_range:
            t = Timer()
            t.start()
            sum_errors = 0
            if shuffle is True:
                shuffled_indices = np.random.permutation(x.shape[0])
                x = x[shuffled_indices]
                y = y[shuffled_indices]

            x_batches=np.array_split(x,math.ceil(x.shape[0]/batch_size))
            y_batches=np.array_split(y,math.ceil(y.shape[0]/batch_size))
            n_batches = len(x_batches)

            if show_loss is True:
                batch_range=tqdm(range(1,n_batches+1),desc=f"EPOCH {i} : ")
            else:
                batch_range=range(1,n_batches+1)
                
            for b in batch_range:
                X_batch=x_batches[b-1]
                Y_batch=y_batches[b-1]
                if shuffle is True:
                    shuffled_indices = np.random.permutation(X_batch.shape[0])
                    X_batch = X_batch[shuffled_indices]
                    Y_batch = Y_batch[shuffled_indices]

                self.activations=[]
                self.node_values=[]
                for j in range(len(self.layers)):
                    self.activations.append(np.zeros((len(X_batch),self.layers[j]['nodes'])))
                    self.node_values.append(np.zeros((len(X_batch),self.layers[j]['nodes'])))

                output=self.forward_propagate(X_batch)
                self.back_propagate(Y_batch, output)
                self.optimizer_function[self.optimizer](learning_rate)

                batch_loss=self.loss_functions[self.loss_func](Y_batch, output)
                sum_errors += batch_loss

                if show_loss is True:
                    batch_range.set_postfix_str(f"Loss: {sum_errors/b:.5f}")

            elapse_time=t.stop()
            total_time+=elapse_time
            loss = sum_errors/n_batches

            if show_loss is False:
                epoch_range.set_postfix_str(f"Loss : {loss:.5f}")

            if(len(self.history['Losses']) > 1 and loss <= self.history['Losses'][-1]):
                patience_count=0

            if (early_stopping == True and len(self.history['Losses']) > 1 and loss > self.history['Losses'][-1]):
                patience_count += 1
                if (patience_count >= patience):
                    print(
                        "\n<==================(EARLY STOPPING AT --> EPOCH {})====================> ".format(i))
                    break

            self.history['Losses'].append(loss)
            self.history['Weights'].append(self.weights)
            self.history['Biases'].append(self.bias)

        print("\nFinal Minimised Loss : {}".format(self.history['Losses'][-1]))
        print(f"\nTraining complete!! , Average Elapse-Time (per epoch) : {(total_time/epochs):.5f} seconds")
        print("========================================================================= :)")
        return self.history['Losses']


    def predict(self, x):
        outputs = []
        values = x
        for i in range(1, len(self.layers)):
            if (self.layers[i-1]['dropouts'] == True):
                wgt = self.weights[i-1] * self.layers[i-1]['dropout_fraction']
                z = np.dot(values, wgt.T)+self.bias[i-1]
            else:
                z = np.dot(values, self.weights[i-1].T)+self.bias[i-1]
            values = self.activation_functions[self.layers[i]['activation_function']](z)
        outputs.append(values)

        return np.array(outputs).reshape(-1, self.n_outputs)


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None
        
    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self,show_elapsed=False):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        if show_elapsed:
            print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return elapsed_time