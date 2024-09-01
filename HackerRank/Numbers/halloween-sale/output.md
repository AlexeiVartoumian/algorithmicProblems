<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>You wish to buy video games from the famous online video game store Mist.</p>
<p>Usually, all games are sold at the same price,



![Equation](svg_equations/equation_1.svg) dollars. However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. Specifically, the first game will cost ![Equation](svg_equations/equation_2.svg) dollars, and every subsequent game will cost ![Equation](svg_equations/equation_3.svg) dollars less than the previous one. This continues until the cost becomes less than or equal to ![Equation](svg_equations/equation_4.svg) dollars, after which every game will cost ![Equation](svg_equations/equation_5.svg) dollars. How many games can you buy during the Halloween Sale?</p>
<p><strong>Example</strong> <br/>


![Equation](svg_equations/equation_6.svg) <br/>


![Equation](svg_equations/equation_7.svg) <br/>


![Equation](svg_equations/equation_8.svg) <br/>


![Equation](svg_equations/equation_9.svg). </p>
<p>The following are the costs of the first 

![Equation](svg_equations/equation_10.svg), in order:</p>
<p></p><div class="MathJax_SVG_Display" style="text-align: center;">

![Equation](svg_equations/equation_11.svg)</div><p></p>
<p>Start at 

![Equation](svg_equations/equation_12.svg) units cost, reduce that by ![Equation](svg_equations/equation_13.svg) units each iteration until reaching a minimum possible price, ![Equation](svg_equations/equation_14.svg).  Starting with ![Equation](svg_equations/equation_15.svg) units of currency in your Mist wallet, you can buy 5 games: ![Equation](svg_equations/equation_16.svg).</p>
<p><strong>Function Description</strong> </p>
<p>Complete the <em>howManyGames</em> function in the editor below.  </p>
<p><em>howManyGames</em> has the following parameters:  </p>
<ul>
<li><em>int p:</em> the price of the first game  </li>
<li><em>int d:</em> the discount from the previous game price</li>
<li><em>int m:</em> the minimum cost of a game  </li>
<li><em>int s:</em> the starting budget  </li>
</ul></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The first and only line of input contains four space-separated integers 

![Equation](svg_equations/equation_17.svg), ![Equation](svg_equations/equation_18.svg), ![Equation](svg_equations/equation_19.svg) and ![Equation](svg_equations/equation_20.svg).  </p></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><ul>
<li>

![Equation](svg_equations/equation_21.svg) </li>
<li>

![Equation](svg_equations/equation_22.svg) </li>
<li>

![Equation](svg_equations/equation_23.svg) </li>
</ul></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 0</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span></span><span class="err">20 3 6 80</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 0</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span class="err">6</span>
</pre></div>
</div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation 0</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>Assumptions other than starting funds, 

![Equation](svg_equations/equation_24.svg), match the example in the problem statement.  With a budget of ![Equation](svg_equations/equation_25.svg), you can buy ![Equation](svg_equations/equation_26.svg) games at a cost of ![Equation](svg_equations/equation_27.svg). A ![Equation](svg_equations/equation_28.svg) game for an additional ![Equation](svg_equations/equation_29.svg) units exceeds the budget.    </p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 1</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span></span><span class="err">20 3 6 85</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 1</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span class="err">7</span>
</pre></div>
</div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation 1</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>This is the same as the previous case, except this time the starting budget 

![Equation](svg_equations/equation_30.svg) units of currency. This time, you can buy ![Equation](svg_equations/equation_31.svg) games since they cost ![Equation](svg_equations/equation_32.svg). An additional game at ![Equation](svg_equations/equation_33.svg) units will exceed the budget.  </p></div></div></div></div>

