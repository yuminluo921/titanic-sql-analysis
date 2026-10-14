import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# 1. 连接数据库
db_password = os.getenv("MYSQL_PASSWORD")
engine = create_engine(f'mysql+pymysql://root:{db_password}@localhost:3306/sql_practice')

# 2. 用 SQL 把我们要画图的数据查出来
sql = """
SELECT sex, pclass, AVG(survived) AS survival_rate
FROM titanic
GROUP BY sex, pclass
"""
df = pd.read_sql(sql, engine)

# 3. 用 Seaborn 画柱状图
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='pclass', y='survival_rate', hue='sex')
plt.title('Survival Rate by Pclass and Sex')
plt.ylabel('Survival Rate')
plt.xlabel('Pclass')

# 4. 保存图片到本地 (一定要写在 plt.show() 之前)
plt.savefig('titanic_survival_rate.png', dpi=300, bbox_inches='tight')
print("图片已成功保存为 titanic_survival_rate.png")
plt.show()