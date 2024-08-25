<img alt="SVG image" height="200" src="svg1.svg" width="300"/>

![Equation](equation.svg)

![Equation](svg_equations/equation_1.svg)

![Equation](svg_equations/equation_2.svg)

<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>A <em>modified Kaprekar number</em> is a positive whole number with a special property.  If you square it, then split the number into two integers and sum those integers, you have the same value you started with.</p>
<p>Consider a positive whole number

![Equation](equation_1.svg) with ![Equation](equation_2.svg) digits.  We square ![Equation](equation_3.svg) to arrive at a number that is either ![Equation](equation_4.svg) digits long or 

![Equation](equation_5.svg) digits long.  Split the string representation of the square into two parts, ![Equation](equation_6.svg) and ![Equation](equation_7.svg).  The right hand part, ![Equation](equation_8.svg) must be ![Equation](equation_9.svg) digits long.  The left is the remaining substring.  Convert those two substrings back to integers, add them and see if you get ![Equation](equation_10.svg).</p>
<p><strong>Example</strong> </p>
<p>

![Equation](equation_11.svg) <br/>
![Equation](equation_12.svg) </p>
<p>First calculate that 

![Equation](equation_13.svg). Split that into two strings and convert them back to integers ![Equation](equation_14.svg) and ![Equation](equation_15.svg).  Test ![Equation](equation_16.svg), so this is not a modified Kaprekar number.  If ![Equation](equation_17.svg), still ![Equation](equation_18.svg), and ![Equation](equation_19.svg).  This gives us ![Equation](equation_20.svg), the original ![Equation](equation_21.svg). </p>
<p><strong>Note:</strong> r may have leading zeros.  </p>
<p>Here's an explanation from Wikipedia about the <strong>ORIGINAL</strong> <a href="https://en.wikipedia.org/wiki/Kaprekar_number">Kaprekar Number</a> (spot the difference!):  </p>
<blockquote>
<p>In mathematics, a Kaprekar number for a given base is a non-negative integer, the representation of whose square in that base can be split into two parts that add up to the original number again. For instance, 45 is a Kaprekar number, because 45² = 2025 and 20+25 = 45.</p>
</blockquote>
<p>Given two positive integers 
![Equation](equation_22.svg) and ![Equation](equation_23.svg) where ![Equation](equation_24.svg) is lower than ![Equation](equation_25.svg), write a program to print the modified Kaprekar numbers in the range between ![Equation](equation_26.svg) and ![Equation](equation_27.svg), inclusive.  If no modified Kaprekar numbers exist in the given range, print <code>INVALID RANGE</code>.  </p>
<p><strong>Function Description</strong> </p>
<p>Complete the <em>kaprekarNumbers</em> function in the editor below.  </p>
<p>kaprekarNumbers has the following parameter(s):  </p>
<ul>
<li><em>int p:</em> the lower limit     </li>
<li><em>int q:</em> the upper limit   </li>
</ul>
<p><strong>Prints</strong> </p>
<p>It should print the list of modified Kaprekar numbers, space-separated on one line and in ascending order.  If no modified Kaprekar numbers exist in the given range, print <code>INVALID RANGE</code>.  No return value is required.  </p></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The first line contains the lower integer limit ![Equation](equation_28.svg). <br/>
The second line contains the upper integer limit ![Equation](equation_29.svg).  </p>
<p><strong>Note</strong>: Your range should be inclusive of the limits.</p></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>![Equation](equation_30.svg) </p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre><code>STDIN   Function
-----   --------
1       p = 1
100     q = 100
</code></pre></div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>1 9 45 55 99  </p></div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>![Equation](equation_31.svg), ![Equation](equation_32.svg), ![Equation](equation_33.svg), ![Equation](equation_34.svg), and ![Equation](equation_35.svg) are the modified Kaprekar Numbers in the given range.</p></div></div></div></div>



Consider a positive whole number
![Equation](svg_equations/equation_1.svg) 


with ![Equation](svg_equations/equation_2.svg) digits.  We square ![Equation](svg_equations/equation_3.svg) to arrive at a number that is either ![Equation](svg_equations/equation_4.svg) digits long or ![Equation](svg_equations/equation_5.svg) digits long.  Split the string representation of the square into two parts, ![Equation](svg_equations/equation_6.svg) and ![Equation](svg_equations/equation_7.svg).  The right hand part, ![Equation](svg_equations/equation_8.svg) must be ![Equation](svg_equations/equation_9.svg) digits long.  The left is the remaining substring.  Convert those two substrings back to integers, add them and see if you get ![Equation](svg_equations/equation_10.svg).
Example
![Equation](svg_equations/equation_11.svg) 
![Equation](svg_equations/equation_12.svg) 
First calculate that ![Equation](svg_equations/equation_13.svg). Split that into two strings and convert them back to integers ![Equation](svg_equations/equation_14.svg) and ![Equation](equation_15.svg).  Test ![Equation](svg_equations/equation_16.svg), so this is not a modified Kaprekar number.  If ![Equation](svg_equations/equation_17.svg), still ![Equation](svg_equations/equation_18.svg), and ![Equation](equation_19.svg).  This gives us ![Equation](equation_20.svg), the original ![Equation](equation_21.svg). </p>
<p><strong>Note:</strong> r may have leading zeros.  </p>