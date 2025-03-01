# Exploratory Data Analysis (EDA)

<!-- MarkdownTOC levels=1,2,3 -->

- Summary Statistics
    - Statistical Distribution
    - Anomalies
- Exploratory Data Analysis
- Essential Code Blocks
    - Distribution
    - Summary statistics of numerical features
    - Summary statistics of categorical features
    - Plot of numeric features
    - Plot of categorical features
    - Grouping and segmentation
    - Relationships between numeric features
- How to Identify Outliers?
    - Extreme Value Analysis
    - Proximity Methods
    - Projection Methods
    - Methods Robust to Outliers
- References

<!-- /MarkdownTOC -->


## Summary Statistics

It is important to know how to extract information from descriptive statistics.

```py
    # get the data info
    df.info()    

    # inspect the data 
    df.head()

    # summary stats
    df.describe() 

    # include string and categorical features
    df.describe(include=['int', 'float', 'object', 'category'])
```

### Statistical Distribution

#### Mean

With the mean value, you are trying to get a sense of what an average data point looks like. 

#### Standard Deviation

Standard deviation is a measure of variation/dispersion of data points with respect to the mean.

Smaller STD indicates that the data are mostly centered around the mean whereas a higher STD value indicates the data points are rather dispersed.

#### Median (50%)

The 50th percentile (the 50% column) is also known as the median. Like mean, it’s another measure of central tendency.

Median is a preferred metric rather than mean if there are outliers or high variability in the data.

If the difference between mean and median is _small_, you can infer that the data is symmetrically distributed.

If the median is higher than the mean, data is likely _left-skewed_ in distribution.

#### Min and Max

Min and max values represent the lower and upper limit of a variable in the dataset.


### Anomalies

You can get a sense of outliers, anomalies, and other points of interest in the dataset using descriptive statistics.

#### Outliers

A large difference between the 75th percentile and the maximum value indicates the presence of potential outliers.

Likewise, a large difference between the minimum value and the 25th percentile indicates the presence of potential outliers.

To confirm outliers you can create a boxplot for visual inspection:

```py
    sns.boxplot(y=df['total_bill']);
```

#### Red flags

Sometimes descriptive statistics can raise red flags.

Places with unexpected minimum values (0 or negative) or absolutely unacceptible maximum values (such as someone’s age 120 years!).

These are obvious indications that there are issues in the data and need further investigation.



## Exploratory Data Analysis

Exploratory Data Analysis (EDA) is one of the first steps of the data science process which involves learning as much as possible about the data without spending too much time. 

We can get an instinctive as well as a high-level practical understanding of the data including a general idea of the structure of the data set, some cleaning ideas, the target variable and possible modeling techniques.

We can the summary statistics and create histograms for the numeric variables of the dataset as presented in the code below.

Things we can do:

- Study the relationship between satisfaction and class category.
- Investigate the relationship between total delay time, overall rating, and satisfaction. 
- Check if age is affecting the satisfaction of customers. 

```py
    # check the shape of the dataframe
    df.shape
        
    # check data types
    df.dtypes

    df.size
    
    # summary statistics
    df.describe()
    
    # get column list
    df.columns.tolist()
        
    # number of missing values in each column
    df.isna().sum()
    
    # Find and verify missing values
    np.where(pd.isnull(df))
    df.iloc[296, 12]

    # replace missing values
    df.replace(np.nan, 0)
    
    # count of unique values
    df.nunique()
    
    # check for duplicate values
    df.duplicated()

    # Remove duplicates
    df.drop_duplicates(subset=['PersonId', 'RecordDate'], keep='last')

    # Drop duplicate column
    df_X.drop(['TEST1', 'TEST2'], axis=1)

    
    # check the distribution of categorical columns
    df["product_group"].value_counts()
    
    # find percent share of each value by using the normalize parameter
    df["product_group"].value_counts(normalize=True)
    
    # check the average price of products for each product group 
    df.groupby("product_group", as_index=False).agg(  
        avg_price = ("price","mean")
    )
    
    # change null to 0 
    df5.loc[df5['column1'].isnull(),   'column1'] = 0
    
    # change nan to 0 
    df['column1'] = df['column1'].fillna(0)

    # change column data type
    df[['age', 'weight']] = df[['age', 'weight']].astype(float)
    
    # drop rows where all columns are missing/ NaN
    df.dropna(axis=0, how="any", inplace=True)
        
    
    # Set New Column Value Based on Multiple Criteria
    # Use bitwise operators instead of AND and OR
    df.loc[(df.AvgProduction> 1000000) & (df.Age > 5), 'Category'] = 'Priority 1'
    
    
    # Check For Missing Timestamps or Rows
    time_range = pd.date_range(startdate , enddate, freq='1min')
    ts =   pd.DataFrame(time_range)
    ts.rename(columns = {ts.columns[0]:'timestamp'}, inplace = True)
    ## now complete a merge to join the sets together
    
    
    # Filter Data Based on String Match
    df1 = df[df[‘Flag’].str.contains(“CHECK ME NOW”)]
    
    # Aggregate across columns
    df['StateAverage'] = df_mo[['school1', 'school2','school3', 'school4']].mean(axis=1)

    
    pd.DataFrame({"values":{col:df[col].unique() for col in df},
              'type':{col:df[col].dtype for col in df},
              'unique values':{col:len(df[col].unique()) for col in df},
              'NA values':{col:str(round(sum(df[col].isna())/len(df),2))+'%' for col in df},
              'Duplicated Values':{col:sum(df[col].duplicated()) for col in df}
    })
```

