### Problem statement
Throughout this project we will use Collaborative filtering to predict the ratings that a user might give to a certain item based on the Amazon’s rating data set. This Project is built using the [Surprise](http://surpriselib.com/) recommendation library  

### Dataset
About:
The dataset  is the actual ratings given to Amazon clothing,  shoes, and jewelry category. It has a set of users and items and the ratings given by those users to some items.  Our model will try to minimize the error between predicted ratings and actual ratings. 

Download:
* Download the dataset from the following link and place it in the same directory of the project.
* Extract the file and make sure it has the following name:"Clothing_Shoes_and_Jewelry_5.json"
* Download the dataset from the direct link [here](snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Clothing_Shoes_and_Jewelry_5.json.gz)

### Project structure
Code files:
* `UserDefinedAlgorithm.py`: Implementation of the benchmark algorithm that is used in the project. Place it on the same project directory
* `cf_recommendation_clothing_dataset.ipynb`: Jupyter notebook that has the actual implementation of the project

Other files:
* `proposal.pdf`: The proposal that was previously accepted for this project
* `report.pdf`: The report of the project
* `cf_recommendation_clothing_dataset.html`: The HTML version of the exectuted notebook

### Libraries Needed
Surprise:
* Surpise is an open source collaborative filtering library
* Install it as follows:
	* $ git clone https://github.com/NicolasHug/surprise.git
		$ python setup.py install
	* Important: DO NOT install using pip. The pip version is not the latest version and the project is using functionalities available in latest version only


Libraries:
* pandas
* Numpy
* matplotlib
* seaborn
* sklearn
* pickle
* Surprise (See below section of instruction on how to install it)


