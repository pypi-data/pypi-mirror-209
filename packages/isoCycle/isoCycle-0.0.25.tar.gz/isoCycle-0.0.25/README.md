# isoCycle
#### A Deep Network-Based Decoder for Isolating Single Cycles of Neural Oscillations in Spiking Activity

<p align="justify">
Neural oscillations are prominent features of neuronal population activity in the brain, manifesting in various forms such as frequency-specific power changes in electroencephalograms (EEG) and local field potentials (LFP), as well as phase locking between different brain regions, modulated by modes of activity. Despite the intrinsic relation between neural oscillations and the spiking activity of single neurons, identification of oscillations has predominantly relied on indirect measures of neural activity like EEG or LFP, overlooking direct exploration of oscillatory patterns in the spiking activity, which serve as the currency for information processing and information transfer in neural systems. Recent advancements in densely recording large number of neurons within a local network have enabled direct evaluation of changes in network activity over time by examining population spike count variations across different time scales. Here we leverage the power of deep neural networks to robustly isolate single cycles of neural oscillations from the spiking of densely recorded populations of neurons. isoCycle effectively identifies individual cycles in the temporal domain, where cycles from different time scales may have been combined in various ways to shape spiking probability. The reliable identification of single cycle of neural oscillations in spiking activity across various time scales will deepen our understanding about the dynamics of neural activity.
</p>

## Demo Jupyter Notebook
<p align="justify">
isoCycle_example.ipynb demonstrates the code used to extract gamma and beta cycles, as well as slower cycles, from the spiking activity of 131 neurons simultaneously recorded in mouse V1 during visual stimulation.</p>

Run the demo on google colab
<a class="new-tab-link" href="https://colab.research.google.com/github/esiabri/isoCycle/blob/main/isoCycle_example_Colab.ipynb" target="_blank" style="pointer-events: none;">
  <img alt="https://colab.research.google.com/assets/colab-badge.svg" src="https://colab.research.google.com/assets/colab-badge.svg" align="center" style="pointer-events: auto;" />
</a>
<br>or run it on your machine after installing the package [isoCycle_example.ipynb](https://github.com/esiabri/isoCycle/blob/main/isoCycle_example.ipynb).

## Extract the Cycles in your Spiking data on Google Colab
<a class="new-tab-link" href="https://colab.research.google.com/github/esiabri/isoCycle/blob/main/isoCycle_yourData_Colab.ipynb" target="_blank" style="pointer-events: none;">
  <img alt="https://colab.research.google.com/assets/colab-badge.svg" src="https://colab.research.google.com/assets/colab-badge.svg" align="center" style="pointer-events: auto;" />
</a>
<br>Here, you can utilize isoCycle on Google Colab to analyze your data. Simply provide the recorded spike times, and isoCycle will extract the times of the cycle you choose (e.g. gamma, theta, etc). If you use kilosort/phy for spike sorting here is an m file that generates, spikeTimes.pkl, the input for isoCycle.  
    
## Installation

If you are comfortable with python, you can pip install in your environment of choice:

```buildoutcfg
pip install isoCycle
```

Here are the detailed steps for installation from scratch using Anaconda:

1. First, ensure that you have Anaconda installed on your computer. If you don't have Anaconda, you can download it from the official Anaconda [website](https://www.anaconda.com/downloads). Anaconda is a popular distribution of Python that comes with many pre-installed packages and a package manager called conda, making it convenient for data analysis and scientific computing tasks.

2. Once you have Anaconda installed, open a terminal or command prompt on your computer, and create a new conda environment by executing the following command:
```buildoutcfg
conda create --name myenv
```
Replace myenv with the desired name for your environment.

3. Activate the newly created environment with the following command:
```buildoutcfg
conda activate myenv
```
Again, replace myenv with the name of your environment.

4. Install isoCycle and its dependencies by running the command:
```buildoutcfg
pip install isoCycle
```
5. After the installation is complete, you can import isoCycle into your Python scripts or notebooks using the statement
```buildoutcfg
import isoCycle
```

Now, with Anaconda installed, a new environment created, and isoCycle successfully installed, you are ready to analyze your data using isoCycle. You can use [Jupyter Notebook](https://jupyter.org/try-jupyter/retro/notebooks/?path=notebooks/Intro.ipynb) to import and use isoCycle, check the [isoCycle_example.ipynb](https://github.com/esiabri/isoCycle/blob/main/isoCycle_example.ipynb) provided in this package.
