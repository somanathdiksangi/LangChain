from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()
model1=ChatGroq(model="llama3-8b-8192")
model2=ChatGroq(model="llama-3.3-70b-versatile")
model3=ChatGroq(model="llama3-8b-8192")

prompt1=PromptTemplate(
    template='generate short notes of given text {text}',
    input_variables=['text']
)
prompt2=PromptTemplate(
    template='for the givin text {text} generate a 5 qustion'
)

prompt3=PromptTemplate(
    template='marge the provoded notes and qustion into a single docotement \n notes {notes}and \n qustion {qustion} '
)
perser=StrOutputParser()


paralle_scama=RunnableParallel({
    'notes':prompt1|model1|perser,
    'qustion':prompt2|model2|perser
})

merge_chain=prompt3|model2|perser

chain=paralle_scama|merge_chain
text="""
In machine learning, support vector machines (SVMs, also support vector networks[1]) are supervised max-margin models with associated learning algorithms that analyze data for classification and regression analysis. Developed at AT&T Bell Laboratories,[1][2] SVMs are one of the most studied models, being based on statistical learning frameworks of VC theory proposed by Vapnik (1982, 1995) and Chervonenkis (1974).

In addition to performing linear classification, SVMs can efficiently perform non-linear classification using the kernel trick, representing the data only through a set of pairwise similarity comparisons between the original data points using a kernel function, which transforms them into coordinates in a higher-dimensional feature space. Thus, SVMs use the kernel trick to implicitly map their inputs into high-dimensional feature spaces, where linear classification can be performed.[3] Being max-margin models, SVMs are resilient to noisy data (e.g., misclassified examples). SVMs can also be used for regression tasks, where the objective becomes 
ϵ
{\displaystyle \epsilon }-sensitive.

The support vector clustering[4] algorithm, created by Hava Siegelmann and Vladimir Vapnik, applies the statistics of support vectors, developed in the support vector machines algorithm, to categorize unlabeled data.[citation needed] These data sets require unsupervised learning approaches, which attempt to find natural clustering of the data into groups, and then to map new data according to these clusters.

The popularity of SVMs is likely due to their amenability to theoretical analysis, and their flexibility in being applied to a wide variety of tasks, including structured prediction problems. It is not clear that SVMs have better predictive performance than other linear models, such as logistic regression and linear regression.[5]
"""
result=chain.invoke({'text':text})
print(result)
chain.get_graph().print_ascii()