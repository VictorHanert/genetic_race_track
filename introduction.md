# AI Configuration Guide

The `config-feedforward.txt` file contains all the AI settings for `main.py`. If you want to adjust the AI behavior, you can modify this file.

This file is used by the NEAT (NeuroEvolution of Augmenting Topologies) library to configure the neural network and evolutionary algorithm. These settings define how the neural networks are initialized, mutated, and evolved, as well as how the population of genomes is managed.

## [NEAT] Section
- **fitness_criterion**: Determines how fitness is evaluated across the population (`max`, `min`, or `mean`).
- **fitness_threshold**: The fitness value required to stop the evolution process.
- **pop_size**: The number of genomes in each generation.
- **reset_on_extinction**: If `True`, resets the population when all genomes fail.

## [DefaultGenome] Section
Defines the structure and mutation behavior of the neural networks:
- **activation_default**: Default activation function for nodes (e.g., `tanh`, `relu`).
- **activation_mutate_rate**: Probability of changing the activation function of a node.
- **activation_options**: List of possible activation functions. (e.g., `tanh`, `relu`, `sigmoid`).

- **aggregation_default**: Default aggregation function for nodes (e.g., `sum`, `product`).
- **aggregation_mutate_rate**: Probability of changing the aggregation function of a node.
- **aggregation_options**: List of possible aggregation functions. (e.g., `sum`, `product`).

- **bias_init_mean**: Initial mean value for node biases.
- **bias_init_stdev**: Initial standard deviation for node biases.
- **bias_max_value**: Maximum value for node biases.
- **bias_min_value**: Minimum value for node biases.
- **bias_mutate_power**: Maximum change in bias during mutation.
- **bias_mutate_rate**: Probability of mutating a node's bias.
- **bias_replace_rate**: Probability of replacing a node's bias with a new random value.

- **compatibility_disjoint_coefficient**: Coefficient for disjoint genes in the compatibility distance calculation.
- **compatibility_weight_coefficient**: Coefficient for excess genes in the compatibility distance calculation.

- **conn_add_prob**: Probability of adding a new connection between nodes.
- **conn_delete_prob**: Probability of deleting an existing connection.

- **enabled_default**: 
- **enabled_mutate_rate**:

- **feed_forward**: If `True`, the genome is a feed-forward network.
- **initial_connection**: Determines how nodes are initially connected (`full`, `partial`)

- **node_add_prob**: Probability of adding a new node to the network during mutation.
- **node_delete_prob**: Probability of removing an existing node from the network during mutation.

- **num_hidden**: Number of hidden nodes in the neural network.
- **num_inputs**: Number of input nodes in the neural network (e.g., sensor data).
- **num_outputs**: Number of output nodes (e.g., steering and acceleration).

- **response_init_mean**: Initial mean value for node response parameters.
- **response_init_stdev**: Initial standard deviation for node response parameters.
- **response_max_value**: Maximum allowable value for node responses.
- **response_min_value**: Minimum allowable value for node responses.
- **response_mutate_power**: Maximum change in node response during mutation.
- **response_mutate_rate**: Probability of mutating a node's response.
- **response_replace_rate**: Probability of replacing a node's response with a new random value.

- **weight_init_mean**: Initial mean value for connection weights.
- **weight_init_stdev**: Initial standard deviation for connection weights.
- **weight_max_value**: Maximum allowable value for connection weights.
- **weight_min_value**: Minimum allowable value for connection weights.
- **weight_mutate_power**: Maximum change in connection weight during mutation.
- **weight_mutate_rate**: Probability of mutating a connection weight.
- **weight_replace_rate**: Probability of replacing a connection weight with a new random value.

## [DefaultSpeciesSet] Section
- **compatibility_threshold**: Determines how genomes are grouped into species. Lower values create more species.

## [DefaultStagnation] Section
- **species_fitness_func**: Function used to evaluate the fitness of species.
- **max_stagnation**: Maximum number of generations a species can go without improvement before being removed.
- **species_elitism**: Number of top-performing species preserved each generation.

## [DefaultReproduction] Section
- **elitism**: Number of top genomes preserved each generation without mutation.
- **survival_threshold**: Proportion of genomes allowed to reproduce.