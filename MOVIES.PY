movies = {
 'actors':{
 'prabhas':{'knownAs':'Darling', 'awards':{'nandi':1, 'cinemaa':1, 'siima':1},'remuneration':100,
'hits':{'industry':2, 'super':3,'flops':8}, 'age':41, 'height':6.1, 'mStatus':'single','sRate':'35%'},
 'mahesh':{'knownAs':'Prince','awards':{'nandi':8, 'cinemaa':3, 'siima':3},'remuneration':50,
'hits':{'industry':2, 'super':6,'flops':11},'age':46, 'height':6.2, 'mStatus':'married','sRate':'46%'},
 'ramcharan':{'knownAs':'Mega Power Star', 'awards':{'nandi':2, 'cinemaa':1, 'siima':1}, 
'remuneration':70, 'hits':{'industry':3, 'super':1,'flops':5}, 'age':36, 'height':5.9, 'mStatus':'married',
'sRate':'50%'},
 'ntr':{'knownAs':'Jr NTR', 'awards':{'nandi':2, 'cinemaa':5, 'siima':3}, 'remuneration':70,
'hits':{'industry':1, 'super':7,'flops':11}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'40%'},
 'pavan':{'knownAs':'Power Star', 'awards':{'nandi':2, 'cinemaa':2, 'siima':5}, 'hits':{'industry':2, 
'super':7,'flops':16}, 'age':48, 'height':5.9, 'mStatus':'married','sRate':'37%','remuneration':50},
 },
 'actress':{
'tamanna':{'knownAs':'Milky Beauty', 'awards':{'nandi':0, 'cinemaa':1, 'siima':1}, 
'remuneration':10, 'hits':{'industry':1, 'super':7,'flops':11}, 'age':28, 'height':5.9, 'mStatus':'single',
'sRate':'40%'},
 'rashmika':{'knownAs':'Butter Milky Beauty', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2}, 
'remuneration':12,'hits':{'industry':0, 'super':4,'flops':2}, 'age':36, 'height':5.9, 'mStatus':'single',
'sRate':'30%'},
 'saipallavi':{'knownAs': 'Laughing Queen', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2}, 
'remuneration':8, 'hits':{'industry':0, 'super':3,'flops':0}, 'age':28, 'height':5.9,'mStatus':'single',
'sRate':'60%'},
 'samantha':{'knownAs':'Sam', 'awards':{'nandi':2, 'cinemaa':3, 'siima':5},'remuneration':15,
'hits':{'industry':3, 'super':7,'flops':4}, 'age':33, 'height':5.9,'mStatus':'married','sRate':'70%'},
 'kajal':{'knownAs':'Kaj', 'awards':{'nandi':0, 'cinemaa':2, 'siima':2},'remuneration':12,
'hits':{'industry':1, 'super':6,'flops':8}, 'age':35, 'height':5.9, 'mStatus':'married','sRate':'60%'},
 }
}




# 1. Write a program to display all actors names

# for gen in movies:
#     if gen == "actors":
#         for act in movies[gen]:
#             print(act)


# 2. Write a program to display all actress names

# for gen in movies:
#     if gen == "actress":
#         for act in movies[gen]:
#             print(act)


# 3. Who is Darling?

# for gen in movies:
#     for act in movies[gen]:
#         for key in movies[gen][act]:
#             if movies[gen][act][key] == "Darling":
#                 print(act,"is known as Darling")
            


# 4. What are the total number of Nandi Awards won by actors?
# total=0
# for gen in movies:
#     if gen =="actors":
#         for act in movies[gen]:
#             for key in movies[gen][act]:
#                 if key == "awards":
#                     for j,k in movies[gen][act][key].items():
#                         if j == "nandi":
#                             total+=k
# print("Total nandi awards got by the actors are....",total)


# 5. What is the name of Prince?

# for i in movies:
#     for j in movies[i]:
#         for k,l in movies[i][j].items():
#             if l == "Prince":
#                 print(j,k,l)


# 6. What are the total number of awards own by Ram Charan?
# total=0
# for cat in movies:
#     for act in movies[cat]:
#         if act == "ramcharan":
#             for details in movies[cat][act]:
#                 if details=="awards":
#                     for i , j in movies[cat][act][details].items():
#                         total+=j
# print("Ram Charan got",total,"awards",)


