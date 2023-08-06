from urllib import response
import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

from learntools_dados_ufv.core import *

root_df = pd.read_csv('./Market_Basket_Optimisation.csv',header=None)

def run_df_processing(steps=0):
    answer = root_df.copy()
    if (steps == 0): 
        return answer
    
    transactions_array = []
    for i in range(len(df)):
        transactions_array.append([str(df.values[i,j]) for j in range(len(df.columns))])
        
    transactions_array = np.array(transactions_array)
    transactions_oht = TransactionEncoder()
    transactions = transactions_oht.fit(transactions_array).transform(transactions_array)
    
    answer = pd.DataFrame(transactions, columns=transactions_oht.columns_)
    answer.drop(['nan'],axis=1,inplace=True)

    if (steps == 1): 
        return answer
    
    answer = apriori(answer, min_support=0.01, use_colnames=True)

    if (steps == 2): 
        return answer
    
    answer = association_rules(answer, metric='confidence', min_threshold=0.3)
    
    if (steps == 3): 
        return answer
    
    if (steps == 4):
        return answer[(answer['support'] >= 0.015) & (answer['confidence'] >= 0.4)]
    
    if (steps == 5):
        return answer[(answer['lift'] >= 2) & (answer['confidence'] >= 0.5)]
    

# q1
class Q1(CodingProblem):
    _var = 'df'
    #_hint = 'Utilize a função `pd.read_csv` com o caminho do arquivos `pesos_populacao.csv`. Note que não há cabeçalhos no arquivo.'

    _solution = ''

    def check(self, df):
        assert_isinstance(pd.DataFrame, df, name='df')
        answer = run_df_processing(1)
        assert_df_equals(df, answer, name='df')


# q2.a
class Q2A(CodingProblem):
    _var = 'frequent_itemsets'
    _hints = [
        'Utilize a função `apriori` como mostrado no roteiro.',
        'Você deve passar os paramêtros na descrição do problema.',
        'Você adicionou os parâmetros `use_colnames` e `min_support`?',
    ]

    _solution = ''

    def check(self, frequent_itemsets):
        assert_isinstance(pd.DataFrame, frequent_itemsets, name='frequent_itemsets')
        answer = run_df_processing(2)
        assert_df_equals(frequent_itemsets, answer, name='frequent_itemsets')

# q2.b
class Q2B(CodingProblem):
    _var = 'rules'
    _hints = [
        'Utilize a função `association_rules` como mostrado no roteiro.',
        'Você deve passar os paramêtros na descrição do problema.',
        'Você adicionou o parâmetro `min_threshold`?',
        'A metric passada como parâmetro é a `confidence`?',
    ]

    _solution = ''

    def check(self, rules):
        assert_isinstance(pd.DataFrame, rules, name='rules')
        answer = run_df_processing(3)
        assert_df_equals(rules, answer, name='rules')

Q2 = MultipartProblem(Q2A, Q2B)

# q3.a
class Q3A(CodingProblem):
    _var = 'rules_a'
    _hints = [
        'Tente fazer primeiro o filtro de suporte.',
        'Monte agora o filtro de confidence',
        'Junte os dois filtros utilizando o operador and (&)'
        
    ]

    _solution = ''

    def check(self, rules_a):
        answer = run_df_processing(4)
        assert_equal(rules_a, answer, name='rules_a')

# q3.b
class Q3B(CodingProblem):
    _var = 'rules_b'
    _hints = [
        'Tente fazer primeiro o filtro do lift.',
        'Monte agora o filtro de confidence',
        'Junte os dois filtros utilizando o operador and (&)'
        
    ]

    _solution = ''

    def check(self, rules_b):
        answer = run_df_processing(5)
        assert_equal(rules_b, answer, name='rules_b')


Q3 = MultipartProblem(Q3A, Q3B)


qvars = bind_exercises(globals(), [
    Q1,
    Q2,
    Q3,
  
], var_format='q{n}')

__all__ = list(qvars)