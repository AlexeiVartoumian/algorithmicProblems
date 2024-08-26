<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>A <em>left rotation</em> operation on an array of size



![Equation](svg_equations/equation_1.svg) shifts each of the array's elements ![Equation](svg_equations/equation_2.svg) unit to the left. Given an integer, ![Equation](svg_equations/equation_3.svg), rotate the array that many steps left and return the result.  </p>
<p><strong>Example</strong> <br/>


![Equation](svg_equations/equation_4.svg) <br/>


![Equation](svg_equations/equation_5.svg) </p>
<p>After 

![Equation](svg_equations/equation_6.svg) rotations, ![Equation](svg_equations/equation_7.svg).</p>
<p><strong>Function Description</strong> </p>
<p>Complete the <em>rotateLeft</em> function in the editor below.  </p>
<p><em>rotateLeft</em> has the following parameters:  </p>
<ul>
<li><em>int d:</em>  the amount to rotate by  </li>
<li><em>int arr[n]:</em> the array to rotate  </li>
</ul>
<p><strong>Returns</strong> </p>
<ul>
<li><em>int[n]:</em> the rotated array</li>
</ul></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The first line contains two space-separated integers that denote 

![Equation](svg_equations/equation_8.svg), the number of integers, and ![Equation](svg_equations/equation_9.svg), the number of left rotations to perform. <br/>
The second line contains 

![Equation](svg_equations/equation_10.svg) space-separated integers that describe ![Equation](svg_equations/equation_11.svg).  </p></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><ul>
<li>

![Equation](svg_equations/equation_12.svg) </li>
<li>

![Equation](svg_equations/equation_13.svg) </li>
<li>

![Equation](svg_equations/equation_14.svg)</li>
</ul></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre><code>5 4
1 2 3 4 5
</code></pre></div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre><code>5 1 2 3 4
</code></pre></div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>To perform 

![Equation](svg_equations/equation_15.svg) left rotations, the array undergoes the following sequence of changes: </p>
<p></p><div class="MathJax_SVG_Display" style="text-align: center;">

![Equation](svg_equations/equation_16.svg)</div><p></p></div></div></div></div>

