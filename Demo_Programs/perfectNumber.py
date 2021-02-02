'''
Hello, this program is using the Rich import. If you do not want to install the import please remove
'perfectNumberFormattedPrint function', and uncomment a for loop below and comment (or delete)
all in the 'with progress' area

Rich is a console color package used for making everything more interesting
and not just black on white text (or black on white text)
'''
from rich.console import Console
console = Console()

def perfectNumberFormattedPrint(x) -> None:
    for i in range(len(x)):
        x[i].sort()
        console.print(str(sum(x[i])) + " is a perfect number made of " + str(x[i]))

        # print(i for i in range(x))




#Not Combined
def findSums(number) -> list:
    x = [1]
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            x.append(i)
    return x
def findIfPerfectUnCombined(number, x) -> list:
    if sum(x) == number:
            print(number, "is a perfect number with the values of:", x)
            return x

# for i in range(1, 10000):
#     x = findSums(i)
#     findIfPerfectUnCombined(i, x)

import math as m 

# Combined
def findIfPerfectCombined(number) -> list:
    x = [1]
    for i in range(2, (int(m.sqrt(number))) + 1):
        if number % i == 0:
            x.append(i)
            x.append(number // i)
    value = 0
    for i in range(len(x)):
        value += x[i] 
    if value == number:
        # print(number, "is a perfect number with the values of: "+ str(x))
        return x
x = []



from rich.progress import Progress
n = 100000
i = 0

#Insanly Faster, but no progress bar
# for i in range(n):
#     findIfPerfectCombined(i)


#Slow but with UI

import os
with Progress() as progress:
    os.system("clear")
    task1 = progress.add_task("[red]Working...", total=n)
    
    while not progress.finished:
        progress.update(task1, completed=i)
        if not findIfPerfectCombined(i) == None:
            x.append(findIfPerfectCombined(i))
        i+=1

perfectNumberFormattedPrint(x)




#Other program


# x = '''
# 6
# 28
# 496
# 8128
# 33550336
# 8589869056
# 137438691328
# 2305843008139952128
# 265845599156...615953842176
# 191561942608...321548169216
# 131640364585...117783728128
# 144740111546...131199152128
# 235627234572...160555646976
# 141053783706...759537328128
# 541625262843...764984291328
# 108925835505...834453782528
# 994970543370...675139915776
# 335708321319...332628525056
# 182017490401...437133377536
# 407672717110...642912534528
# 114347317530...558429577216
# 598885496387...324073496576
# 395961321281...702691086336
# 931144559095...790271942656
# 100656497054...255141605376
# 811537765823...603941666816
# 365093519915...353031827456
# 144145836177...957360406528
# 136204582133...233603862528
# 131451295454...491774550016
# 278327459220...416840880128
# 151616570220...600565731328
# 838488226750...540416167936
# 849732889343...028118704128
# 331882354881...017723375616
# 194276425328...724174462976
# 811686848628...573022457856
# 955176030521...475123572736
# 427764159021...460863021056
# 793508909365...578206896128
# 448233026179...460572950528
# 746209841900...874791088128
# 497437765459...536164704256
# 775946855336...476577120256
# 204534225534...975074480128
# 144285057960...837377253376
# 500767156849...221145378816
# 169296395301...626270130176
# 451129962706...557930315776
# 109200152134...402016301056
# 110847779864...007191207936
# '''.strip().split("\n")

# y = []

# for i in range(len(x)):
#     try:
#         y+=(x[i][-1])
#     except:
#         y+=(x[i])

# os.system("clear")

# six = 0
# eight = 0

# sixList = []
# eightList = []
# otherList = []


# tF = []

# r1 = []
# r2 = []

# for i in range(len(y)):
#     if y[i] == "6":
#         six += 1
#         eight = 0
#         sixList.append(six)
#         r1.append(i)
#     elif y[i] == "8":
#         eight += 1
#         six = 0
#         eightList.append(eight)
#         r2.append(i)


# import matplotlib.pyplot as plt
 
# # Create bars
# barWidth = 0.9
# bars1 = sixList
# bars2 = eightList
# bars4 = bars1 + bars2

# print(sixList)
 
# # The X position of bars


# r4 = r1 + r2
 
# # Create barplot
# plt.bar(r1, bars1, width = barWidth, color = (0.3,0.1,0.4,0.6), label='Last Digit is Six')
# plt.bar(r2, bars2, width = barWidth, color = (0.3,0.5,0.4,0.6), label='Last Digit is Eight')
# # plt.bar(r3, bars3, width = barWidth, color = (0.3,0.9,0.4,0.6), label='With other genotype')
# # Note: the barplot could be created easily. See the barplot section for other examples.
 
# # Create legend
# plt.legend()
 
# # Text below each barplot with a rotation at 90°
# # plt.xticks([r + barWidth for r in range(len(r4))], [str(i) for i in range(len(r4)) ], rotation=90)
# plt.xticks([i for i in range(1,len(r4)+1)],[i for i in range(1,len(r4)+1)]) 
# # Create labels
# label = [str(i) for i in range(len(r4))]
 
# # Text on the top of each barplot
# for i in range(len(r4)):
#     plt.text(x = r4[i]-0.5 , y = bars4[i]+0.1, s = label[i], size = 8)
 
# # Adjust the margins
# plt.subplots_adjust(bottom= 0.2, top = 0.98)
# plt.title("Values of Perfect Number Ones Digits")
# # Show graphic
# plt.show()
