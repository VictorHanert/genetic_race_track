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
- **num_inputs**: Number of input nodes in the neural network (e.g., sensor data).
- **num_outputs**: Number of output nodes (e.g., steering and acceleration).
- **activation_default**: Default activation function for nodes (e.g., `tanh`, `relu`).
- **bias_mutate_rate**: Probability of mutating a node's bias.
- **weight_mutate_rate**: Probability of mutating a connection's weight.
- **initial_connection**: Determines how nodes are initially connected (`full`, `partial`, etc.).

## [DefaultSpeciesSet] Section
- **compatibility_threshold**: Determines how genomes are grouped into species. Lower values create more species.

## [DefaultStagnation] Section
- **max_stagnation**: Maximum number of generations a species can go without improvement before being removed.
- **species_elitism**: Number of top-performing species preserved each generation.

## [DefaultReproduction] Section
- **elitism**: Number of top genomes preserved each generation without mutation.
- **survival_threshold**: Proportion of genomes allowed to reproduce.

## Tips for Adjusting Parameters
- **Increasing `pop_size`**: Improves diversity but increases computation time.
- **Lowering `compatibility_threshold`**: Creates more species, which can help preserve diversity.
- **Adjusting mutation rates**: Higher rates encourage exploration, while lower rates focus on refinement.
- **Changing `fitness_threshold`**: Use a realistic value based on your problem's requirements.

By tweaking these parameters, you can fine-tune the AI's learning process to better suit your specific application.