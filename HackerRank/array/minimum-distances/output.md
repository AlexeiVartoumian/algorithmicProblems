<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The distance between two array values is the number of indices between them.  Given



![Equation](svg_equations/equation_1.svg), find the minimum distance between any pair of equal elements in the array. If no such value exists, return ![Equation](svg_equations/equation_2.svg).</p>
<p><strong>Example</strong> <br/>


![Equation](svg_equations/equation_3.svg)</p>
<p>There are two matching pairs of values: 

![Equation](svg_equations/equation_4.svg) and ![Equation](svg_equations/equation_5.svg).  The indices of the ![Equation](svg_equations/equation_6.svg)'s are ![Equation](svg_equations/equation_7.svg) and ![Equation](svg_equations/equation_8.svg), so their distance is ![Equation](svg_equations/equation_9.svg).  The indices of the ![Equation](svg_equations/equation_10.svg)'s are ![Equation](svg_equations/equation_11.svg) and ![Equation](svg_equations/equation_12.svg), so their distance is ![Equation](svg_equations/equation_13.svg).  The minimum distance is ![Equation](svg_equations/equation_14.svg).  </p>
<p><strong>Function Description</strong> </p>
<p>Complete the <em>minimumDistances</em> function in the editor below.  </p>
<p>minimumDistances has the following parameter(s):  </p>
<ul>
<li><em>int a[n]:</em> an array of integers   </li>
</ul>
<p><strong>Returns</strong> </p>
<ul>
<li><em>int:</em> the minimum distance found or 

![Equation](svg_equations/equation_15.svg) if there are no matching elements  </li>
</ul></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The first line contains an integer 

![Equation](svg_equations/equation_16.svg), the size of array ![Equation](svg_equations/equation_17.svg). <br/>
The second line contains 

![Equation](svg_equations/equation_18.svg) space-separated integers ![Equation](svg_equations/equation_19.svg).</p></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><ul>
<li>

![Equation](svg_equations/equation_20.svg) </li>
<li>

![Equation](svg_equations/equation_21.svg) </li>
</ul></div></div></div><div class="challenge_output_format"><div class="msB challenge_output_format_title"><p><strong>Output Format</strong></p></div><div class="msB challenge_output_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>Print a single integer denoting the minimum 

![Equation](svg_equations/equation_22.svg) in ![Equation](svg_equations/equation_23.svg).  If no such value exists, print ![Equation](svg_equations/equation_24.svg).</p>
<p><strong>Sample Input</strong></p>
<pre><code>STDIN           Function
-----           --------
6               arr[] size n = 6
7 1 3 4 1 7     arr = [7, 1, 3, 4, 1, 7]
</code></pre>
<p><strong>Sample Output</strong></p>
<pre><code>3
</code></pre>
<p><strong>Explanation</strong> <br/>
There are two pairs to consider:</p>
<ul>
<li>

![Equation](svg_equations/equation_25.svg) and ![Equation](svg_equations/equation_26.svg) are both ![Equation](svg_equations/equation_27.svg), so ![Equation](svg_equations/equation_28.svg).</li>
<li>

![Equation](svg_equations/equation_29.svg) and ![Equation](svg_equations/equation_30.svg) are both ![Equation](svg_equations/equation_31.svg), so ![Equation](svg_equations/equation_32.svg).</li>
</ul>
<p>The answer is 

![Equation](svg_equations/equation_33.svg).</p></div></div></div></div>

