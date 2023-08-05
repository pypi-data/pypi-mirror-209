from doc_functions import render_documentation

import pandas as pd

def train_multiple_reg_models(train_df: pd.DataFrame, test_df: pd.DataFrame, labelCol: str, inputCols: list, evaluator, cv: bool, algorithms: list) -> dict:
    """Train multiple regression models
    
    Trains multiple regression models using given train dataframe and evaluates trained models using a given test dataframe.
    Capable of training multiple Linear Regression models at once. Can also be used to train a single model as well.
    
    Args:
        train_df: Dataframe to be used to train the model(s). Should include columns included in inputCols and labelCol parameters.
        test_df: Dataframe to be used to evaluate the model(s). Should include columns included in inputCols and labelCol parameters.
        labelCol: Name of the column in train and test dataframe that contains the labels.
        inputCols: List of the names of feature columns.
        evaluator: What kind of evaluator to be used for the models.
        cv: Whether to perform Cross-Validation or not
        algorithms: Names of algorithms as a list. Currently supports ['GBT', 'GLR', 'LinReg']. Should always be a list, even if only one algorithm should be used.
        
    Returns:
        A dictionary containing following objects for each model that was mentioned in algorithms parameter when the function was executed:
            - Fully trained pipeline: Includes preprocessing transformers as well as the regression model.
            - Transformed train dataframe
            - Transformed test dataframe
            - Cross-Validation results
        Each of these objects are accessible via keys in the return dictionary. The key consists of the object name followed by the lowercase of the algorithm.
        For example: trained pipeline of the GBT can be accessed as follows:
            return_dict['trained_pipeline_gbt']
            
    Examples:
        The following example focuses on training a GBT model.
        >>> train_models(train_dataframe, 
            test_dataframe, 
            labelCol='Label', 
            inputCols=['feature1', 'feature2'],
            evaluator=<SOME_EVALUATOR_HERE>,
            cv=True,
            algorithms=['GBT'])
        {
        'output': bg
        }

    Raises:
        AttributeError: When invalid attributes are called in the function.
        ValueError: When invalid values are passed to the function.
    """
    
    return {}

def feature_importance(pipeline: pd.DataFrame, dataframe: pd.DataFrame, input_cols: list, n_samples: int = 5, bg_data_limit: int = None) -> pd.DataFrame:
    """Calculate feature importance

    Calculates feature importance for each feature in a dataset that is used to predict a label column.
    Requires a model trained from the same features and uses the same label column as its target.
    Copatible with PySpark Pipelines that contain preprocesing transformers like OneHotEncoder, StringIndexer, and VectorAssembler.
    Feature importances are calculated by taking the average of feature importance for each feature values calculated for each sample used.
    Returns and displays raw feature importances (not absolute values) and their percentage of feature importance (calculated from absolute values).
    Generates a bar plot to visualize the feature importance percentages(calculated from absolute values).

    Args:
        pipeline: A PySpark pipeline that contains the trained model and the preprocessing transformers. Should be a trained pipeline.
        dataframe: A PySpark dataframe that contains data similar to the data that was used to train the pipeline. Should include all features mentioned in input_cols
        input_cols: List of features that were used to train the model. Importances of these features  will be calculated in this function. Do not inlcude the Label column in this list.
        n_samples: Number of samples used as explain instances. Optional. Defaulted to 5.
        bg_data_limit: Number of rows that will be used in the background data in feature importance calculation. Should be either None or an integer. Optional. Defaulted to None.
                        If None, the entire dataframe given in the dataframe paramter will be used.
                        If int, the bg_data_limit should be equal to or less than the number of rows in the dataframe given in the dataframe parameter.

    Returns:
        Pandas DataFrame containing feature names, their importances, and feature importance percentages
    """

    return pd.DataFrame({})

def func():
    pass

print(globals())

html = render_documentation(globals(), module_name="Test")

with open('D:\\Misc\\notebook-doc\\test.html', 'w') as f:
    f.write(html)