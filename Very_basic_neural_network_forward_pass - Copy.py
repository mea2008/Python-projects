import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def forward_pass(X, W, b):
    
    # Implements the forward propagation for a single-layer neural network.
    
    # Inputs:
    #     X : Input data matrix of shape (examples, features).
    #     W : Weight matrix of shape (num_of_features, 1).
    #     b : Bias term.
        
    # Returns:
    #     Predicted probabilities
    
    # Calculate the weighted sum 
    weighted_sum = np.dot(X, W) + b
    
    # Apply the sigmoid activation function to get the probabilities
    Prob = sigmoid(weighted_sum)
    
    return Prob # Prob is an array

def loss_function(Prob, correct):
    
    # Computes the binary cross-entropy loss.
    
    # Inputs:
    #     Predicted probabilities from the forward pass.
    #     "correct" array: True labels.
        
    # Returns:
    #     float: The binary cross-entropy loss.
    
    m = correct.shape[0]  # Takes the number of examples, so m = 10 as 'correct' is (10,1)
    # correct.shape[0] → first number (rows) = number of examples.
    # Why not correct.shape[1]? 
    # Because we don’t care about columns for loss. 
    # We only need how many examples to divide by.
    # We use 0 because rows = examples.

    # Quick visualization (10 examples, each one has 5 features):
    # Example	Feature 1	Feature 2	Feature 3	Feature 4	Feature 5
    # 0	           x₁₁	       x₁₂	        x₁₃	        x₁₄	        x₁₅
    # 1	           x₂₁	       x₂₂	        x₂₃	        x₂₄	        x₂₅
    # ...	...	...	...	...	...
    # 10	       x₁₀₁       x₁₀₂          x₁₀₃          x₁₀₄       x₁₀₅ 

    # Ensure numerical stability by clipping values to avoid log(0)
    epsilon = 1e-8
    Prob_clipped = np.clip(Prob, epsilon, 1-epsilon)

    # Calculate the cross-entropy loss
    loss = (-1/m) * np.sum(correct * np.log(Prob_clipped) + (1 - correct) * np.log(1 - Prob_clipped))
    
    return loss

             # =======================================================  PROGRAM STARTS HERE ================================================

inputs = np.random.randn(10, 5)  # 10 examples, 5 features
correct_labels = np.random.randint(0, 2, size=(10, 1)) # Creates an array, starting from 0 (inclusive) to 2 (exclusive) so it can only be 0 or 1
# The size ensures that we get a column vector with 10 entries
number_of_features = inputs.shape[1] # This will give us 5, as each input as five shapes → inputs is (10,5) 

# Initialize weights and bias randomly
W = np.random.randn(number_of_features, 1) * 0.01
b = 0.0

# Perform the forward pass
FP = forward_pass(inputs, W, b)

# Compute the loss, compare the forward pass result with the labels
Final_loss = loss_function(FP, correct_labels)

print(f"Correct labels: {correct_labels.flatten()}") # .flatten() turns it to a 1D array for easy viewing
print(f"Initial Predicted Probabilities : {np.round(FP.flatten(), 3)}") # np.round rounds it to 3 dec places
print(f"Initial Average Loss: {Final_loss:.3f}")