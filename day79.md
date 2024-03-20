question link: https://www.interviewbit.com/problems/loopcmpl/  <br><br>


::Code snippet:: <br>
int a = 0, b = 0; <br>
for (i = 0; i < N; i++) { <br>
  a = a + rand(); <br>
} <br>
for (j = 0; j < M; j++) { <br>
  b = b + rand(); <br>
} <br>
//Assume that rand() is O(1) time, O(1) space function. <br><br>


Question: What is the time, space complexity of following code? <br>
Answer: O(N + M) time, O(1) space