```py
    numeric_variables = list(df.select_dtypes(include=['int64', 'float64'])) #select the numeric variables

    df[numeric_variables].describe().apply(lambda x:round(x,2)).T #apply describe method

    # create the histograms
    histograms = df[numeric_variables].hist(bins =10, 
        xlabelsize=10, 
        ylabelsize=10, 
        grid=False, 
        sharey= True, 
        figsize = (15,15)) 
```

```py
    # numerical features
    df.describe()

    # include string and categorical features
    df.describe(include=['int', 'float', 'object', 'category'])
    # unique = number of unique categories
    # top = dominant category
    # freq = count of dominant category
``` 



## Essential Code Blocks

1. Shape (dimensions) of the DataFrame
2. Data types of the various columns
3. Display a few rows

We may observe that our dataset has a combination of categorical (object) and numeric (float and int) features.

What to look for:

- Can you understand the column names? Do they make sense? (Check the variable definitions if needed)
- Do the values in the columns make sense? Numeric features that should be categorical and vice versa.
- Are there significant missing values (NaN)?
- What types of classes do the categorical features have?

### Distribution

Distribution refers to how the values in a feature are distributed or how often they occur.

For numeric features, we see how many times groups of numbers appear in a particular column.

For categorical features, we view the classes for each column and their frequency.

We will use both graphs and actual summary statistics.

The graphs enable us to get an overall idea of the distributions while the statistics give us factual numbers.

Both graphs and statistics are recommended since they complement each other.

### Summary statistics of numerical features

```py
    print(df.describe())
    
    # count null values
    df.isnull().sum()
    
    # count of students whose physics marks are greater than 11
    df[df['Physics'] > 11]['Name'].count())
    
    # count students whose physics marks are greater than 10
    # and math marks are greater than 9.
    df[(df['Physics'] > 10 ) & (df['Math'] > 9)]
    
    # Multi-column frequency count
    count = df.groupby(col_name).count()
```

We can see for each numeric feature, the count of valueS, the mean value, std or standard deviation, minimum value, the 25th percentile, the 50th percentile or median, the 75th percentile, and the maximum value.

What to look for:

- Missing values: their count is not equal to the total number of rows of the dataset.
- Minimum or maximum values they do not make sense.
- Large range in values (min/max)

### Summary statistics of categorical features

```py
   df.describe(include=['category'])
```

### Plot of numeric features

```py
    df.hist(figsize=(14,14), xrot=45)
    plt.show()
```

What to look for:

- Possible outliers that cannot be explained or might be measurement errors. 
- Numeric features that should be categorical such as Gender represented by 1 and 0.
- Boundaries that do not make sense such as percentage values > 100.

### Plot of categorical features

```py
    for column in df.select_dtypes(include='object'):
        if df[column].nunique() < 10:
            sns.countplot(y=column, data=df)
    plt.show()
```

What to look out for:

- Sparse classes which have the potential to affect a model’s performance.
- Mistakes in labeling of the classes, for example 2 exact classes with minor spelling differences.


### Grouping and segmentation

Segmentation allows us to cut the data and observe the relationship between categorical and numeric features.

#### Segment the target variable by categorical features

Compare the _target_ feature (Price) between the various classes of our main categorical features (Type, Method, and Regionname) and see how the target changes with the classes.

```py
    # Plot boxplot of each categorical feature with Price.
    for column in data.select_dtypes(include=’object’):
        if data[column].nunique() < 10:
            sns.boxplot(y=column, x=’Price’, data=data)
    plt.show()
```

