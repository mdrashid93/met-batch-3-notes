# #find second largest number
# numbers=[10,20,5,8,40]
# numbers.sort()
# print(numbers[-2])

#count vowel in string
# count=0
# vowel=set('aeiou')

# word='beAUTiful'
# for char in word:
#     if char in vowel:
#         count+=1
# print(count)


# text='congraTuLatoN'
# def find_the_lowerupper(sentence):
#     upper=0
#     lower=0
#     for char in text:
#         if char.isupper():
#             upper+=1
#         elif char.islower():
#             lower+=1
#     return lower,upper
# lower,upper=find_the_lowerupper(text)
# print(f"lower :{lower}, upper:{upper}")

#check anagram string
# listen silent
# word='listen'
# words='silent'
# def ana(a,b):
#     return sorted(a)==sorted(b)
# print(ana('a','b'))

#check missing number from a list
# a=[1,2,3,4,6]
# fullrange=set(range(min(a),max(a)+1))
# missing=list(fullrange-set(a))
# print(missing)

# for i in range(1,max(a)+1):
#     if i not in a:
#         print("missing number",i)
# length=len(number)
# print(length) 
        
# to set last
# numbers=[0,1,0,3,12]
# for n in numbers:
#     if n==0:
#         numbers.remove(n)
#         numbers.append(0)
# print(numbers) 

#find duplicate ele in alist   
# numbers=[1,3,4,2,2]
# def findduplicate(a):
#     items=set()
#     for n in numbers:
#         if n in items:
#             return n
#         items.add(n)
# print(findduplicate(numbers))    
           
#sting  palindrom
# word='malyalam'
# rever=word[::-1]
# print(word==rever)   

# num=[1,2,3,3,4,5,5,6,6,7]
# original=set(num)
# print(original)
#----------------------------------------------------------------------------------------
#find the sum of digit in this strings
s='abc12def34gh5'
total=''
temp=0
for ch in s:
    if ch.isdigit():
        # print(ch)
        total+= ch
    else:
        if total !='':
            temp +=int(total)
            total=''

if total:
    temp+=int(total)
print(temp)
        
        
