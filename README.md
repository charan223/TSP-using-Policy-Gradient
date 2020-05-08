# TSP-using-Policy-Gradient

## Instructions to run

To run TSP using policy gradient,

```python Neural_Reinforce.py```

To entropy regularization experiments,

```python Entropy_Reinforce.py```

To run using 2-opt heuristic baseline,
```python Heuristic_Reinforce.py```

## Plots

![Reward graph for entropy regularization TSP20 experiment](plots/plot_entropy_20.png)

![Reward graph for heuristic baseline TSP20 experiment](plots/plot_heuristic_20.png)



## References

We took the boilerplate code from [here](https://github.com/MichelDeudon/encode-attend-navigate)

@inproceedings{Deudon2018LearningHF,
  title={Learning Heuristics for the TSP by Policy Gradient},
  author={Michel Deudon and Pierre Cournut and Alexandre Lacoste and Yossiri Adulyasak and Louis-Martin Rousseau},
  booktitle={CPAIOR},
  year={2018}
}
