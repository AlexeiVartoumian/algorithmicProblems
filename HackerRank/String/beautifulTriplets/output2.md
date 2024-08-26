<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>Given a sequence of integers



![Equation](svg_equations/equation_1.svg), a triplet ![Equation](svg_equations/equation_2.svg) is beautiful if:</p>
<ul>
<li>

![Equation](svg_equations/equation_3.svg)</li>
<li>

![Equation](svg_equations/equation_4.svg)</li>
</ul>
<p>Given an increasing sequenc of integers and the value of 

![Equation](svg_equations/equation_5.svg), count the number of beautiful triplets in the sequence.</p>
<p><strong>Example</strong> <br/>


![Equation](svg_equations/equation_6.svg) <br/>


![Equation](svg_equations/equation_7.svg) </p>
<p>There are three beautiful triplets, by index: 

![Equation](svg_equations/equation_8.svg).  To test the first triplet, ![Equation](svg_equations/equation_9.svg) and ![Equation](svg_equations/equation_10.svg).  </p>
<p><strong>Function Description</strong> </p>
<p>Complete the <em>beautifulTriplets</em> function in the editor below.     </p>
<p>beautifulTriplets has the following parameters:  </p>
<ul>
<li><em>int d:</em> the value to match   </li>
<li><em>int arr[n]:</em>  the sequence, sorted ascending   </li>
</ul>
<p><strong>Returns</strong> </p>
<ul>
<li><em>int:</em> the number of beautiful triplets   </li>
</ul></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The first line contains 

![Equation](svg_equations/equation_11.svg) space-separated integers, ![Equation](svg_equations/equation_12.svg) and ![Equation](svg_equations/equation_13.svg), the length of the sequence and the beautiful difference. <br/>
    The second line contains 

![Equation](svg_equations/equation_14.svg) space-separated integers ![Equation](svg_equations/equation_15.svg).</p></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><ul>
<li>

![Equation](svg_equations/equation_16.svg)</li>
<li>

![Equation](svg_equations/equation_17.svg)</li>
<li>

![Equation](svg_equations/equation_18.svg)</li>
<li>

![Equation](svg_equations/equation_19.svg)</li>
</ul></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre>STDIN           Function
    -----           --------
    7 3             arr[] size n = 7, d = 3
    1 2 4 5 7 8 10  arr = [1, 2, 4, 5, 7, 8, 10]
    </pre></div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre><code>3
    </code></pre></div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>There are many possible triplets 

![Equation](svg_equations/equation_20.svg), but our only beautiful triplets are ![Equation](svg_equations/equation_21.svg) , ![Equation](svg_equations/equation_22.svg) and ![Equation](svg_equations/equation_23.svg) by value, not index. Please see the equations below:    </p>
<p>

![Equation](svg_equations/equation_24.svg) <br/>


![Equation](svg_equations/equation_25.svg) <br/>


![Equation](svg_equations/equation_26.svg) </p>
<p>Recall that a beautiful triplet satisfies the following equivalence relation: 

![Equation](svg_equations/equation_27.svg) where ![Equation](svg_equations/equation_28.svg). </p></div></div></div></div>

