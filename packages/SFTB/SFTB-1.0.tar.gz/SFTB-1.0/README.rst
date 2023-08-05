1 Introduction to the SFTB library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.1 SFTB library
^^^^^^^^^^^^^^^^

The SFTB library is a Python code library designed for simulating and
applying the SFTB algorithm. It is currently hosted by PyPI and follows
the MIT open-source license.

1.2 Obtaining the SFTB library
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the code has been indexed by PyPI, users can quickly download the
code using various popular integrated development environments (such as
Spyder, Conda, etc.) when they need the library. To do this, simply
enter the following command (Code 4.1) in the window, and the system
will automatically download the main code and its dependencies.

::

   pip install SFTB

1.3 Key Features of the SFTB Library
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The SFTB library includes all major functionality of the SFTB algorithm,
including one class and over 30 functions. In particular, the qua_rating
class is the core of the entire library and contains all necessary
public variables, maintaining the overall integrity of the library. The
remaining 30 plus functions can be classified into five major
categories: 1. Generating estimation equation sets This functionality is
mainly provided by the func_generation() function. Because the SFTB
estimation has a maximum likelihood property, it needs to be equipped
with a large number of equation sets before participating in
calculation. Due to the mechanical and symmetrical nature of this task,
this function is designed to generate functions for users in batches and
in a standardized way. Equation sets can be generated freely by setting
the number of players participating in the game and the length of the
sliding interval. 2. Data input and pre-processing This functionality is
mainly provided by the matrix_in() function, etc. This group of
functions is the data input to the entire estimation class and is
responsible for importing data from xlsx into the calculation space. It
supports two main stream data input formats: matrix input, i.e., the
victory-defeat matrix between opponents, and list-style input, i.e., the
actual results of each “pairwise comparison”. 3. Estimation and solving
equations This functionality is mainly provided by the
main_calculation() function, which is the core of the SFTB estimation.
This module will use iterative calculation methods to estimate the data
after preprocessing through the equation set generated above to obtain
the most primitive estimation parameters. 4. Data plotting This
functionality is mainly provided by the draw_plot() function. After the
complicated estimation process, this function serves as a solution to
the problem of resetting the estimation interval and plotting the
estimation data to provide users with an intuitive visual conclusion.
Because the SFTB estimation involves sliding windows and the estimated
equation only provides the most primitive estimation parameters, its
visibility is not strong. 5. Distance calculation This functionality is
mainly provided by the calculate_frechet_distance() function, which is
responsible for the post-estimation work. Its main function is to
calculate the curve distance between functions, which can intuitively
reflect the accuracy of the estimation by the distance between the
estimated function and the function to be estimated.

2 SFTB Library User Manual
~~~~~~~~~~~~~~~~~~~~~~~~~~

After using pip to install the library code, users only need to enter
the necessary parameters based on the configuration to complete the
ranking estimate based on pairwise comparison. The following will guide
users on how to use some important functions of the library.

1. Import the library

::

   import SFTB 
   fx = SFTB.fx
   # Set the root directory
   qr = SFTB.qRrating(r'data-nfl-collect')

Firstly, as shown in Code 1 above, import the SFTB library and set the
root folder location. All subsequent operations must be carried out
around the root folder.

2. Build regression equations

::

   # Creates a set of equations and outputs to a local excel file
   qr.func_generation(player=3,year=3)

Given the complexity and regularity of the estimation equation, using
the above statement (Code 2), the system will quickly help users
generate the estimation equation set, and the obtained equation set will
be output to the root directory, named data_3_base_manul_func_3.xlsx
(using the above parameter as an example).

3. Data preprocessing First, we need to create a file in the root
   directory named “file” and make an xlsx file for each year based on
   the estimation year (named “{year}_matrix.xlsx”) that includes the
   wins and losses of each player that year. Taking Example 2.3.2 as an
   example, splitting Table 2.2 into three tables by year and converting
   the middle “x” to 0 is sufficient. To demonstrate the functionality
   of interval estimation, this example creates fourth-year rankings,
   with the same numerical values as those of the first year rankings.

4. Fill in equations, fit and solve

