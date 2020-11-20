# creating a function for saving an object to a file
def save_pickle (self, filename=None):
    ''' This function saves a variable in the .pickle format (abbreviated as .pkl).

    INPUT: - self = variable to save
    OUTPUT: - filename = desired string name for the saved object with no extension
    '''
    import os
    import numpy
    import pickle

    # making a pickles directory, if it does not exist
    try:
        if not os.path.exists('pickles'):
            os.mkdir('pickles')
    except:
        print("directory 'pickles' already exists")
        pass

    # instantiating the name for the saved file, with '.pkl' extension
    save_name = filename + '.pkl'

    print("-"*15, f"PICKLING {filename}", "-"*25)

    # serializing the file
    with open(f'pickles/{save_name}', 'wb') as f:
        pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
    print("Saved as ", save_name, "\n")


# creating a function to deserialize and instantiate objects
def read_pickle(filepath):
    ''' takes a string file(path) of a pickled file
    and returns its de - serialized object'

    INPUT:  - filepath = (str) path to file
    OUTPUT: - loaded variable (instantiate with "variable = read_pickle(filepath)")
    '''
    import os
    import numpy
    import pickle

    with open(filepath, 'rb') as f:
        variable_name = pickle.load(f)
    print(f"Object restored from {filepath}")
    return (variable_name)


def string_to_integer(df_cols):
    """ Converts string type columns to integers
    - INPUT:    dataframe column slice
                <df[["col"]]> for a single column, 
                or <df[list_cols]> for a list of columns.
    - OUTPUT: converte columns
    """
    print( "Converting...................")
    return df_cols.astype('int64')


def string_to_float(df_cols):
    """Converts string type columns to floats,
        rounded to a single decimal place
    - INPUT:    dataframe column slice
                <df[["col"]]> for a single column, 
                or <df[list_cols]> for a list of columns.
    - OUTPUT:   None. Dataframe columns are converted to floats.
        
    """
    print( "Converting...................")
    return df_cols.astype('float')
