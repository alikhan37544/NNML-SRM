def find_s(data):
    # Initialize the most specific hypothesis
    hypothesis = ['0', '0', '0']

    # Loop through the data
    for sample in data:
        # If the sample is positive (has pneumonia)
        if sample[-1] == 'Pneumonia':
            # Ignore the last column which is the disease
            for i, feature in enumerate(sample[:-1]):
                # If this is the first positive example, initialize the hypothesis
                if hypothesis[i] == '0':
                    hypothesis[i] = feature
                # If the feature disagrees with the hypothesis, generalize it
                elif hypothesis[i] != feature:
                    hypothesis[i] = '?'
    return hypothesis


# Each sample is a list: [Fever, Cough, Difficulty Breathing, Diagnosed Disease]
data = [
    ['Yes', 'Yes', 'No', 'Pneumonia'],
    ['No', 'Yes', 'No', 'Common Cold'],
    ['Yes', 'Yes', 'Yes', 'Pneumonia'],
    ['No', 'No', 'No', 'Healthy'],
    ['Yes', 'Yes', 'Yes', 'Pneumonia']
]

# Apply the Find-S algorithm
hypothesis = find_s(data)

print("Final Hypothesis:", hypothesis)
