# 344. Reverse String 


## Descriptipn
Write a function that takes a string as input and returns the string reversed.  
Example: Given s = "hello", return "olleh".

## Experience

Try to exchange last char to first.
To do the same as someone else has done, until try length/2 times. 

## Note

for loop can control two variable ,Simultaneously.

```
for(int i= s_length-1,j=0;i>= s_length/2;i--,j++)
```
It is necessary to give **strlen** to **const** value,or it will falt.

## Reference 
[solution1](https://stackoverflow.com/questions/784417/reversing-a-string-in-c)
[solution2](https://hk.saowen.com/a/f901067e92b94e8bad3d35732d4d40f6523e5e2f1ae82238adecfa54673dc2be)
[tips](https://davidwho.me/算法/2016/05/29/LeetCode学习笔记(344)-Reverse-String/)


