def generalize_hypothesis(hypothesis, sample):
    """Generalize the hypothesis minimally so that it becomes consistent with the sample."""
    for i in range(len(hypothesis)):
        if hypothesis[i] != sample[i]:
            hypothesis[i] = '?'
    return hypothesis


def specialize_hypothesis(general_hypotheses, sample, domain):
    """Specialize the general hypotheses minimally so that they exclude the sample."""
    new_general_hypotheses = []
    for hypothesis in general_hypotheses:
        for i in range(len(hypothesis)):
            if hypothesis[i] == '?':
                for value in domain[i]:
                    if sample[i] != value:
                        new_hypothesis = hypothesis.copy()
                        new_hypothesis[i] = value
                        new_general_hypotheses.append(new_hypothesis)
            elif hypothesis[i] != sample[i]:
                new_general_hypotheses.append(hypothesis)
                break
    return new_general_hypotheses


def candidate_elimination(examples):
    """Perform the Candidate Elimination Algorithm on the given examples."""
    # Initialize S and G
    S = [['ϕ', 'ϕ', 'ϕ']]
    G = [['?', '?', '?']]

    # Define the domain of each attribute to help with specialization
    domain = [['Big', 'Small'], ['Red', 'Blue'], ['Circle', 'Triangle']]

    for sample in examples:
        if sample[-1] == 'Yes':  # If the example is positive
            G = [g for g in G if all([s == '?' or s == g[i]
                                     for i, s in enumerate(sample[:-1])])]
            if S[0][0] == 'ϕ':  # First positive example
                S = [sample[:-1]]
            else:
                S = [generalize_hypothesis(S[0], sample[:-1])]
        else:  # If the example is negative
            S = [s for s in S if not all(
                [s[i] == '?' or s[i] == sample[i] for i in range(len(s))])]
            G = specialize_hypothesis(G, sample[:-1], domain)

    return S, G


# Define the examples
examples = [
    ['Big', 'Red', 'Circle', 'No'],
    ['Small', 'Red', 'Triangle', 'No'],
    ['Small', 'Red', 'Circle', 'Yes'],
    ['Big', 'Blue', 'Circle', 'No']
]

S_final, G_final = candidate_elimination(examples)

print("Final Specific Hypothesis (S):", S_final)
print("Final General Hypotheses (G):", G_final)
