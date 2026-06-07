import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    # ReLU keeps positive values, turns negatives to 0
    return np.maximum(0, z)

def forward_pass(X, W1, b1, W_output, b_output):
    
    """  Implements the forward propagation for a double-layer (hidden and output) neural network.
    
     Inputs:
        X : Input data matrix of shape (examples, features).
        W1 : Weight matrix of hidden layer
        b1 : Bias terms of input layer
        W_output : Weight matrix of output layer
        b_output : Bias (its only one) of output later
        
     Returns:
         Predicted probabilities"""
   
    # Hidden layer
    Z1 = np.dot(X, W1) + b1     # (10,5)·(5,5) + (1,5) = (10,5)
    A1 = sigmoid(Z1)            # (10,5)
    
    # Output layer
    Z_output = np.dot(A1, W_output) + b_output   # (10,5)·(5,1) + (1,1) = (10,1)
    A_output = sigmoid(Z_output)              # (10,1)
    
    return A_output

def loss_function(Predicted, correct):
    
    # Computes the binary cross-entropy loss.
    
    # Inputs:
    #     Predicted probabilities from the forward pass.
    #     "correct" array: True labels.
        
    # Returns:
    #     float: The binary cross-entropy loss.
    
    m = correct.shape[0]  # Takes the number of examples, so m = 10 as 'correct' is (10,1)

    # Quick visualization (10 examples, each one has 5 features):
    # Example	Feature 1	Feature 2	Feature 3	Feature 4	Feature 5
    # 0	           x₁₁	       x₁₂	        x₁₃	        x₁₄	        x₁₅
    # 1	           x₂₁	       x₂₂	        x₂₃	        x₂₄	        x₂₅
    # ...	...	...	...	...	...
    # 10	       x₁₀₁       x₁₀₂          x₁₀₃          x₁₀₄       x₁₀₅ 

    # Ensure numerical stability by clipping values to avoid log(0)
    epsilon = 1e-8
    Predicted_clipped = np.clip(Predicted, epsilon, 1-epsilon)

    # Calculate the cross-entropy loss
    loss = (-1/m) * np.sum(correct * np.log(Predicted_clipped) + (1 - correct) * np.log(1 - Predicted_clipped))
    
    return loss

             # =======================================================  PROGRAM STARTS HERE ================================================
             # THIS IS A 2 LAYERED NETWORK
             # THIS NETWORK HAS 1 HIDDEN LAYER (5 NEURONS) AND 1 OUTPUT LAYER (1 NEURON)

inputs = np.random.randn(10, 5)  # 10 examples, each input has 5 features
correct_labels = np.random.randint(0, 2, size=(10, 1)) # Creates an array, starting from 0 (inclusive) to 2 (exclusive) so it can only be 0 or 1
# The size ensures that we get a column vector with 10 entries
 
# Dimensions
number_of_features = inputs.shape[1] # This will give us 5, as each input as five features → inputs is (10,5)
hidden_size = 5 # <-- you can change this

# Initialize weights and bias randomly
W1 = np.random.randn(number_of_features, hidden_size) * 0.01
b1 = np.zeros((1, hidden_size)) # .zeros() just creates an array full of zeros, as we normally start biases with zeros
W_output = np.random.randn(hidden_size, 1) * 0.01
b_output = np.zeros((1,1))


# Perform the forward pass
FP = forward_pass(inputs, W1, b1, W_output, b_output)

# Compute the loss, compare the forward pass result with the labels
Final_loss = loss_function(FP, correct_labels)

print(f"Correct labels: {correct_labels.flatten()}") # .flatten() turns it to a 1D array for easy viewing
print(f"Initial Predicted Probabilities : {np.round(FP.flatten(), 3)}") # np.round rounds it to 3 dec places
print(f"Initial Average Loss: {Final_loss:.3f}")