import random
def generate():
     small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
     capital=[ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
     numbers=['0','1','2','3','4','5','6','7','8','9']
     symbol=['!','@','#','$','%','&','*','+']
     password=[]
     num=random.randint(4,8)
     sml=random.randint(2,6)
     cpl=random.randint(2,5)
     sg=random.randint(2,5)
     for i in range(num):
          password.append(random.choice(numbers))
     for i in range(sml):
          password.append(random.choice(small))
     for i in range(cpl):
          password.append(random.choice(capital))
     for i in range(sg):
          password.append(random.choice(symbol))
          random.shuffle(password)

     p=""
     for i in password:
          p+=i
     return p