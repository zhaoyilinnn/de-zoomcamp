import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    non_zero_passengers_df = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
        
    def camel_to_snake(camel_case_string):
        snake_case_string = ""
        for i, c in enumerate(camel_case_string):
            if i == 0:
                snake_case_string += c.lower()
            elif c.isupper():
                snake_case_string += "_" + c.lower()
            else:
                snake_case_string += c
        return snake_case_string
    new_lt = []

    for i in list(non_zero_passengers_df.columns):
        i = i.replace('ID', 'Id')
        i = camel_to_snake(i)
        new_lt.append(i)
    print([i for i in new_lt if i not in list(non_zero_passengers_df.columns)])
    non_zero_passengers_df.columns = new_lt

    print(non_zero_passengers_df['vendor_id'].unique())
    return non_zero_passengers_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output[output['passenger_count'] ==0].shape[0] == 0 #'There are rides with zero passengers'
    assert ('vendor_id' in list(output.columns))
    assert output[output['trip_distance'] == 0].shape[0] == 0