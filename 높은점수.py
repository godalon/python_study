# ๐จ ์ฌ๊ธฐ๋ ๊ทธ๋๋ก ๐
scores = input("ํ์๋ค์ ์ฑ์ ์ ์๋ ฅ :\n").split()
for n in range(0, len(scores)):
  scores[n] = int(scores[n])
  #์ฑ์  ์๋ ฅ์ ๋ฌธ์์ด๋ก ๋ฐ๊ธฐ ๋๋ฌธ์ ๋ค์ ์ ์๋ก ๋ณํํด์ ๋ฆฌ์คํธ์ ์๋ ฅ
print(scores)
# ๐จ ์ฌ๊ธฐ๋ ๊ทธ๋๋ก ๐

# ์๋์ ์ฝ๋ ์์ฑ ๐
highest_score = 0
lowst_score = 99999
# for n in scores:
#     if(n > highest_score) :
#         highest_score = n
#     if(n < lowst_score) :
#         lowst_score = n
    
# print(f"๊ฐ์ฅ ๋์ ์ ์๋ : {highest_score}")
# print(f"๊ฐ์ฅ ๋ฎ์ ์ ์๋ : {lowst_score}")
    
print(f"๊ฐ์ฅ ๋์ ์ ์๋ : {max(scores)}")
print(f"๊ฐ์ฅ ๋ฎ์ ์ ์๋ : {min(scores)}")
