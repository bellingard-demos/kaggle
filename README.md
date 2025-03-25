# kaggle


We estimate that the website contains approximately 1 million notebook or script, which are divided between Python and R programming languages.

Additionally, there is an API available [Kaggle API](https://www.kaggle.com/docs/api).

## Example

Let us take an example to see how the data looks.

First, this code will retrieve the top 5 Python kernels with the highest vote count. Then, we print the elements in the first one.

```python
import kaggle
ls = kaggle.api.kernels_list(language="python", page_size=5, sort_by="voteCount")
print(vars(ls[0]))
```

The output:

```json
{
   "languageNullable":"None",
   "kernelTypeNullable":"None",
   "isPrivateNullable":"None",
   "enableGpuNullable":"None",
   "enableTpuNullable":"None",
   "enableInternetNullable":"None",
   "id":0,
   "ref":"pmarcelino/comprehensive-data-exploration-with-python",
   "title":"Comprehensive data exploration with Python",
   "author":"Pedro Marcelino, PhD",
   "slug":"",
   "lastRunTime":datetime.datetime(2022, 4, 30, 19, 20, 37),
   "language":"",
   "hasLanguage":false,
   "kernelType":"",
   "hasKernelType":false,
   "isPrivate":false,
   "hasIsPrivate":false,
   "enableGpu":false,
   "hasEnableGpu":false,
   "enableTpu":false,
   "hasEnableTpu":false,
   "enableInternet":false,
   "hasEnableInternet":false,
   "categoryIds":[],
   "datasetDataSources":[],
   "kernelDataSources":[],
   "competitionDataSources":[],
   "modelDataSources":[],
   "totalVotes":13913
}
```

The most important information at the moment is the 'ref' which corresponds to the user_name/title ('pmarcelino/comprehensive-data-exploration-with-python').

To download this kernel:

```python
kernel_ref = vars(ls[0])["ref"]
kaggle.api.kernels_pull(kernel_ref, "notebooks/" + kernel_ref, metadata=True)
```
This code will download the kernel to the directory notebooks/user_name/title. The downloaded files will be either a notebook '.ipynb' or a Python script '.py'.
Additionally, there is the kernel-metadata.json, which looks like this:

```json
{
  "id": "pmarcelino/comprehensive-data-exploration-with-python",
  "id_no": 186062,
  "title": "Comprehensive data exploration with Python",
  "code_file": "comprehensive-data-exploration-with-python.ipynb",
  "language": "python",
  "kernel_type": "notebook",
  "is_private": false,
  "enable_gpu": false,
  "enable_tpu": false,
  "enable_internet": false,
  "keywords": [
    "exploratory data analysis",
    "data cleaning",
    "beginner",
    "matplotlib",
    "numpy",
    "pandas",
    "scipy",
    "seaborn"
  ],
  "dataset_sources": [],
  "kernel_sources": [],
  "competition_sources": [
    "house-prices-advanced-regression-techniques"
  ],
  "model_sources": []
}
```

## Scenarios

The API is limited to pulling 11 pages with 100 codes on each page (totaling 1100 codes). Browsing the code online can yield up to 105 pages with 20 codes on each page (totaling 2100 codes).

To acquire more data, we can explore different scenarios:

1. Download the kernels (code) when the language is set to 'python' and try all possible 'sortby' options.
```
sortby = ['hotness', 'commentCount', 'dateCreated', 'dateRun', 'relevance', 'scoreAscending', 'scoreDescending', 'viewCount', 'voteCount']
```
2. Download all the datasets, then fetch all the 'python' kernels that are associated with each dataset.
3. Retrieve all the usernames from the downloaded kernels, then download all the 'python' kernels related to each user."
