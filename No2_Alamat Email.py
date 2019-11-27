import re 
print('no2 adam')  
x = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def validasi(email):  
  
    if(re.search(x,email)):  
        print("Email Valid")       
    else:  
        print("Email Invalid")       
if __name__ == '__main__' :  
      
    # email1 = "lintangwisesa@ymail.com"  
    # email2 = "lintang@purwadhika.com"
    # email3 = "lintang123@ironman123.space"
    # email4 = "l/nt*ngw:s=s!@ym~il.com" 
    # email5 = "lintang@purwadhika.community"
    # email6 = "lintang123@ironman123"
    email7 = "lintang@purwadhika.com"
    email8 = "lintangwisesa@ymail.com"
    email9 = "captain@l*nt*ng.id"
      
# validasi(email1) 
# validasi(email2)
# validasi(email3)
# validasi(email4)
# validasi(email5)
# validasi(email6)

validasi(email7)
validasi(email8)
validasi(email9)


