from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mypandas.models import Jikwon
plt.rc('font', family='malgun gothic')

def mainFunc(request):
    return render(request, 'main.html')


def showFunc(request):
    jikwons = Jikwon.objects.all().values()
    # print(jikwons)
    df = pd.DataFrame.from_records(data=jikwons)
    df.columns = ['사번','직원명','부서','직급','연봉','입사','성별','평점']
    # print(df.head(2))
    
    # 직급별 연봉합/평균
    jik_group = df['연봉'].groupby(df['직급'])
    # print(jik_group.sum())
    
    jik_group_detail = {'sum':jik_group.sum(), 'avg':jik_group.mean()}
    df2 =pd.DataFrame(jik_group_detail)
    # print(df2)
    ctab = pd.crosstab(df['직급'], df.성별)
    # print(ctab)
    
    # 시각화
    jik_result = jik_group.agg(['sum', 'mean'])
    print(jik_result)
    jik_result.plot(kind='barh')   # DataFrame 으로 시각화를 진행
    plt.title('직급별 연봉 합/평균')
    plt.xlabel('연봉')
    plt.ylabel('직급')
    fig = plt.gcf()
    fig.savefig('django12_pandas/mypandas/static/images/jik.png') # 절대경로를 써야한다.
    
    return render(request, 'list.html', {'datas':df.to_html(index=False, border=10),
                                         'jik_group':jik_group,
                                         # 'jik_group2':jik_group.to_html()
                                         'jik_group_detail': df2.to_html(border=10),
                                         'ctab':ctab.to_html(border=10),
                                         
                                         })