::

   def main():
       # Read the xlsx data, start is the starting data of the continuous numbering, 
       # cont is the total number of files to be analyzed
       b,c,start,cont = qr.matrix_in(start=1,cont=3)  
       # Define the equation set to be solved
       def equations(x):
           y = [
                   # Fill in the estimation equation set generated above
               ]
           return y
           qr.cal_main(player=3,
                       start=start,
                       cont=cont,
                       equations=equations)
       
   for year in range(BIG_NUM):
       try:
           main(year)
       except:
           pass

After writing and running the estimation framework shown in Code 3
above, the system will automatically complete all estimation parts and
output the estimated parameter results in the form of xlsx to the root
directory. The output file will be automatically named coeff_player,
start, length_3_1_4.xlsx and coeff_player, start, length_3_2_5.xlsx. In
the files, all necessary estimated parameters are provided. In the Code
above, the parameter start is the starting value of each estimation
time, and the parameter cont is the window size for each estimation.

4. Data plotting

::

   qr.draw_plot(player=3, 
                  start=1, 
                   cont=3,
                    num=0, 
               margin=1.5)

After obtaining all xlsx files that contain estimation parameters
through pre-processing, estimation, and plotting, it is critical to
provide users with a method to calculate the distance between the
estimated curve and the curve to be estimated. The Code above (Code 4)
can instantly merge the information and draw the parameter estimation
graph output to the root directory (the image will be named
skillrate_{1}.png). At the same time, the system will automatically
calculate the average estimation and fill in the estimation data. The
completed information will also be output to the root directory (the
fill-in information will be named avg_player{1}. Xlsx). In the Code
above, the player represents the number of players participating in the
game, start and cont are the same as before, num represents which
player’s image to output, and margin is the decoration parameter for
curve plotting.

5. Distance comparison

::

   qr.fs_excel(r'data-compare.xlsx')

The distance between the curves reflects the accuracy of the estimation.
After completing the preprocessing, estimation, and plotting steps,
providing users with a way to calculate the distance between the curve
to be estimated and the estimated curve is of utmost importance. In the
Code above (Code 5), users need to give the system an xlsx file with a
full path, and the file needs to include two columns of data to be
calculated (which need to be placed in the first and second columns of
the xlsx file). As a result, the system will output the curve distance
between the two columns in the console.

1 SFTB库&简介
~~~~~~~~~~~~~

1.1 SFTB库
^^^^^^^^^^

SFTB库是本文为了研究SFTB算法的仿真、应用而设计的一个python代码库,目前代码云由pypi开源组织代管,代码遵循MIT开源协议。

1.2获取SFTB的方式
^^^^^^^^^^^^^^^^^

由于代码已获得pypi组织的索引,故用户可利用python的各种常用集成编译器(如spyder,conda等)方式快速的进行代码下载。在需要该库时,仅需在窗口中输入如下(代码1)的信息,系统将自动完成保留主代码段与依赖包的下载。
``pip install SFTB``

1.3 SFTB库的主要功能
^^^^^^^^^^^^^^^^^^^^

SFTB库包含了SFTB算法的所有主要功能,其主要包括1个类与30余个函数。其中,qua_rating类是整个库函数的核心,其包含了所有必要的公共变量,并维护着库函数的整体性。剩下的30余个函数的功能可分为5大类,具体而言：
1. 生成估计方程组
该功能主要由函数func_generation()承担,由于SFTB估计的极大似然特性,故其需要先设定大量的方程组而后才能参与计算,由于该工作的机械性与对称性,本文设计了此函数以批量、标准的为用户生成函数。方程组可通过设定参与比赛的人数,以及滑动区间的长短自由生成。
2. 数据输入&预处理
该功能主要由函数matrix_in()等承担,此组函数是整个估计类的数据入口,负责将数据由xlsx导入计算空间,其支持两种主流的数据输入格式：矩阵式输入,即对手间的胜负矩阵；列表式输入,即每次“成对比较”的实际结果。
3. 估计&求解方程
该功能主要由函数main_calculation()承担,是SFTB估计的核心。该模块将采用迭代计算的方式,使得经过预处理的数据通过上述生成的方程组进行估计,从而获得最原始的估计参数。
4. 数据绘图
该功能主要由函数draw_plot()承担,复杂估计后函数的绘图工作。由于SFTB估计涉及到滑动窗口,且估计的方程仅提供最原始的估计参数,可视性不强,故通过该函数可以一步解决估计窗口复位与估计数据绘图的问题,以提供用户直观的视觉结论。
5. 距离计算
该功能主要由函数calculate_frechet_distance()承担,负责后估计工作。其主要的功能是计算函数间的曲线距离,可通过估计函数与带估计函数的距离大小直观的反应估计的准确度。