# 7. Which actor won more number of Nandi Awards?

# actor=[]
# greater=[]
# for gen in movies:
#     if gen == "actors":
#         for act in movies[gen]:
#             for key in movies[gen][act]:
#                 if key == "awards":
#                     for j,k in movies[gen][act][key].items():
#                         if j == "nandi":
#                             actor.append(act)
#                             greater.append(k)
# maxAw=max(greater)
# for i in range(len(greater)):
#     if greater[i]==maxAw:
#         print(gen,actor[i],"has more number of nandi awards :",maxAw)                            


# 8. What is the success rate of Prince?

# for gen in movies:
#     for act in movies[gen]:
#         for details,ans in movies[gen][act].items():
#             if ans == "Prince":
#                 result=movies[gen][act]["sRate"]
#                 print("Success rate of Prince is",result)


# 9. Which actor and actress has more number of Hits?

# for gen in movies:
#     cou=[]
#     names=[]
#     for act in movies[gen]:
#         for details in movies[gen][act]:
#             if details == "hits":
#                 total=0
#                 for hit,num in movies[gen][act][details].items():
#                     if hit == "industry" or hit == "super":
#                         total+=num
#                 cou.append(total)
#                 names.append(act)
#     maxHits=max(cou)
#     for i in range(len(cou)):
#         if cou[i]==maxHits:
#             print(gen,names[i],"has more number of hits :",maxHits)  


# 10. Who is Milky Beauty?

# for gen in movies:
#     for act in movies[gen]:
#         for details, ans in movies[gen][act].items():
#             if ans=="Milky Beauty":
#                 print(act,"is known as",ans)


# 11. What is the nick name of Rashmika?

# for gen in movies:
#     for act in movies[gen]:
#         if act == "rashmika":
#             nickname=movies[gen][act]["knownAs"]
#             print("The nick name of Rashmika is",nickname)


# 12. What are actress names who did not win at least one Nandi Award?

# for gen in movies:
#     for act in movies[gen]:
#         total=0
#         for details in movies[gen][act]:
#             if details == "awards":
#                 for award,count in movies[gen][act][details].items():
#                     if award == "nandi":
#                         total+=count
#         if total < 1:
#             print(act,"did not win at least one Nandi Award")


# 13. What are the total number of SIIMA awards won by both actors and actress?

# total=0
# for gen in movies:
#     for act in movies[gen]:
#         for details in movies[gen][act]:
#             if details == "awards":
#                 for award,count in movies[gen][act][details].items():
#                     if award == "siima":
#                         total+=count
# print("The total number of SIIMA awards won by both actors and actress are",total)  

# 14. What are the actor and actress names who has more success rate?                      

     
# for gen in movies:
#     result=[]
#     names=[]
#     for act in movies[gen]:
#         for details,ans in movies[gen][act].items():
#             if details == "sRate":
#                 ans=ans[0:len(ans)-1]
#                 ans=int(ans)
#                 result.append(ans)
#                 names.append(act)
#     maxSucces=max(result)
#     for i in range(len(result)):
#         if result[i]==maxSucces:
#             print("The",gen,names[i],"has more success rate",str(maxSucces)+"%") 


#15. What is the age of actor who has more super hit movies?

# total=[]
# age=[]
# names=[]
# for gen in movies:
#     if gen == "actors":    
#         for act in movies[gen]:
#             for details in movies[gen][act]:
#                 if details == "hits" :
#                     for hit,count in movies[gen][act][details].items():
#                         if hit == "super":
#                             total.append(count)
#                             ag= movies[gen][act]["age"]
#                             age.append(ag)
#                             names.append(act)
# moreHit=max(total)
# for i in range (len(total)):
#     if total[i]==moreHit:
#         print("The",gen,names[i],"has",moreHit,"super hits","and his age is",age[i])                        


# 16. What is the actress name who is married?

# for gen in movies:
#     if gen =="actress":    
#         for act in movies[gen]:
#                 for details,ans in movies[gen][act].items():
#                     if details == "mStatus" :
#                          if ans == "married":
#                               print("The",gen,act,"is married")


# 17. Who is the tallest actress?

