# **Skillcraft Dataset Analysis**

This project was developed for the 'Machine Learning' (APA) course at FIB in 2021-22 Q1. The analysis is based on data taken from Starcraft 2 players which can be found at [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/skillcraft1+master+table+dataset)

**Authors:**

David Nogales Pérez

Alex Ochoa Blasco

## **Main script**

The analysis of the dataset can be found in the `.ipynb` notebook file.

## **Installation**

---------------
For running the Notebook you will have to install a Jupyter Notebook enviroment, which comes with `Anaconda` or `VSCode`, alternatively you could upload it directly to [Google Colab](https://colab.research.google.com).

In the python notebook uncomment the first command line which is:

```python
  > !pip install -r requirements.txt
```

to install the necessary dependencies from the `requirements.txt` file. Alternatively you can do this before in the console by typing the same command without the exclamation sign:

```powershell
  > pip install -r requirements.txt
```

If you will be running the notebook in [Google Colab](https://colab.research.google.com) you will have to upload the `requirements.txt` file as well.

## **Usage**

---------------

In windows first execute the `dataset_downloader.py` script:

```powershell
> python.exe .\dataset_downloader.py 
```

Which will download the dataset in the current directory if it isn't present already. Or you can download the dataset manually from this [dataset repository](http://archive.ics.uci.edu/ml/datasets/skillcraft1+master+table+dataset).

Alternatively the Jupyter Notebook will check the presence of the dataset and will download it in its enviroment if necessary. Lastly execute the `.ipynb` file in your enviroment of choice by running all cells.
