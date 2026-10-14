import os
import pandas as pd
from sqlalchemy import create_engine

# 1. 从环境变量读取密码
db_password = os.getenv("MYSQL_PASSWORD")
engine = create_engine(f'mysql+pymysql://root:{db_password}@localhost:3306/sql_practice')

# 2. 使用国内加速镜像直接读取 Titanic 数据
print("正在通过国内镜像下载数据，请稍等...")
# 这里用 ghproxy 加速访问 GitHub 的原始数据链接
url = "https://ghproxy.net/https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
print("数据预览：\n", df.head())

# 3. 导入到 MySQL 数据库
df.to_sql('titanic', engine, index=False, if_exists='replace')
print(f"成功导入 {len(df)} 行数据到 titanic 表！")