# tall=[]
# names=[]
# for gen in movies:
#     if gen == "actress":
#         for act in movies[gen]:    
#             for details,ans in movies[gen][act].items():
#                 if details == "height":
#                     tall.append(ans)
#                     names.append(act)
# maxTall=max(tall)
# for i in range(len(tall)):
#     if tall[i]==maxTall:
#         print("The actress",names[i],"is tallest and her height is",tall[i])             


# 18. Who is the Youngest actor and actress?


# for gen in movies:
#     list=[]
#     list1=[]
#     for act in movies[gen]:
#         for details,ag in movies[gen][act].items():
#             if details == "age":
#                 list.append(ag)
#                 list1.append(act)
#     young= min(list)
#     index1=list.index(young)
#     for i in range(len(list)):
#         if list[i]==young:
#             print(list1[i],list[i])


#19. Who are unmarried actress?
            
# for gen in movies:
#     if gen =="actress":    
#         for act in movies[gen]:
#                 for details,ans in movies[gen][act].items():
#                     if details == "mStatus" :
#                          if ans == "single":
#                               print("The",gen,act,"is unmarried")




# 20. Who is smallest actress?

# for gen in movies:
#     list=[]
#     list1=[]
#     if gen =="actress":    
#         for act in movies[gen]:
#                 for details,ans in movies[gen][act].items():
#                      if details == "age":
#                           list.append(act)
#                           list1.append(ans)
# smallest=min(list1)
# for i in range (len(list)):
#      if list1[i]==smallest:
#           print(list[i],list1[i])

# 21. Which actress has more Flops?

# total=[]
# names=[]
# for gen in movies:
#     if gen == "actress":    
#         for act in movies[gen]:
#             for details in movies[gen][act]:
#                 if details == "hits" :
#                     for hit,count in movies[gen][act][details].items():
#                         if hit == "flops":
#                             total.append(count)
#                             names.append(act)
# maxTotal=max(total)
# for i in range(len(total)):
#     if total[i]==maxTotal:
#         print(gen,names[i],"has",total[i],"flops") 

# 22. What is the age of butter milky beauty?

# for gen in movies:
#     for act in movies[gen]:
#         for details,ans in movies[gen][act].items():
#             if details == "knownAs":
#                 if ans == "Butter Milky Beauty":
#                     age = movies[gen][act]["age"]
#                     print("The",gen,act,"is known as butter milky beauty and her age is",age)                       


# 23. What are the total number of flops of all actress?

# for gen in movies:
#     if gen == "actress":    
#         total=0
#         name=''
#         for act in movies[gen]:
#             for details in movies[gen][act]:
#                 if details == "hits" :
#                     for hit,count in movies[gen][act][details].items():
#                         if hit == "flops":
#                             total+=count
# print("The total number of flops of all actress are",total) 


# 24. What are the ages of Sam and Kaj?

# for gen in movies:
#     for act in movies[gen]:
#         for details,ans in movies[gen][act].items():
#             if details == "knownAs":
#                 if ans == "Sam" or ans == "Kaj":
#                     age=movies[gen][act]["age"]
#                     print(ans,"is",age)


# 25. Which actress own highest total number of Awards?

# total=[]
# names=[]
# for gen in movies:
#     if gen == "actress":    
#         for act in movies[gen]:
#             for details in movies[gen][act]:
#                 if details == "awards" :
#                     tot=0
#                     for aw,count in movies[gen][act]["awards"].items():
#                         tot+=count
#                     total.append(tot)
#                     names.append(act)
# maxAw=max(total)
# for i in range(len(total)):
#     if total[i]==maxAw:
#         print("The",gen,names[i],"has highest individual awards :",maxAw)   


# 26. Who is tallest Actor and Actress?

# for gen in movies:
#     hList=[]
#     names=[]
#     for act in movies[gen]:
#         for details,ans in movies[gen][act].items():
#             if details == "height":
#                 hList.append(ans)
#                 names.append(act)
#     maxHi=max(hList)
#     for i in range (len(hList)):
#         if hList[i]==maxHi:
#             print("The",names[i],"tallest",gen,":",maxHi)  


# 27. What are the total number of Industry hits of who has more Success Rate?

