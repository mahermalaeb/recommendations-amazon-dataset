Dataset:
	- Download the dataset from the following link and place it in the same directory of the project.
	- Extract the file and make sure it has the following name:"Clothing_Shoes_and_Jewelry_5.json"
	- Direct link to dataset: snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Clothing_Shoes_and_Jewelry_5.json.gz

Libraries:
	- pandas
	- Numpy
	- matplotlib
	- seaborn
	- sklearn
	- pickle
	- Surprise (See below section of instruction on how to install it)

Surprise:
	- Surpise is an open source collaborative filtering library
	- Install it as follows:
		$ git clone https://github.com/NicolasHug/surprise.git
		$ python setup.py install
	- Important: DO NOT install using pip. The pip version is not the latest version and the project is using functionalities available in latest version only

Code files:
	- `UserDefinedAlgorithm.py`: Implementation of the benchmark algorithm that is used in the project. Place it on the same project directory
	- `cf_recommendation_clothing_dataset.ipynb`: Jupyter notebook that has the actual implementation of the project

Other files:
	- `proposal.pdf`: The proposal that was previously accepted for this project
	- `report.pdf`: The report of the project
	- `cf_recommendation_clothing_dataset.html`: The HTML version of the exectuted notebook