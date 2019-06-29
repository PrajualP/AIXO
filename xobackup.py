# import random
# import pymysql
# conn=pymysql.connect(host="localhost",user="root",passwd="",db="aixo")
# #Creating a 3x3 Board
# Board=[[[] for i in range(3)]for i in range(3)]
# #Initialise Basic values
# for i in range(3):
#     for j in range(3):
#         Board[i][j]=0
# #Set the Standard Values for input
# standardinput={'7':[0,0],'8':[0,1],'9':[0,2],
#                 '4':[1,0],'5':[1,1],'6':[1,2],
#                 '1':[2,0],'2':[2,1],'3':[2,2]}
# #To keep Track of Values
# trackingMoves=[]
# print("Who Starts First????")
# print("For Computer press: C or User Press: P")
# UserChoice=input()
# print(Board)
# # Board[0][2]=-1
# # Board[1][1]=-1
# # Board[2][0]=-1
# # print(Board)
# #Checking if The game is Completed
# def leftToRightCheck():
#     for i in range(3):
#         additionresult=0
#         for j in range(3):
#             additionresult=additionresult+Board[i][j]
#         if additionresult == 3 or additionresult == -3:
#             print("Finished Game")
#             if additionresult==3:
#                 print("User Won")
#                 # print(trackingMoves[0]['PresentComputerMove'])
#                 mycursor= conn.cursor()
#                 x=trackingMoves[len(trackingMoves)-1]
#                 mycursor.execute("INSERT INTO movestracker(PresentComputerMove,PreviousComputerMove,LatestUserMove,LastbutoneUserMove,Score) VALUES ('%s','%s','%s','%s','%d')" %(str(x['PresentComputerMove']),str(x['PreviousComputerMove']),str(x['LatestUserMove']),str(x['LastbutoneUserMove']),-1))
#                 conn.commit()
#                 conn.close()
#                 print(trackingMoves)
#                 #print(trackingMoves[len(trackingMoves)-1])
#                 exit()
#             else:
#                 # print("CHecked from Left to right")
#                 print("Computer Won")
#                 #Update the table with score 1
#                 for i in trackingMoves:
#                     mycursor= conn.cursor()
#                     mycursor.execute("INSERT INTO movestracker(PresentComputerMove,PreviousComputerMove,LatestUserMove,LastbutoneUserMove,Score) VALUES ('%s','%s','%s','%s','%d')" %(str(i['PresentComputerMove']),str(i['PreviousComputerMove']),str(i['LatestUserMove']),str(i['LastbutoneUserMove']),1))
#                     conn.commit()
#                 conn.close()
#                 exit()
# def topToBottomCheck():
#     for j in range(3):
#         additionresult=0
#         for i in range(3):
#             additionresult=additionresult+Board[i][j]
#         if additionresult == 3 or additionresult == -3:
#             print("Finished Game")
#             if additionresult==3:
#                 print("User Won")
#                 mycursor= conn.cursor()
#                 x=trackingMoves[len(trackingMoves)-1]
#                 mycursor.execute("INSERT INTO movestracker(PresentComputerMove,PreviousComputerMove,LatestUserMove,LastbutoneUserMove,Score) VALUES ('%s','%s','%s','%s','%d')" %(str(x['PresentComputerMove']),str(x['PreviousComputerMove']),str(x['LatestUserMove']),str(x['LastbutoneUserMove']),-1))
#                 conn.commit()
#                 conn.close()
#                 print(trackingMoves)
#                 exit()
#             else:
#                 # print("Checked from top to Bottom")
#                 print("Computer Won")
#                 for i in trackingMoves:
#                     mycursor= conn.cursor()
#                     mycursor.execute("INSERT INTO movestracker(PresentComputerMove,PreviousComputerMove,LatestUserMove,LastbutoneUserMove,Score) VALUES ('%s','%s','%s','%s','%d')" %(i['PresentComputerMove'],i['PreviousComputerMove'],i['LatestUserMove'],i['LastbutoneUserMove'],1))
#                     conn.commit()
#                 conn.close()
#                 exit()

