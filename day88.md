question link: https://www.interviewbit.com/problems/cross-the-bridge/<br><br>

Four people are on this side of the bridge. Everyone has to get across.<br>
Problem is that it’s dark and so you can’t cross the bridge without a flashlight and they only have one flashlight.<br>
Plus the bridge is only big enough for two people to cross at once.<br>
When two people cross the bridge together (sharing the flashlight), they both walk at the slower person’s pace.<br>
The four people walk at different speeds:<br>
- one fella is so fast it only takes him 1 minute to cross the bridge, [a]
- another 2 minutes, [b]
- a third 5 minutes, [c]
- the last it takes 10 minutes to cross the bridge. [d]<br><br>

Question: What is the minimum time required for all 4 to cross the bridge? [Answer is a integer which represents the number of minutes]<br>
Answer: 17<br><br>

::**Solution**::<br>
First, a & b crosses the bridge. (2 mins)<br>
a returns with flashlight. (1 mins)<br>
c & d crosses the bridge. (10 mins)<br>
b returns with flashlight. (2 mins)<br>
Finally, a & b crosses the bridge. (2 mins)<br>
Total time taken = 2+1+10+2+2 = ***17 mins***
