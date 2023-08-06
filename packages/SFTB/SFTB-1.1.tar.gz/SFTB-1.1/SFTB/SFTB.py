# -*- coding: utf-8 -*-
"""
Created on Tue May  9 13:44:05 2023

@author: Y.C.Huang 
@email:1950003@tongji.edu.cn
@version 1.0
          _____                    _____                _____                    _____          
         /\    \                  /\    \              /\    \                  /\    \         
        /::\    \                /::\    \            /::\    \                /::\    \        
       /::::\    \              /::::\    \           \:::\    \              /::::\    \       
      /::::::\    \            /::::::\    \           \:::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \           \:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \           \:::\    \        /:::/__\:::\    \    
    \:::\   \:::\    \      /::::\   \:::\    \          /::::\    \      /::::\   \:::\    \   
  ___\:::\   \:::\    \    /::::::\   \:::\    \        /::::::\    \    /::::::\   \:::\    \  
 /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \      /:::/\:::\    \  /:::/\:::\   \:::\ ___\ 
/::\   \:::\   \:::\____\/:::/  \:::\   \:::\____\    /:::/  \:::\____\/:::/__\:::\   \:::|    |
\:::\   \:::\   \::/    /\::/    \:::\   \::/    /   /:::/    \::/    /\:::\   \:::\  /:::|____|
 \:::\   \:::\   \/____/  \/____/ \:::\   \/____/   /:::/    / \/____/  \:::\   \:::\/:::/    / 
  \:::\   \:::\    \               \:::\    \      /:::/    /            \:::\   \::::::/    /  
   \:::\   \:::\____\               \:::\____\    /:::/    /              \:::\   \::::/    /   
    \:::\  /:::/    /                \::/    /    \::/    /                \:::\  /:::/    /    
     \:::\/:::/    /                  \/____/      \/____/                  \:::\/:::/    /     
      \::::::/    /                                                          \::::::/    /      
       \::::/    /                                                            \::::/    /       
        \::/    /                                                              \::/____/        
         \/____/                                                                ~~              

"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
from scipy.optimize import fsolve,root


'''逻辑函数'''
def fx(dx):
    exp = 2.7182818
    ans = exp**dx/(1.0+exp**dx)
    return ans

'''主类'''
class qRrating:
    
    '''保存根目录'''
    def __init__(self,base_root):
        self.base_root = base_root
        self.tak =1

    #001生成估计方程组
    '''创建可用的拟合公式，
    第一参数NUM是选手数，
    第二参数year是滑动窗口的大小
    目前只能处理二次拟合，
    最大处理对手数32
    '''
    
    def func_generation(self,player,year):
        if player > 32:
            print("选手数量最大值为32")
            return
        NUM = player
        # 将公式拆分成一个列表
        formulas = [
            "x[0]+x[1]+x[2]",
            "x[3]+x[4]+x[5]",
            "x[6]+x[7]+x[8]",
            "x[9]+x[10]+x[11]",
            "x[12]+x[13]+x[14]",
            "x[15]+x[16]+x[17]",
            "x[18]+x[19]+x[20]",
            "x[21]+x[22]+x[23]",
            "x[24]+x[25]+x[26]",
            "x[27]+x[28]+x[29]",
            "x[30]+x[31]+x[32]",
            "x[33]+x[34]+x[35]",
            "x[36]+x[37]+x[38]",
            "x[39]+x[40]+x[41]",
            "x[42]+x[43]+x[44]",
            "x[45]+x[46]+x[47]",
            "x[48]+x[49]+x[50]",
            "x[51]+x[52]+x[53]",
            "x[54]+x[55]+x[56]",
            "x[57]+x[58]+x[59]",
            "x[60]+x[61]+x[62]",
            "x[63]+x[64]+x[65]",
            "x[66]+x[67]+x[68]",
            "x[69]+x[70]+x[71]",
            "x[72]+x[73]+x[74]",
            "x[75]+x[76]+x[77]",
            "x[78]+x[79]+x[80]",
            "x[81]+x[82]+x[83]",
            "x[84]+x[85]+x[86]",
            "x[87]+x[88]+x[89]",
            "x[90]+x[91]+x[92]",
            "x[93]+x[94]+x[95]"
        ]
     
        formulas = formulas[:NUM]
        
        # 计算每两个公式之间的差并存储到列表中
        differences = []
        for i in range(len(formulas)):
            for j in range(len(formulas) ):
                diff = "fx(" + formulas[i] + ")-(" + formulas[j] + ")"
                differences.append(diff)
        
        def split_list(lst):
            n = NUM
            return [lst[i:i+n] for i in range(0, len(lst), n)]
        spdiff = split_list(differences)
        
        
        def concatenate_strings(lst):
            return "+".join(lst)
        cs = []
        for ea in spdiff:
            csdiff = concatenate_strings(ea)
            cs.append(csdiff)
                
        qs = []
        q = 0
        for big in range(year*3):
            for ead in range(len(cs)):
                ds = "b["+str(big)+"]*"+"(" + cs[ead] + ")-c["+str(q)+"]*b["+str(big)+"],"
                q = q+1
                qs.append(ds)
        
        df = pd.DataFrame(qs)
        df.to_excel(self.base_root+'/data_'+str(NUM)+'_base_manul_func_'+str(year)+'.xlsx', index=False)                  
    
    
    
    
    ##-----------------------------------------------------------------------------------##
    
    #002生成&估计测试数据
    '''创建假想数据'''
    def generate_test_value(self):
        # 创建 x 坐标轴上的值数组，范围为 -5 到 5，仅取整数点
        x = np.arange(-5, 6, 1)
        # 第一条曲线
        y1 = np.ones_like(x) * 15
        # 第二条曲线由两个二次函数组成
        y2 = np.piecewise(x, [x < 0, x >= 0],
                           [lambda x: -((x+3.5)**2) +10, lambda x: (x-3.5)**2+16])
        
        # 转换为 DataFrame
        data = pd.DataFrame({'x': x, 'y1': y1, 'y2': y2})    
    
        # 绘制折线图
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        plt.plot(x, y1, 'o-', label='team A')
        plt.plot(x, y2, 'x-', label='team B')
        plt.xlabel('假想时间（年）')
        plt.ylabel('技能水平')
        plt.xticks(x)
        plt.legend()
        plt.show()
        return data

    #处理数据
    #模拟比赛输赢
    def generate_pairs(self,n1, n2):
        """根据两个数字的大小比例的绝对值返回一对和为20、比例大小等于这两个值的倒数的整数数对。"""
        ratio = abs(n2 / n1)
        a = int(round(20 * n1 / (n1 + n2)))
        b = 20 - a
        return a, b
    
    #将模拟数据打入dataframe
    def generate_rate(self,data):
    #获取比较数据
        data['y1_win'] = ''
        data['y2_win'] = ''
        for i, row in data.iterrows():
            y1 = row['y1']
            y2 = row['y2']
            w1,w2 = self.generate_pairs(y1, y2)
            data.at[i, 'y1_win'] = w1
            data.at[i, 'y2_win'] = w2
        return data
    
    ### srt开始年份
    def estimate_main(self,data,srt):
        #拟合
        #参数配置，顺序为t^2,t,1，时间序为-1to1
        b = [-1,1,-1,0,0,1,1,1,1]
        #确定b，对称情况下不变 
        #确定c,这是不同的。
        cd = []
        #因为只有两个人，所以直接建立矩阵
        for index, row in data.iterrows():  # 遍历DataFrame的每一行
               y1_win = row['y1_win']  
               y2_win = row['y2_win']  
               cd.extend([y1_win, y2_win]*3)          
        start = 0 + 6*srt
        cont = 18 + 6*srt
        c = cd[start:cont]   
        return b,c,start,cont

    def cal_main(self,player,start,cont,equations):
        ###解方程
        # 初始值
        initialGuess = np.ones(player*3)
        
        # 求解方程组
        result = root(equations, initialGuess, method='lm')
        # 输出结果
        res = result.x
        
        #结果分列
        def partition(lst, n):
            """将列表每n个元素分为一组"""
            return [lst[i:i + n] for i in range(0, len(lst), n)]
        
        #记录结果，二次系数
        cpoa = partition(res, 3)
        dfoa = pd.DataFrame(cpoa)
        dfoa.to_excel(self.base_root+'/coeff_player,start,length_'+
                                str(player)+'_'+str(int(start/6))+'_'+str(int(cont/6))+'.xlsx', index=False) 

    #模拟数据主函数
    def process_main(self,start_day):
        data_raw = self.generate_test_value()
        data_rate = self.generate_rate(data_raw)
        b,c,start,cont = self.estimate_main(data_rate,start_day)          
        return b,c,start,cont
       
    ##--------------------------------------------------------------------------------##
    
    #003数据输入&预处理
    #新制函数，从excel读入数据，数据已经是矩阵形式
    #start是开始，cont是总长，最小为1
    def matrix_in(self,start,cont):
        #确定b，对称情况下不变
        #b是时间参数，c是胜负参数
        b = [-1,1,-1,0,0,1,1,1,1]       
        c = []
        for year in range(start,start+cont):
            # 读取 Excel 文件
            df = pd.read_excel(self.base_root+r'/file/'+str(year)+'_matrix.xlsx')
            # 计算每一行的和
            sum_list = df.sum(axis=1).tolist()
            #复制的原因是一次胜负要对应时间的3参数
            c.extend(sum_list*3)
   
        return b,c,start,start+cont
   
    ##修改
    def line_to_matrix(self,year):
        # 从 Excel 文件中读取数据
        df = pd.read_excel(self.base_root+r'/file/'+str(year)+'_pairdata.xlsx')        
        unique_list = list(set(df['p1_team'].tolist()))
        mat_num = len(unique_list)
        mat =  [[0]*mat_num for _ in range(mat_num)]
        matscore =  [[0]*mat_num for _ in range(mat_num)]
        df = df.sort_values(by="p1_team",ascending=False) # by指定按哪列排
        for index, row in df.iterrows():
            # 输出 "home" 标签的值       
            home = row['p1_team']
            homescore = row['p1_score']
            away = row['p2_team']
            awayscore = row['p2_score']
            ih = unique_list.index(home)
            ia = unique_list.index(away)
            mat[ih][ia] = mat[ih][ia] + 1
            if homescore > awayscore:
                matscore[ih][ia] = matscore[ih][ia] + 1
            if homescore < awayscore:
                matscore[ia][ih] = matscore[ia][ih] + 1
        
        matr = pd.DataFrame(mat,index=unique_list,columns=unique_list)
        matrscore = pd.DataFrame(matscore,index=unique_list,columns=unique_list)
        matr.to_excel(self.base_root+r'/'+str(year)+'_team_matrax.xlsx')
        matrscore.to_excel(self.base_root+r'/'+str(year)+'_score_matrax.xlsx')
    
    ##----------------------------------------------------------------------------------##
    #004估计&求解方程
    #解方程
    def main_calculation(self,player,start,cont,equations):     
       # 初始值
       initialGuess = np.ones(player*3)      
       # 求解方程组
       result = root(equations, initialGuess, method='lm')      
       # 输出结果
       res = result.x
       #结果分列
       def partition(lst, n):
           """将列表每n个元素分为一组"""
           return [lst[i:i + n] for i in range(0, len(lst), n)]
       
       #记录结果，记录二次系数
       coefficient = partition(res, 3)
       df_coefficient = pd.DataFrame(coefficient)
       df_coefficient.to_excel(self.base_root+'/coeff_player,start,length_'+
                               str(player)+'_'+str(start)+'_'+str(cont)+'.xlsx', index=False) 
     
        
    
    ##---------------------------------------------------------------------------##
    #005 数据绘图
    #正规化
    def normalize_three_lists(self,list1, list2, list3):
        """
        将三个列表分别进行最大值最小值归一化，并返回归一化后的三个列表
        """
        max_val = max(max(list1), max(list2), max(list3))
        min_val = min(min(list1), min(list2), min(list3))
        list1_norm = [(x - min_val) / (max_val - min_val) for x in list1]
        list2_norm = [(x - min_val) / (max_val - min_val) for x in list2]
        list3_norm = [(x - min_val) / (max_val - min_val) for x in list3]

        return list1_norm, list2_norm, list3_norm
    
    #插值
    def smooth(self,data):
        # Normalize data to the range of 0 to 1
        # Create x array with range from -5 to 5
        x = np.linspace(-5, 5, len(data))       
        from scipy.interpolate import interp1d
        # Use cubic spline interpolation to smooth the normalized data
        spl = interp1d(x, data, kind='linear')

        # Define new x array with more points for smoother curve
        x_new = np.linspace(-5, 5, 300)

        # Calculate y values of the smooth curve
        y_new = spl(x_new)
        return y_new    
    
    #主绘图函数
    ###FLAG控制区间
    def draw_plot(self,player,start,cont,num,margin,Flag=False):
        #margin = 1.5
        ###调整点 num = 1
        
        #绘制整点线
        def acf(a,b,c):
            r1 = a  - b  + c
            r2 = c
            r3 = a  + b  + c
            ans = [r1,r2,r3]
            return ans
        
        #绘制曲线
        
        def pqf(a, b, c):
            left_end = -1 * margin
            right_end = -left_end
            x = np.linspace(left_end, right_end, 200)
            y = a * x ** 2 + b * x + c
            plt.plot(x+self.tak , y,linestyle='--')
            self.tak = self.tak +1
        
        big_x = []
        i = 0
        while True:
            try:
                df_raw = pd.read_excel(self.base_root+'/coeff_player,start,length_'+
                                    str(player)+'_'+str(i)+'_'+str(i+cont)+'.xlsx')
                df = df_raw.iloc[num, :].tolist()
                a,b,c = df[0],df[1],df[2]
                pqf(a, b, c)
                big_x.extend(acf(a,b,c))
                i = i+1
            except:
                break
        
        if Flag==False:
        
            #初始值
            avg = [big_x[0]]
            max_ = [big_x[0]]
            min_ = [big_x[0]]
    
            avg.append((big_x[1]+big_x[3])/2.0)
            max_.append(max(big_x[1],big_x[3]))
            min_.append(min(big_x[1],big_x[3]))
    
            for i in range(0,len(big_x)):
                try:
                    avg.append((big_x[3*i+2]+big_x[3*i+4]+big_x[3*i+6])/3.0)
                    max_.append(max(big_x[3*i+2],big_x[3*i+4],big_x[3*i+6]))
                    min_.append(min(big_x[3*i+2],big_x[3*i+4],big_x[3*i+6]))
                except:
                    pass
                
            avg.append((big_x[-2]+big_x[-4])/2.0)
            max_.append(max(big_x[-2],big_x[-4]))
            min_.append(min(big_x[-2],big_x[-4]))
    
            avg.append(big_x[-1])
            max_.append(big_x[-1])
            min_.append(big_x[-1])
    
            
            plt.plot(avg,color='red',linewidth=1,marker='o'
                     ,markeredgecolor='r',markersize='5',markeredgewidth=0.01,label="avg")
            plt.plot(max_,color='black',linewidth=1,marker='o'
                     ,markeredgecolor='r',markersize='5',markeredgewidth=0.01,label="max")
            plt.plot(min_,color='black',linewidth=1,marker='o'
                     ,markeredgecolor='r',markersize='5',markeredgewidth=0.01,label="min")

        else:
            avg = []
            for i in range(0,len(big_x)*2):
                try:
                    avg.append((big_x[3*i]))
                    
                except:
                    pass
           
            plt.plot(avg,color='red',linewidth=1,marker='o'
              ,markeredgecolor='r',markersize='5',markeredgewidth=0.01,label="avg")
        plt.yticks([])
        plt.gca().yaxis.set_ticklabels([])
     

        plt.xlabel('假想时间（年）')
        plt.ylabel('技能水平估计')

        plt.legend()
        
        plt.savefig(self.base_root+'/skillrate_'+str(num+1)+'.png', dpi=300)
       
        plt.show()
        from sklearn.preprocessing import minmax_scale
        if Flag ==False:
            avg_,max__,min__ = self.normalize_three_lists(avg,max_, min_)
        else:
            avg_=minmax_scale(avg)
        
        df = pd.DataFrame(self.smooth(avg_))
        df.to_excel(self.base_root+'/avg_player'+str(num+1)+'.xlsx', index=False)
        self.tak = 0
    

    ##--------------------------------------------------------------------##
    #006距离计算
   
    
    '''计算fs距离'''
    def calculate_euclid(self,point_a, point_b):
        import math
        """
        Args:
            point_a: a data point of curve_a
            point_b: a data point of curve_b
        Return:
            The Euclid distance between point_a and point_b
        """
        return math.sqrt((point_a - point_b) ** 2)


    def calculate_frechet_distance(self,dp, i, j, curve_a, curve_b):
        """
        Args:
            dp: The distance matrix
            i: The index of curve_a
            j: The index of curve_b
            curve_a: The data sequence of curve_a
            curve_b: The data sequence of curve_b
        Return:
            The frechet distance between curve_a[i] and curve_b[j]
        """
        if dp[i][j] > -1:
            return dp[i][j]
        elif i == 0 and j == 0:
            dp[i][j] = self.calculate_euclid(curve_a[0], curve_b[0])
        elif i > 0 and j == 0:
            dp[i][j] = max(self.calculate_frechet_distance(dp, i - 1, 0, curve_a, curve_b),
                           self.calculate_euclid(curve_a[i], curve_b[0]))
        elif i == 0 and j > 0:
            dp[i][j] = max(self.calculate_frechet_distance(dp, 0, j - 1, curve_a, curve_b),
                           self.calculate_euclid(curve_a[0], curve_b[j]))
        elif i > 0 and j > 0:
            dp[i][j] = max(min(self.calculate_frechet_distance(dp, i - 1, j, curve_a, curve_b),
                               self.calculate_frechet_distance(dp, i - 1, j - 1, curve_a, curve_b),
                               self.calculate_frechet_distance(dp, i, j - 1, curve_a, curve_b)),
                           self.calculate_euclid(curve_a[i], curve_b[j]))
        else:
            dp[i][j] = float("inf")
        return dp[i][j]


    def fs_similarity(self,curve_a, curve_b):
        dp = [[-1 for _ in range(len(curve_b))] for _ in range(len(curve_a))]
        similarity = self.calculate_frechet_distance(dp, len(curve_a) - 1, len(curve_b) - 1, curve_a, curve_b)
        # return max(np.array(dp).reshape(-1, 1))[0]
        return similarity
    
    def fs_excel(self,file):
        df = pd.read_excel(file)
        # 将'p1'和'p2'列转换为list并返回
        a1 = df.iloc[:, 0].tolist()
        a2 = df.iloc[:, 1].tolist()
        fs_sm = self.fs_similarity(a1,a2)

        return fs_sm


if __name__ == "__main__":
    print("Start!")


