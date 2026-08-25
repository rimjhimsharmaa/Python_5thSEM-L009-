#wap to take amount in rs and calculate how many 500 are 100 are needed eg 3800  = 7 motes of 500 and 3 notes of 100

am = int(input("enter amount in rs"))
notes_5 = am// 500   # float divi
ram = am % 500        
notes_100 = ram // 100 
print(" 5oo notes needed",notes_5 )
print(" 1oo notes needed",notes_100 )