# more=[]
# industryHits=[]
# name=[]
# for gen in movies:
#     for act in movies[gen]:
#         for details,ans in movies[gen][act].items():
#             if details == "sRate":
#                 ans=int(ans[0:len(ans)-1])
#                 more.append(ans)
#                 name.append(act)
#                 iHits=movies[gen][act]["hits"]["industry"]
#                 industryHits.append(iHits)
# maxRate=max(more)
# for i in range(len(more)):
#     if more[i]==maxRate:
#         print(name[i],"has more sucess rate",str(maxRate)+"%","and",industryHits[i],"industry hits.")                  

# 28. What is the success rate of youngest actress?


# for gen in movies:
#     list=[]
#     list1=[]
    
#     if gen == "actress":
#         for act in movies[gen]:
#             for details,ans in movies[gen][act].items():
#                 if details == "age":
#                     print(ans)
#                     list.append(act)
#                     list1.append(ans)
# young=min(list1)
# for i in range (len(list)):
#     if list1[i]==young:
#         name=list[i]
#         sRate=movies["actress"][list[i]]["sRate"]
#         print(name,"age =",young,"and success rate =",sRate)

# 29. Who is youngest married actress?

# list=[]
# list1=[]
# print("Married actress")
# for gen in movies:
#     if gen == "actress":
#         for act in movies[gen]:
#             for details,ans in movies[gen][act].items():
#                 if details == "mStatus":
#                     if ans =="married":
#                         list.append(act)
#                         age=movies[gen][act]["age"]
#                         list1.append(age)
# young=min(list1)
# for i in range (len(list)):
#     if list1[i]==young:
#         print(list[i],"youngest married actress") 

# 30. Who is oldest unmarried actor?

# ageList=[]
# name=[]
# for gen in movies:
#     if gen == "actors":
#         for act in movies[gen]:
#             for details,ans in movies[gen][act].items():
#                 if details == "mStatus":
#                     if ans =="single":
#                         years=movies[gen][act]["age"]
#                         ageList.append(years)
#                         name.append(act)

# maxAge=max(ageList)
# for i in range(len(ageList)):
#     if ageList[i]==maxAge:
#         print(name[i],"is oldest actor and his age is :",maxAge)

# 31. Who are the high successful actor and actress?


# for gen in movies:
#     result=[]
#     names=[]
#     for act in movies[gen]:
#         for details,ans in movies[gen][act].items():
#             if details == "sRate":
#                 ans=ans[0:len(ans)-1]
#                 ans=int(ans)
#                 result.append(ans)
#                 names.append(act)
#     high=max(result)
#     for i in range(len(result)):
#         if result[i]==high:
#             print("The",gen,names[i],"has more success rate",str(high)+"%") 


# 32. Totally How many unmarried actors and actress are acting in movies?

# count=0
# for gen in movies:
#     for act in movies[gen]:
#             for details,ans in movies[gen][act].items():
#                 if details == "mStatus" :
#                         if ans == "single":
#                             count+=1
# print(count,"unmarried actors and actress are acting in movies")


# 33. Which actress is having more industry hit movies?
                            
# for gen in movies:
#     high=[]
#     name=[]
#     for act in movies[gen]:
#         for details,ans in movies[gen][act].items():
#             if details=="hits":
#                 for type,hit in movies[gen][act][details].items():
#                      if type=="industry":
#                           high.append(hit)
#                           name.append(act)
#     more=max(high)
#     for i in range(len(high)):
#         if high[i]==more:

#             print("The",gen,name[i],"is having more industry hit movies :",more)                           
                           

# 34. Which actress does not have atleast one industry hit also?            

# names=[]                           
# for gen in movies:
#     if gen == "actress":
#         for act in movies[gen]:
#             for details,ans in movies[gen][act].items():
#                 if details=="hits":
#                     for type,hit in movies[gen][act][details].items():
#                         if type=="industry":
#                             if hit == 0:
#                                 names.append(act)
# print("The actress does not have atleast one industry hit also")
# for name in names:
#     print(name)

# 35. What are the total number of industry and super hits of tallest actress?

