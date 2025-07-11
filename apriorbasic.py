from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
data=[['pen','pencil'],
      ['pen','note'],
      ['pen','pencil','note'],
      ['pen','pencil','eraser'],
      ['pen','pencil','note','eraser']]
te=TransactionEncoder()
te_arr=te.fit(data).transform(data)
df=pd.DataFrame(te_arr,columns=te.columns_)
print(df)
frequent_sets=apriori(df,min_support=0.5,use_colnames=True)
print(frequent_sets)
#from mlxtend.frequent_patterns import apriori, association_rules
assoc_rule=association_rules(frequent_sets,metric="confidence",min_threshold=0.5)
print(assoc_rule[['confidence','consequents','support']])
