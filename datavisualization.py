import pandas as pd
import io
import sys  
import seaborn as sns
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码  
 
budget = pd.read_csv("mn-budget-detail-2014.csv",encoding = "utf8")
# print(budget)
budget = budget.sort_values('amount',ascending=False)[:10]

sns.set_style("darkgrid")
bar_plot = sns.barplot(x=budget["detail"],y=budget["amount"],
palette="muted",
x_order=budget["detail"].tolist())
plt.xticks(rotation=90)
plt.show()