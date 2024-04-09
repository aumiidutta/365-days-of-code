question link: https://www.interviewbit.com/problems/100-people-in-a-circle/<br /><br /><br />


One hundred people are standing in a circle in an order 1 to 100.<br />
No.1 has a sword.<br />
He kills the next person (i.e., no. 2) and gives the sword to the next (i.e., no. 3).<br />
All person does the same until only one survives.<br /><br /><br />

Question: Which number survives at last? [Answer is an integer]<br />
Answer: 73<br /><br /><br />


::Solution::<br />
People numbered from 1 to 100 stand in circle.<br />
People standing at even number position is killed.<br />
People at these position survives:<br />
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99 <br /><br />

99 kills 100 and sword returns to 1.<br />
Then again 1 kills 3, gives sword to 5.<br />
Till 97 kills 99 and hand swords to 1.<br />
People at these position survives:<br />
1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97<br /><br />

1 kills 5 and gives sword to 9.<br />
People at these position survives:<br />
1, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97<br /><br />

Sword is  with 97.<br />
97 kills 1 and gives sword to 9.<br />
People at these position survives:<br />
9, 25, 41, 57, 73, 89<br /><br />

Sword is with 89.<br />
89 kills 97 and gives sword to 9.<br />
People at these position survives:<br />
9, 41, 73<br /><br />

73 kills 89.<br />
Sword is with 9.<br />
9 kills 41 and gives sword to 73.<br />
73 kills 9 and is the last survivor.
