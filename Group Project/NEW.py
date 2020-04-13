INFILE = open("player_regular_season_career.txt","r")

i=0
li = []
for line in INFILE:
    if(i==0):
        i += 1
        continue
    i+=1
    fields = line.split('|')
    firstName = fields[1]
    lastName = fields[2]
    gp,pts,reb,asts,stl,blk,turnover,fga,fgm,fta,ftm =\  ##提取每个球员的参数
    int(fields[4]),int(fields[6]),int(fields[9]),int(fields[10]),int(fields[11]),int(fields[12]),\
    int(fields[13]),int(fields[15]),int(fields[16]),int(fields[17]),int(fields[18])
    ##print(gp,pts,reb,asts,stl,blk,turnover,fga,fgm,fta,ftm)
    #break
    efficiency = (pts+reb+asts+stl+blk-(fga-fgm)+fta-ftm+turnover)/float(gp)
    li.append([efficiency,firstName,lastName])  ##把efficiency和名字对应起来，存储于列表
print("data collected")
li.sort()
li.reverse()  ##倒序，大到小排列

OUTFILE = open("top50.txt","w")
for i in range(50):
    OUTFILE.write(li[i][1]+" "+li[i][2]+","+str(li[i][0])+"\n")
OUTFILE.close()

print("finished")

k = int(input("请输入所查找的球员编号，全部输出请输入0"))
if k<50 and k>=0:
    if k==0:
        for i in range(50):
            print(li[i][1] + " " + li[i][2] + "," + str(li[i][0]) + "\n")
    else:
        print(li[k-1][1]+" "+li[k-1][2]+","+str(li[k-1][0])+"\n")