# def diagonalChecks():
#     additionresult=0
#     for i in range(3):
#         additionresult=additionresult+Board[i][i]
#     if additionresult == 3 or additionresult == -3:
#             print("Finished Game")
#             if additionresult==3:
#                 print("User Won")
#                 mycursor= conn.cursor()
#                 x=trackingMoves[len(trackingMoves)-1]
#                 mycursor.execute("INSERT INTO movestracker(PresentComputerMove,PreviousComputerMove,LatestUserMove,LastbutoneUserMove,Score) VALUES ('%s','%s','%s','%s','%d')" %(str(x['PresentComputerMove']),str(x['PreviousComputerMove']),str(x['LatestUserMove']),str(x['LastbutoneUserMove']),-1))
#                 conn.commit()
#                 conn.close()
#                 print(trackingMoves)
#                 exit()
#             else:
#                 print("Computer Won")
#                 for i in trackingMoves:
#                     mycursor= conn.cursor()
#                     mycursor.execute("INSERT INTO movestracker(PresentComputerMove,PreviousComputerMove,LatestUserMove,LastbutoneUserMove,Score) VALUES ('%s','%s','%s','%s','%d')" %(i['PresentComputerMove'],i['PreviousComputerMove'],i['LatestUserMove'],i['LastbutoneUserMove'],1))
#                     conn.commit()
#                 conn.close()
#                 exit()
#     additionresult=0
#     col=2
#     for i in range(3):
#         additionresult=additionresult+Board[i][col]
#         col=col-1
#     if additionresult == 3 or additionresult == -3:
#             print("Finished Game")
#             if additionresult==3:
#                 print("User Won")
#                 mycursor= conn.cursor()
#                 x=trackingMoves[len(trackingMoves)-1]
#                 mycursor.execute("INSERT INTO movestracker(PresentComputerMove,PreviousComputerMove,LatestUserMove,LastbutoneUserMove,Score) VALUES ('%s','%s','%s','%s','%d')" %(str(x['PresentComputerMove']),str(x['PreviousComputerMove']),str(x['LatestUserMove']),str(x['LastbutoneUserMove']),-1))
#                 conn.commit()
#                 conn.close()
#                 print(trackingMoves)
#                 exit()
#             else:
#                 print("Computer Won")
#                 for i in trackingMoves:
#                     mycursor= conn.cursor()
#                     mycursor.execute("INSERT INTO movestracker(PresentComputerMove,PreviousComputerMove,LatestUserMove,LastbutoneUserMove,Score) VALUES ('%s','%s','%s','%s','%d')" %(i['PresentComputerMove'],i['PreviousComputerMove'],i['LatestUserMove'],i['LastbutoneUserMove'],1))
#                     conn.commit()
#                 conn.close() 
#                 exit()

# def drawCheck():
#     count=0
#     for i in range(3):
#         if 0 not in Board[i]:
#             count=count+1
#     print('Count is ',count,end='\n')
#     if count==3:
#         print("Draw Match...")
#         exit()
    
# def isgameCompleted():
#     leftToRightCheck()
#     topToBottomCheck()
#     diagonalChecks()
#     drawCheck()
# previousUserMovelist=[[],[]]
# def UserMove():
#     currentmove=input("Enter your choice")
#     temp=standardinput.get(currentmove)
#     if Board[temp[0]][temp[1]]!=0:
#         print("Move already Performed....")
#         UserMove()
#     else:
#         Board[temp[0]][temp[1]]=1
#         # trackingMoves.append({"PresentUserMove":[temp[0],temp[1]],"PreviousUserMove":previousUserMovelist[0]})
#         previousUserMovelist.remove(previousUserMovelist[0])
#         previousUserMovelist.append([temp[0],temp[1]])
#         for i in range(3):
#             for j in range(3):
#                 if Board[i][j]==1:
#                     print('X',end=' ')
#                 elif Board[i][j]==-1:
#                     print('O',end=' ')
#                 else:
#                     print('-', end=' ')
#             print(end='\n')
#         isgameCompleted()
#         computerMove()

