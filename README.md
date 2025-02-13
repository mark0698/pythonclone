<h1>Habit Tracker</h1>

<h2>Introduction</h2>
<p>This project is a Habit Tracker designed to help users build and maintain good habits. It allows users to add, track, and manage their habits, view progress, and calculate completion percentages. The application uses Google Sheets as a database to store habit data, making it accessible and easy to use.</p>

<h2>Site Goals</h2>
<ul>
    <li>Provide a simple and intuitive application for users to track their habits.</li>
    <li>Allow users to add, update, and delete habits.</li>
    <li>Enable users to track successful and unsuccessful days for each habit.</li>
    <li>Provide insights into habit progress, including start dates and completion percentages.</li>
</ul>

<h2>Target Audience</h2>
<ul>
    <li>Individuals who want to build and maintain good habits.</li>
    <li>Users who prefer a simple, text-based interface for habit tracking.</li>
</ul>

<h2>User Stories</h2>
<ul>
    <li>As a User, I want to add a new habit so that I can start tracking it.</li>
    <li>As a User, I want to add a successful or unsuccessful day to a habit so that I can track my progress.</li>
    <li>As a User, I want to view all my habits so that I can see what I’m tracking.</li>
    <li>As a User, I want to delete a habit so that I can remove it from my tracker.</li>
    <li>As a User, I want to view the completion percentage of a habit so that I can measure my progress.</li>
    <li>As a User, I want to view the progress of a habit, including its start date and success percentage, so that I can evaluate my performance.</li>
    <li>As a User, I want to exit the program easily when I’m done.</li>
</ul>

<h2>Features Planned</h2>
<ul>
    <li><strong>Add a New Habit</strong>: Users can add a new habit with a start date.</li>
    <li><strong>Track Successful/Unsuccessful Days</strong>: Users can log successful or unsuccessful days for a habit.</li>
    <li><strong>View All Habits</strong>: Users can view a list of all their habits.</li>
    <li><strong>Delete a Habit</strong>: Users can remove a habit from the tracker.</li>
    <li><strong>View Completion Percentage</strong>: Users can see the completion percentage for a specific habit.</li>
    <li><strong>View Habit Progress</strong>: Users can view the start date and success percentage for a habit.</li>
    <li><strong>Exit the Program</strong>: Users can exit the application easily.</li>
</ul>

<h2>Logical Flow</h2>
<ol>
    <li>Main Menu</li>
    <li>Add a New Habit</li>
    <li>Track Successful/Unsuccessful Days</li>
    <li>View All Habits</li>
    <li>Delete a Habit</li>
    <li>View Completion Percentage</li>
    <li>View Habit Progress</li>
    <li>Exit</li>
</ol>

<h2>Database Design</h2>
<p>The application uses Google Sheets as a database with three worksheets:</p>
<ul>
    <li><strong>habits</strong>: Stores the names of all habits.</li>
    <li><strong>completion_data</strong>: Stores the completion percentage, successful days, and unsuccessful days for each habit.</li>
    <li><strong>start_dates</strong>: Stores the start date for each habit.</li>
</ul>

<h2>Technologies</h2>
<ul>
    <li><strong>Python</strong>: The main programming language used to build the application.</li>
    <li><strong>gspread</strong>: A Python library used to interact with Google Sheets.</li>
    <li><strong>Google Sheets</strong>: Used as the database to store habit data.</li>
    <li><strong>colorama</strong>: Used to add colored text to the terminal for better user experience.</li>
</ul>

<h2>Testing</h2>
<ul>
    <li><strong>Functional Testing</strong>: All menu options were tested to ensure they work as expected.</li>
    <li><strong>Input Validation</strong>: Tested with invalid inputs to ensure the program handles errors gracefully.</li>
    <li><strong>Edge Cases</strong>: Tested with edge cases, such as adding a habit with the same name or entering an invalid date format.</li>
</ul>

<h2>Deployment</h2>

<h3>Google Sheets Setup</h3>
<ul>
    <li>Create a Google Sheets document and share it with the service account email.</li>
    <li>Set up the three worksheets: habits, completion_data, and start_dates.</li>
</ul>

<h3>Local Setup</h3>
<ul>
    <li>Clone the repository.</li>
    <li>Install the required Python libraries (gspread, colorama).</li>
    <li>Add the <code>creds.json</code> file for Google Sheets API authentication.</li>
</ul>

<h3>Run the Program</h3>
<ul>
    <li>Execute the Python script to start the habit tracker.</li>
</ul>

<h2>Credits</h2>
<ul>
    <li><strong>Google Sheets API Documentation</strong>: Used to set up and interact with Google Sheets.</li>
    <li><strong>gspread Library Documentation</strong>: Used to implement Google Sheets functionality in Python.</li>
    <li><strong>colorama Library</strong>: Used to enhance the terminal interface with colored text.</li>
</ul>

<h2>Conclusion</h2>
<p>This Habit Tracker is a simple yet powerful tool for individuals looking to build and maintain good habits. With its intuitive interface and robust features, users can easily track their progress and stay motivated to achieve their goals. Future enhancements, such as habit streaks and graphical progress tracking, will make the application even more useful.</p>

</body>
</html>



