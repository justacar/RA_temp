import pandas as pd
from sklearn.model_selection import train_test_split

def build_dataset(df):
    
    data = ''
   
    for idx,row in df.iterrows():
        answer = row['answer']
        question = row['question']
        sep_token = '<SEP>'
        eos_token = '<EOS>'
        df.loc[idx,"input"] = answer + ' ' + sep_token + ' ' +question + ' '+  eos_token
        
if __name__ == "__main__":
    FAQ_eval = pd.read_csv("FAQ_Bank_eval.csv",usecols=[0,2,4,7,8],encoding='utf-8')
    FAQ = FAQ_eval[(FAQ_eval["language"]=="en")&(FAQ_eval["type"]=="Question")&(FAQ_eval["index"]!=1195)]
    build_dataset(FAQ)
    train_valid_ratio = 8/10
    df_train, df_valid = train_test_split(FAQ, train_size = train_valid_ratio, random_state = 77)
    
    f = open('train.txt', 'w')
    data = ''
    for idx,row in df_train.iterrows():
        data += row['input'] + '\n'
    f.write(data)


    f = open('valid.txt', 'w')
    data = ''
    for idx,row in df_valid.iterrows():
        data += row['input'] + '\n'
    f.write(data)