# hList=[]
# names=[]
# for gen in movies:
#     if gen == "actress":
#         for act in movies[gen]:
#             for details,height in movies[gen][act].items():
#                 if details=="height":
#                     hList.append(height)
#                     names.append(act)
# print(hList)                    
# tallActress=[]                    
# tallest=max(hList)
# for i in range (len(hList)):
#     if hList[i]==tallest:
#         tallActress.append(names[i])
# for name in tallActress:
#     total=0
#     for type , hit in  movies[gen][name]["hits"].items():
#         if type == "industry" or "super":
#             total+=hit
#     print(gen,name,"has",total,"total number of industry and super hits of tallest actress")               


# 36. Which actress is having lengthiest nick name?

# maxLength=[]
# name=[]                    
# for gen in movies:
#     if gen == "actress":
#         for act in movies[gen]:
#             for details,nick in movies[gen][act].items():
#                 if details=="knownAs":
#                     maxLength.append(len(nick))
#                     name.append(act)
# maxLen=max(maxLength)
# for i in range(len(maxLength)):
#     if maxLength[i]==maxLen:
#         print("Actress",name[i],"is having lengthiest nick name :",maxLen)                    

# 37. Who are the youngest unmarried actor and actress?

# for gen in movies:
#     names=[]
#     ageList=[]
#     for act in movies[gen]:
#             for details,ans in movies[gen][act].items():
#                 if details == "mStatus" :
#                         if ans == "single":
#                               names.append(act)
#                               age = movies[gen][act]["age"]
#                               ageList.append(age)
#     youngest= min(ageList)                    
#     for i in range(len(names)):
#         if ageList[i]==youngest:
#             print(names[i],"is youngest unmarried",gen,"and age is",youngest)
        
            
              
              
                
                
          


# 38. What are the total number of Industry hits and Super Hits of the actress who got more SIIMA awards?

# total=0
# for gen in movies:
#     moreAward=[]
#     names=[]
#     for act in movies[gen]:
#         for details in movies[gen][act]:
#             if details == "awards":
#                 for award,count in movies[gen][act][details].items():
#                     if award == "siima":
#                         moreAward.append(count)
#                         names.append(act)
#     more=max(moreAward)
#     for name in names:
#         total=0
#         for type,hit in movies[gen][name]["hits"].items():
#             if type == "industry" or "super":
#                 total+=1
#         print(gen,name,"has total",total,"Industry hits and Super Hits")   


# 39. What are the ages of Darling and Milky Beauty?

# for gen in movies:
#     for act in movies[gen]:
#         for details,nick in movies[gen][act].items():
#             if details == "knownAs":
#                 if nick == "Darling" or nick =="Milky Beauty":
#                     age= movies[gen][act]["age"]
#                     print(gen,act,details,nick,"and age is",age)


# 40. What are names of actors whose nick name contains star?
# str_obj.find(sub, start, end)

# for gen in movies:
#     for act in movies[gen]:
#         for details,nick in movies[gen][act].items():
#             if details == "knownAs":
#                 if nick.find("Star") != -1 :
#                     print(act,details,nick)


# 41. What is the total remuneration of all actors?

# total=0
# for gen in movies:
#     for act in movies[gen]:
#         for details,amount in movies[gen][act].items():
#             if details == "remuneration":
#                 total+=amount
# print("The total remuneration of all actors :",total)                

# 42. What is the remuneration of an actor who has more flops?

# total=[]
# actor = []
# for gen in movies:
#     if gen == "actors":
#         for act in movies[gen]:
#             for details in movies[gen][act]:
#                 if details == "hits":
#                     for hit,count in movies[gen][act][details].items():
#                         if hit == "flops":
#                             total.append(count)
#                             actor.append(act)
# more= max(total)                    
# for i in range(len(total)):
#     if total[i] == more:
#         remuneration = movies["actors"][actor[i]]["hits"]["flops"]
#         # print(movies["actors"],actor[i],"remuneration :",more)
#         print(actor[i],"remuneration :",more)


# 43. What is the highest remuneration of an unmarried actress?

