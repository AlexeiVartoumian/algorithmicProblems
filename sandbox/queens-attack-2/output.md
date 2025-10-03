<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>You will be given a square chess board with one queen and a number of obstacles placed on it.  Determine how many squares the queen can attack.  </p>
<p>A <a href="https://en.wikipedia.org/wiki/Queen_%28chess%29">queen</a> is standing on an



![Equation](svg_equations/equation_1.svg) <a href="https://en.wikipedia.org/wiki/Chess">chessboard</a>. The chess board's rows are numbered from 

![Equation](svg_equations/equation_2.svg) to ![Equation](svg_equations/equation_3.svg), going from bottom to top.  Its columns are numbered from ![Equation](svg_equations/equation_4.svg) to ![Equation](svg_equations/equation_5.svg), going from left to right. Each square is referenced by a tuple, ![Equation](svg_equations/equation_6.svg), describing the row, ![Equation](svg_equations/equation_7.svg), and column, ![Equation](svg_equations/equation_8.svg), where the square is located.</p>
<p>The queen is standing at position 

![Equation](svg_equations/equation_9.svg).  In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from ![Equation](svg_equations/equation_10.svg): </p>
<p><img alt="image" src="https://s3.amazonaws.com/hr-challenge-images/0/1485426500-a4039ebb00-chess1.png" title=""/></p>
<p>There are obstacles on the chessboard, each preventing the queen from attacking any square beyond it on that path. For example, an obstacle at location 

![Equation](svg_equations/equation_11.svg) in the diagram above prevents the queen from attacking cells ![Equation](svg_equations/equation_12.svg), ![Equation](svg_equations/equation_13.svg), and ![Equation](svg_equations/equation_14.svg):</p>
<p><img alt="image" src="https://s3.amazonaws.com/hr-challenge-images/0/1485459132-3fdc1f1ca3-chess_4_.png" title=""/></p>
<p>Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at 

![Equation](svg_equations/equation_15.svg).  In the board above, there are ![Equation](svg_equations/equation_16.svg) such squares.</p>
<p><strong>Function Description</strong> </p>
<p>Complete the <em>queensAttack</em> function in the editor below.   </p>
<p>queensAttack has the following parameters: <br/>
- <em>int n:</em> the number of rows and columns in the board <br/>
- <em>nt k:</em> the number of obstacles on the board <br/>
- <em>int r_q:</em> the row number of the queen's position <br/>
- <em>int c_q:</em> the column number of the queen's position <br/>
- <em>int obstacles[k][2]:</em> each element is an array of 

![Equation](svg_equations/equation_17.svg) integers, the row and column of an obstacle  </p>
<p><strong>Returns</strong> <br/>
- <em>int:</em> the number of squares the queen can attack   </p></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The first line contains two space-separated integers 

![Equation](svg_equations/equation_18.svg) and ![Equation](svg_equations/equation_19.svg), the length of the board's sides and the number of obstacles. <br/>
The next line contains two space-separated integers 

![Equation](svg_equations/equation_20.svg) and ![Equation](svg_equations/equation_21.svg), the queen's row and column position. <br/>
Each of the next 

![Equation](svg_equations/equation_22.svg) lines contains two space-separated integers ![Equation](svg_equations/equation_23.svg) and ![Equation](svg_equations/equation_24.svg), the row and column position of ![Equation](svg_equations/equation_25.svg).       </p></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><ul>
<li>

![Equation](svg_equations/equation_26.svg)</li>
<li>

![Equation](svg_equations/equation_27.svg)</li>
<li>A single cell may contain more than one obstacle.</li>
<li>There will never be an obstacle at the position where the queen is located.</li>
</ul>
<p><strong>Subtasks</strong></p>
<p>For 

![Equation](svg_equations/equation_28.svg) of the maximum score: </p>
<ul>
<li>

![Equation](svg_equations/equation_29.svg)</li>
<li>

![Equation](svg_equations/equation_30.svg)</li>
</ul>
<p>For 

![Equation](svg_equations/equation_31.svg) of the maximum score: </p>
<ul>
<li>

![Equation](svg_equations/equation_32.svg)</li>
<li>

![Equation](svg_equations/equation_33.svg)</li>
</ul></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 0</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span></span><span class="err">4 0</span>
<span class="err">4 4</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 0</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span class="err">9</span>
</pre></div>
</div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation 0</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The queen is standing at position 

![Equation](svg_equations/equation_34.svg) on a ![Equation](svg_equations/equation_35.svg) chessboard with no obstacles:</p>
<p><img alt="image" src="https://s3.amazonaws.com/hr-challenge-images/0/1485426553-3064e08638-chess2.png" title=""/></p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 1</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span></span><span class="err">5 3</span>
<span class="err">4 3</span>
<span class="err">5 5</span>
<span class="err">4 2</span>
<span class="err">2 3</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 1</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span class="err">10</span>
</pre></div>
</div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation 1</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The queen is standing at position 

![Equation](svg_equations/equation_36.svg) on a ![Equation](svg_equations/equation_37.svg) chessboard with ![Equation](svg_equations/equation_38.svg) obstacles:</p>
<p><img alt="image" src="https://s3.amazonaws.com/hr-challenge-images/0/1485426870-84a6a0ce97-chess3.png" title=""/></p>
<p>The number of squares she can attack from that position is 

![Equation](svg_equations/equation_39.svg).</p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 2</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span></span><span class="err">1 0</span>
<span class="err">1 1</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 2</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><div class="highlight"><pre><span class="err">0</span>
</pre></div>
</div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation 2</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>Since there is only one square, and the queen is on it, the queen can move 0 squares.</p></div></div></div></div>

