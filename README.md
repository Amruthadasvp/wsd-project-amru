# Word sense disambiguation using GlossBert
NLP Framework for word sense disambiguation in English and Spanish using the GlossBert approach implemented in Pytorch.
https://arxiv.org/abs/1908.07245
Project specifics can be viewed in those [slides](https://bit.ly/2mL0fo9)


## Project format:
- **source** : source code for training, test and data preprocessing
- **notebooks** : notebooks demonstrating the approach
- **streamlit** : Demo Streamlit app for WSD sense inference in English
- **data** : folders for raw processed and preprocessed data
 <!---
- **tests** : Put all source code for testing in an easy to find location
-  **configs** : Enable modification of all preset variables within single directory (consisting of one or many config files for separate tasks)
- **data** : Include example a small amount of data in the Github repository so tests can be run to validate installation
- **build** : Include scripts that automate building of a standalone environment
- **static** : Any images or content to include in the README or web framework if part of the pipeline -->

## Setup
Clone repository and update python path

#### Installation
create a new environment ,in conda:

```
conda create -n <your env name>
source activate <your env name>
```

Cd into the repo directory and get into development branch
```
pip install --ignore-installed -r requirements.txt
```
#### Training

The training uses the following datasets:
- English Train corpus: Semcor 3.0 
- English Test corpus: Senseval 2007 task 13
- Wordnet 3.0 sense dictionary

#### Getting the Data
To download and preprocess files run:
```
bash get_gen_dataset.sh
```  

#### Initiating the training

You'll see a list of .feather files for test and train data in the ./data/preprocessed folder. 
In order to initiate the training cd into the source directory and run (The data processing for semcor/senseval
will take a while ~30min):
```
python run_training.py \
     --data_path=../data/preprocessed/semcor_gloss.pkl \
     --test_data_path=../data/preprocessed/senseval_gloss.pkl \
     --default_save_path=../data \
     --weak_supervision=True \
     --preprocess_inputs=True \
     --token_layer='sent-cls-ws' \
     --batch_size=16 \
     --val_check_interval=0.05 \
     --model_type='bert-base-uncased' \
     --lr=2e-5 \
     --weight_decay=0.01 \
     --epochs=4

```

The progression of the training can be seen in tensorboard.

```
tensorboard --logdir=../data/lighnting_logs 
```

#### Visualizing the results in the Streamlit app

For inference go to the streamlit directory and run:

```
streamlit run run_inference.py --model_dir=<Your_model_dir>

```
the default model location is in ./data/lightning_logs/version_#/

## Requisites

#### Main Dependencies

- Pytorch
- tensorflow/keras (For tensor padding) 
- Pytorch-lightning
- TensorboardX (Included in pytorch lighning)
- [Streamlit](streamlit.io)


<!--
#### Installation
To install the package above, pleae run:
```shell
pip install -r requiremnts
```


## Build Environment
- Include instructions of how to launch scripts in the build subfolder
- Build scripts can include shell scripts or python setup.py files
- The purpose of these scripts is to build a standalone environment, for running the code in this repository
- The environment can be for local use, or for use in a cloud environment
- If using for a cloud environment, commands could include CLI tools from a cloud provider (i.e. gsutil from Google Cloud Platform)
```
# Example

# Step 1
# Step 2
```

## Configs
- We recommond using either .yaml or .txt for your config files, not .json
- **DO NOT STORE CREDENTIALS IN THE CONFIG DIRECTORY!!**
- If credentials are needed, use environment variables or HashiCorp's [Vault](https://www.vaultproject.io/)


## Test
- Include instructions for how to run all tests after the software is installed
```
# Example

# Step 1
# Step 2
```

## Run Inference
- Include instructions on how to run inference
- i.e. image classification on a single image for a CNN deep learning project
```
# Example

# Step 1
# Step 2
```

## Build Model
- Include instructions of how to build the model
- This can be done either locally or on the cloud
```
# Example

# Step 1
# Step 2
```

## Serve Model
- Include instructions of how to set up a REST or RPC endpoint
- This is for running remote inference via a custom model
```
# Example

# Step 1
# Step 2
```

## Analysis
- Include some form of EDA (exploratory data analysis)
- And/or include benchmarking of the model and results
```
# Example

# Step 1
# Step 2
```

-->