# randomij=[0,1,2]
# previouscomputerMovelist=[[]]#contains the latest and the last before latest move

# def computerMove():
#     print('Computer is Deciding...')
#     #Selecting how it must play
#     #First Priority the user shouldnt win
#     random.shuffle(randomij)
#     i=randomij[0]
#     random.shuffle(randomij)
#     j=randomij[0]
#     mycursor= conn.cursor()
#     mycursor.execute('SELECT `PresentComputerMove`, `PreviousComputerMove`, `LatestUserMove`, `LastbutoneUserMove`,`Score` FROM `movestracker` WHERE `PresentComputerMove`= "%s" AND `PreviousComputerMove`="%s" AND `LatestUserMove`="%s" AND `LastbutoneUserMove`="%s"' %(str([i,j]),str(previouscomputerMovelist[0]),str(previousUserMovelist[1]),str(previousUserMovelist[0])))
#     #mycursor.execute('SELECT `PresentComputerMove`, `PreviousComputerMove`, `LatestUserMove`, `LastbutoneUserMove`,`Score` FROM `movestracker` WHERE `PresentComputerMove`= "%s"' %(str([i,j])))
#     x=mycursor.fetchall()
#     #the moves that should not be performed is temporarily stored in a list(to be done)
#     print(x,end='\n')
#     if Board[i][j] == 0:
#         Board[i][j]=-1
#         trackingMoves.append({"PresentComputerMove":[i,j],"PreviousComputerMove":previouscomputerMovelist[0],"LatestUserMove":previousUserMovelist[1],"LastbutoneUserMove":previousUserMovelist[0]})
#         previouscomputerMovelist.clear()
#         previouscomputerMovelist.append([i,j])
#         for i in range(3):
#             for j in range(3):
#                 if Board[i][j]==1:
#                     print('X',end=' ')
#                 elif Board[i][j]==-1:
#                     print('O',end=' ')
#                 else:
#                     print('-', end=' ')
#             print(end='\n')
#         isgameCompleted()
#         UserMove()
#     else:
#         computerMove()

# if UserChoice == 'P':
#     UserMove()
# elif UserChoice =='C':
#     computerMove() 


# #isgameCompleted()

# import pymysql

# conn=pymysql.connect(host="localhost",user="root",passwd="",db="aixo")
# a='HI'
# mycursor= conn.cursor()
# #mycursor.execute("INSERT INTO movestracker(PresentComputerMove,PreviousComputerMove,LatestUserMove,LastbutoneUserMove,Score) VALUES ('%s','%s','%s','%s','%d')" %(a,a,a,a,1))
# mycursor.execute('SELECT `PresentComputerMove`, `PreviousComputerMove`, `LatestUserMove`, `LastbutoneUserMove`,`Score` FROM `movestracker` WHERE `PresentComputerMove`= "%s" AND `PreviousComputerMove`="%s" AND `LatestUserMove`="%s" AND `LastbutoneUserMove`="%s"' %(a,a,a,a))
# #mycursor.execute("SELECT * FROM movestracker")
# x=mycursor.fetchall()
# print(x[0],end='\n')
# conn.commit()
# conn.close()

a=[{'PresentComputerMove':'[2, 1]'},{'PresentComputerMove':'[3, 2]'}]
for i in a:
    b=int(i['PresentComputerMove'][1])
    c=int(i['PresentComputerMove'][4])
    print(i['PresentComputerMove'])
    print(b+c)
ab=[[2,1],[2,2]]
ab.remove([2,1])
print(ab)