2 SFTB库使用手册
~~~~~~~~~~~~~~~~

使用pip后系统将自动导入所需的代码框架,用户只需根据配置输入必要的参数即可完成基于成对数据比较的排名估计,下面将介绍该库一些重要功能的应用手册。

1. 导入库

::

   import SFTB 
   fx = SFTB.fx
   #设定主文件夹位
   qr = SFTB.qRrating(r'data-nfl-collect')

首先,如上述(代码1)所示,需要使用import导入SFTB库,同时设定主文件夹位置,之后的所有操作均需围绕主文件夹进行。

2. 构建回归方程

::

   #创建后会得到方程,输出于根目录excel
   qr.func_generation(player=3,year=3)

鉴于估计方程的复杂性与规律性,使用上述语句后(代码2),系统将快速帮助用户生成估计方程组,获得的方程组将被输出于根目录,命名为data_3_base_manul_func_3.xlsx(以上述参数为例)。

3. 数据预处理
   首先,我们需要在根目录中新建一个文件并命名为file,并按照估计年份一年制作一份xlsx文件(命名规则为“{年份}_matrix.xlsx”),每份xlsx需包含当年各选手的胜负情况。以例2.3.2为例,即将表2.2按年份拆除三个表,并且将中间的x转换为0即可。为了演示区间估计的功能,此处创建了第4年的成绩,其数值与第一年成绩相同。

4. 回填方程、拟合求值

::

   def main():
   #读取xlsx数据,start为连续标号的初始数据,
   #cont为总共分析的文件总数
       b,c,start,cont = qr.matrix_in(start=1,cont=3)  
       # 定义要求解的方程组
       def equations(x):
           y = [
                   #此处填入上述生成的估计方程组即可  
                   ]
           return y
           qr.cal_main(player=3,
                       start=start,
                       cont=cont,
                       equations=equations)
       
   #遍历框架,range后应设置一个足够大的数字
   for year in range(BIG_NUM):
       try:
           main(year)
       except:
           pass

编写并运行如上图(代码3)的估计框架后,系统将自动完成所有的估计部分,并将估计结果参数以xlsx形式输出至根目录中,输出文件将被自动命名为(coeff_player,start,length_3_1_4.xlsx与coeff_player,start,length_3_2_5.xlsx)。文件中按结构给出了所有必要的估计参数。上述代码中,参数start为每次估计的时间开始值,参数cont为每次估计的窗口大小。

4. 绘图

::

       #根据上述excel绘制曲线
       qr.draw_plot(player=3, 
                      start=1, 
                       cont=3,
                        num=0, 
                   margin=1.5)

获得所有包含估计参数的xlsx后,再运行上述语句(代码4),系统将自动合并其中信息,并绘制参数估计图输出于根目录中(图片会被命名为skillrate_{1}.png)；同时,系统将自动计算估计均值并对其进行差值补全处理,补全完毕的数据信息也将一并输出于根目录(补全信息会被命名为avg_player{1}.xlsx)。上述语句中,player代表参与比赛的人数,start与cont内容与前文一致,num代表输出哪一位选手的图像,margin是曲线绘图装饰参数。

5. 距离比较

::

       #输入一个.xlsx文件全称,输出fs距离
       qr.fs_excel(r'data-compare.xlsx')

距离的远近反应了估计的准确度,在完成上述预处理、估计、绘图等步骤后,给予用户一种计算待估计曲线与估计曲线间的距离的方法具有重要意义。上述语句中(代码5),用户需要给予系统一个具有完整路径的xlsx文件,且该文件需要包含待计算距离的两列数据(需要置于xlsx的第一二列),由此系统将在控制台中输出两列的曲线距离。
