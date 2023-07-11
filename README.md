
<body>
  <h1>Word to Phonetic Converter</h1>
  <p>This is a Python program that converts a word into its corresponding phonetic representation. It provides two output options: regular and creative (funny).</p>
  <p>The program uses a GUI built with the <code>tkinter</code> library and incorporates a dictionary containing the NATO phonetic alphabet for the regular output option. For the creative (funny) output, a custom dictionary with funny names is used.</p>

  <h2>Prerequisites</h2>
  <ul>
    <li>Python 3</li>
    <li>pandas library</li>
    <li>tkinter library</li>
  </ul>

  <h2>Running the Program</h2>
  <ol>
    <li>Clone or download the repository to your local machine.</li>
    <li>Open a terminal or command prompt and navigate to the directory where you have saved the files.</li>
    <li>Run the following command to execute the program:<br>
      <pre><code>python word_to_phonetic_converter.py</code></pre>
    </li>
    <li>The GUI window will open, allowing you to interact with the program.</li>
    <li>Enter a word in the input field.</li>
    <li>Select the output type by choosing either "Regular" or "Creative" (funny).</li>
    <li>Click the "Convert" button.</li>
    <li>The corresponding phonetic representation of the word will be displayed in the output area.</li>
    <li>Repeat the process to convert additional words.</li>
  </ol>

  <h2>Customization</h2>
  <p>You can customize the program by modifying the following:</p>
  <ul>
    <li><strong>Dictionary:</strong> To change the regular or funny names associated with the letters, modify the <code>funny_name_dict</code> or <code>phonetic_dict</code> dictionaries in the code.</li>
    <li><strong>GUI:</strong> Feel free to customize the GUI appearance, such as the colors, fonts, or layout, by modifying the relevant sections of the code.</li>
    <li><strong>CSV Data:</strong> If you want to change or update the regular phonetic alphabet, replace the data in the <code>nato_phonetic_alphabet.csv</code> file.</li>
  </ul>

  <h2>Notes</h2>
  <ul>
    <li>The regular output option uses the NATO phonetic alphabet, which is commonly used in communication to spell out words letter by letter. For example, the word "Hello" would be represented as "Hotel Echo Lima Lima Oscar" in the regular output.</li>
    <li>The creative (funny) output option replaces each letter with a corresponding funny name. For example, the word "Hello" could be represented as "Hippo Elephant Lollipop Lollipop Octopus" in the creative output.</li>
    <li>The GUI provides a user-friendly interface for entering words and selecting the output type. The program dynamically updates the output based on the user's input.</li>
    <li>The program ensures that invalid or unrecognized characters are displayed as they are without any conversion.</li>
    <li>The program is provided as-is without any warranties or guarantees. Use it at your own risk.</li>
  </ul>
</body>

</html>
