<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>Given an array of strings of digits, try to find the occurrence of a given pattern of digits. In the grid and pattern arrays, each string represents a row in the grid.  For example, consider the following grid:  </p>
<pre>1234567890  
09<strong>876543</strong>21  
11<strong>111111</strong>11  
11<strong>111111</strong>11  
2222222222  
</pre>
<p>The pattern array is:  </p>
<pre>876543  
111111  
111111
</pre>
<p>The pattern begins at the second row and the third column of the grid and continues in the following two rows.  The pattern is said to be <em>present</em> in the grid.  The return value should be <code>YES</code> or <code>NO</code>, depending on whether the pattern is found.  In this case, return <code>YES</code>.   </p>
<p><strong>Function Description</strong> </p>
<p>Complete the <em>gridSearch</em> function in the editor below.  It should return <code>YES</code> if the pattern exists in the grid, or <code>NO</code> otherwise.  </p>
<p>gridSearch has the following parameter(s):  </p>
<ul>
<li><em>string G[R]:</em> the grid to search </li>
<li><em>string P[r]:</em> the pattern to search for  </li>
</ul></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The first line contains an integer



![Equation](svg_equations/equation_1.svg), the number of test cases.   </p>
<p>Each of the 

![Equation](svg_equations/equation_2.svg) test cases is represented as follows: <br/>
The first line contains two space-separated integers 

![Equation](svg_equations/equation_3.svg) and ![Equation](svg_equations/equation_4.svg), the number of rows in the search grid ![Equation](svg_equations/equation_5.svg) and the length of each row string. <br/>
This is followed by 

![Equation](svg_equations/equation_6.svg) lines, each with a string of ![Equation](svg_equations/equation_7.svg) digits that represent the grid ![Equation](svg_equations/equation_8.svg). <br/>
The following line contains two space-separated integers, 

![Equation](svg_equations/equation_9.svg) and ![Equation](svg_equations/equation_10.svg), the number of rows in the pattern grid ![Equation](svg_equations/equation_11.svg) and the length of each pattern row string. <br/>
This is followed by 

![Equation](svg_equations/equation_12.svg) lines, each with a string of ![Equation](svg_equations/equation_13.svg) digits that represent the pattern grid ![Equation](svg_equations/equation_14.svg).  </p>
<p><strong>Returns</strong> </p>
<ul>
<li><em>string:</em>  either <code>YES</code> or <code>NO</code></li>
</ul></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>

![Equation](svg_equations/equation_15.svg) <br/>


![Equation](svg_equations/equation_16.svg) <br/>


![Equation](svg_equations/equation_17.svg) <br/>


![Equation](svg_equations/equation_18.svg)</p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre><code>2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99
</code></pre></div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre><code>YES
NO
</code></pre></div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The first test in the input file is:  </p>
<pre><code>10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
</code></pre>
<p>The pattern is present in the larger grid as marked in bold below.  </p>
<pre>7283455864  
6731158619  
8988242643  
3830589324  
222<strong>9505</strong>813  
563<strong>3845</strong>374  
647<strong>3530</strong>293  
7053106601  
0834282956  
4607924137  
</pre>
<p>The second test in the input file is:  </p>
<pre>15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99
</pre>
<p>The search pattern is:  </p>
<pre>99
99
</pre>
<p>This pattern is not found in the larger grid.  </p></div></div></div></div>