What to look for: Classes that most affect the target variable(s).


#### Group numeric features by each categorical feature

See how all the other numeric features (not just target feature) change with each categorical feature by summarizing the numeric features across the classes.

```py
    # For the 3 categorical features with less than 10 classes,
    # we group the data, then calculate the mean across the numeric features.
    for column in df.select_dtypes(include='object'):
        if df[column].nunique() < 10:
            display(df.groupby(column).mean())        
```


### Relationships between numeric features

#### Correlation matrix for numerical features

A _correlation_ is a value between -1 and 1 that amounts to how closely values of two separate features move simultaneously.

A _positive_ correlation means that as one feature increases the other one also increases while a _negative_ correlation means one feature increases as the other decreases.

Correlations close to 0 indicate a _weak_ relationship while closer to -1 or 1 signifies a _strong_ relationship.

```py
    corrs = df.corr()
    print(corrs)
```

This might not mean much now, so we can plot a **heatmap** to visualize the correlations.

#### Heatmap of the correlations

```py
    # Plot the grid as a rectangular color-coded matrix using seaborn heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corrs, cmap='RdBu_r', annot=True)
    plt.show()
```

What to look for:

- Strongly correlated features: either dark red (positive) or dark blue(negative).
- Target variable: If it has strong positive or negative relationship with other features.


----------



## How to Identify Outliers?

Many machine learning algorithms are sensitive to the range and distribution of the input data.

Outliers in input data can affect the training process of ML algorithms abd result in less accurate models.

### Extreme Value Analysis

Start with a simple extreme value analysis:

- Focus on univariate methods

- Visualize the data using scatterplots, histograms, and box and whisker plots to identify extreme values

- Assume a normal distribution (Gaussian) and look for values more than 2 or 3 standard deviations from the mean or 1.5 times from the first or third quartile

- Filter out outliers from training set and evaluate model performance

### Proximity Methods

Next, consider trying proximity-based methods:

- Use clustering methods to identify clusters in the data (such as k-Means and DBSCAN)

- Identify and mark the cluster centroids

- Identify data instances that are a fixed distance or percentage distance from the cluster centroids

- Filter out outliers from training set and evaluate model performance

### Projection Methods

Finally, projection methods can be used to  identify outliers:

- Use projection methods to summarize your data to two dimensions (such as PCA, MDS, and t-SNE)

- Visualize the mapping and identify outliers

- Use proximity measures from projected values or vectors to identify outliers

- Filter out outliers from training set and evaluate model performance

### Methods Robust to Outliers

An alternative approach is to try models that are robust to outliers. 

There are robust forms of regression that minimize the median least square errors rather than mean called robust regression but they are more computationally intensive. 

There are also models such as decision trees that are robust to outliers.

Spot check some methods that are robust to outliers to see if there is a significant improvement in model performance metrics.


## References

[Reading and interpreting summary statistics](https://towardsdatascience.com/reading-and-interpreting-summary-statistics-df34f4e69ba6)

[Python Cheat Sheet for Data Science](https://chipnetics.com/tutorials/python-cheat-sheet-for-data-science/)

[11 Essential Code Blocks for EDA Regression Task](https://towardsdatascience.com/11-simple-code-blocks-for-complete-exploratory-data-analysis-eda-67c2817f56cd)

[6 Pandas Functions for a Quick Exploratory Data Analysis](https://sonery.medium.com/6-pandas-functions-for-a-quick-exploratory-data-analysis-ff9ece0867d7)

[My Top 10 Pandas Functions for Preparing Data](https://betterprogramming.pub/my-top-10-pandas-functions-for-preparing-data-3ec7a1451a84)

[How to build a Machine Learning (ML) Predictive System](https://towardsdatascience.com/machine-learning-ml-based-predictive-system-to-predict-the-satisfaction-level-of-airlines-f0780dbdbc87?source=rss----7f60cf5620c9---4)


[How to Identify Outliers in your Data](https://machinelearningmastery.com/how-to-identify-outliers-in-your-data/)

[Detecting Outliers Using Python](https://towardsdatascience.com/detecting-outliers-using-python-66b25fc66e67)

[Huber and Ridge Regressions in Python: Dealing with Outliers](https://towardsdatascience.com/huber-and-ridge-regressions-in-python-dealing-with-outliers-dc4fc0ac32e4?gi=c292a23ceab7)

[Use k-medians clustering method if you have many outliers](https://towardsdatascience.com/use-this-clustering-method-if-you-have-many-outliers-5c99b4cd380d?gi=5c97a562ff04)