# actor = []
# rList=[]
# for gen in movies:
#     if gen == "actress":
#         for act in movies[gen]:
#             for details,ans in movies[gen][act].items():
#                 if details == "mStatus":
#                     if ans == "single":
#                         actor.append(act)
#                         remuneration = movies[gen][act]["remuneration"]
#                         rList.append(remuneration)
# maxRem=max(rList)                    
# for i in range(len(actor)):
#     if rList[i]==maxRem:
#         print(gen,actor[i],"has highest remuneration",maxRem,"is an unmarried actress")



# 44. What are the names of actor and actress who has more remuneration?


# for gen in movies:
#     total=[]
#     actor = []
#     for act in movies[gen]:
#         for details in movies[gen][act]:
#             if details == "hits":
#                 for hit,count in movies[gen][act][details].items():
#                     if hit == "flops":
#                         total.append(count)
#                         actor.append(act)
#     more= max(total)                    
#     for i in range(len(total)):
#         if total[i] == more:
#             remuneration = movies[gen][actor[i]]["hits"]["flops"]
#             print(actor[i],"remuneration :",more)


# 45. What is the remuneration of high successful Actress?

# sRate=[]
# names=[]
# for gen in movies:
#     if gen == "actress":
#         for act in movies[gen]:
#             for details,ans in movies[gen][act].items():
#                 if details == "sRate":
#                     ans=ans[0:len(ans)-1]
#                     ans=int(ans)
#                     sRate.append(ans)
#                     names.append(act)
# more=max(sRate)
# for i in range(len(names)):
#     if sRate[i]==more:
#         remuneration = movies[gen][names[i]]["remuneration"]
#         print(gen,names[i],"has success rate of",sRate[i],"and remuneration -",remuneration)                   


# 46. What is the remuneration of actress who has more industry hits?

# actor = []
# hitList=[]
# rList=[]
# for gen in movies:
#     if gen == "actress":
#         for act in movies[gen]:
#             for details in movies[gen][act]:
#                 if details == "hits":
#                     for type,count in movies[gen][act][details].items():
#                         if type == "industry":
#                             actor.append(act)
#                             hitList.append(count)
#                             remuneration = movies[gen][act]["remuneration"]
#                             rList.append(remuneration)
# maxhits=max(rList)                    
# for i in range(len(actor)):
#     if rList[i]==maxhits:
#         print(gen,actor[i],"has more industry hits of",maxhits,"and remuneration :",rList[i])

                        
# 47. What are the ages of an actors whose remuneration is more then 90 crores?

# names=[]
# ageList=[]
# for gen in movies:
#     if gen == "actors":
#         for act in movies[gen]:
#             for details,remuneration in movies[gen][act].items():
#                 if details == "remuneration" or details=="age":
#                     if remuneration > 90 :
#                         names.append(act)
#                         age= movies[gen][act]["age"]
#                         ageList.append(age)

# for i in range (len(names)):
#     print(gen,names[i],"remuneration is more then 90 crores and his age is",ageList[i])                        


# 48. What are the total number of industry hits of both Prince and Butter Milky Beauty?
                            
# for gen in movies:
#     for act in movies[gen]:
#         for details,nick in movies[gen][act].items():
#             if details == "knownAs":
#                 if nick == "Prince" or nick == "Butter Milky Beauty":
#                     iHits= movies[gen][act]["hits"]["industry"]
#                     print(nick,"has",iHits,"industry hits")


# 49. What is the age of Laughing Queen?

# for gen in movies:
#     for act in movies[gen]:
#         for details,nick in movies[gen][act].items():
#             if details == "knownAs":
#                 if nick == "Laughing Queen":
#                     age = movies[gen][act]["age"]
#                     print(act,"is known as",nick,"and age is",age)


# 50. What are the total number of awards won by an actor who has less successful rate?
# names=[]
# sRate=[]
# for gen in movies:
#     if gen == "actors":
#         for act in movies[gen]:
#             for details,ans in movies[gen][act].items():
#                 if details == "sRate":
#                     ans=ans[0:len(ans)-1]
#                     ans=int(ans)
#                     sRate.append(ans)
#                     names.append(act)
# minRate=min(sRate)                   
# for i in range (len(names)):
#     if sRate[i]==minRate:
#         total = movies["actors"][names[i]]["hits"]["industry"] + movies["actors"][names[i]]["hits"]["super"]
#         print(gen,names[i],"has less successful rate of",sRate[i],"and",total,"awards")
        