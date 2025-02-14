
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

<h2>Structure</h2>

<h3>Main Menu</h3>
<p><strong>USER STORY</strong>: As a User, I want to easily find various options to manage my habits.</p>
<p><strong>IMPLEMENTATION</strong>:</p>
<ul>
    <li>When the program starts, the main menu is displayed with the following options:</li>
    <ul>
        <li>Add a new habit</li>
        <li>Add a successful day to a habit</li>
        <li>Add an unsuccessful day to a habit</li>
        <li>View all habits</li>
        <li>Delete a habit</li>
        <li>View completion percentage for a habit</li>
        <li>View habit progress (start date and success percentage)</li>
        <li>Exit</li>
    </ul>
    <li>The user must input a number corresponding to the desired option. If an invalid choice is made, the user is alerted, and the menu is presented again.</li>
</ul>

<h3>Add a New Habit</h3>
<p><strong>USER STORY</strong>: As a User, I want to add a new habit so that I can start tracking it.</p>
<p><strong>IMPLEMENTATION</strong>:</p>
<ul>
    <li>The user is prompted to enter the name of the new habit and its start date.</li>
    <li>The habit name is checked to ensure it doesn’t already exist.</li>
    <li>The start date is validated to ensure it’s in the correct format (DD/MM/YYYY).</li>
    <li>The habit and its start date are saved to the Google Sheets database.</li>
</ul>

<h3>Track Successful/Unsuccessful Days</h3>
<p><strong>USER STORY</strong>: As a User, I want to add a successful or unsuccessful day to a habit so that I can track my progress.</p>
<p><strong>IMPLEMENTATION</strong>:</p>
<ul>
    <li>The user is prompted to enter the name of the habit they want to update.</li>
    <li>The program checks if the habit exists in the database.</li>
    <li>If the habit exists, the user can add a successful or unsuccessful day.</li>
    <li>The program updates the habit’s success or failure count in the database.</li>
</ul>

<h3>View All Habits</h3>
<p><strong>USER STORY</strong>: As a User, I want to view all my habits so that I can see what I’m tracking.</p>
<p><strong>IMPLEMENTATION</strong>:</p>
<ul>
    <li>The program retrieves all habits from the database and displays them to the user.</li>
    <li>If no habits are found, the user is notified.</li>
</ul>

<h3>Delete a Habit</h3>
<p><strong>USER STORY</strong>: As a User, I want to delete a habit so that I can remove it from my tracker.</p>
<p><strong>IMPLEMENTATION</strong>:</p>
<ul>
    <li>The user is prompted to enter the name of the habit they want to delete.</li>
    <li>The program checks if the habit exists in the database.</li>
    <li>If the habit exists, it is deleted from the database.</li>
    <li>If the habit doesn’t exist, the user is notified.</li>
</ul>

<h3>View Completion Percentage</h3>
<p><strong>USER STORY</strong>: As a User, I want to view the completion percentage of a habit so that I can measure my progress.</p>
<p><strong>IMPLEMENTATION</strong>:</p>
<ul>
    <li>The user is prompted to enter the name of the habit they want to check.</li>
    <li>The program retrieves the habit’s completion percentage from the database and displays it to the user.</li>
    <li>If no data is found, the user is notified.</li>
</ul>

<h3>View Habit Progress</h3>
<p><strong>USER STORY</strong>: As a User, I want to view the progress of a habit, including its start date and success percentage, so that I can evaluate my performance.</p>
<p><strong>IMPLEMENTATION</strong>:</p>
<ul>
    <li>The user is prompted to enter the name of the habit they want to check.</li>
    <li>The program retrieves the habit’s start date and success percentage from the database.</li>
    <li>The program calculates the number of days since the habit’s start date.</li>
    <li>The habit’s progress is displayed to the user, including the start date, days since start, and success percentage.</li>
</ul>

<h3>Exit the Program</h3>
<p><strong>USER STORY</strong>: As a User, I want to exit the program easily when I’m done.</p>
<p><strong>IMPLEMENTATION</strong>:</p>
<ul>
    <li>The user can select the "Exit" option from the main menu to close the program.</li>
</ul>

<h2>Error Handling</h2>
<ul>
    <li><strong>Invalid Input</strong>: The program handles invalid input by alerting the user and prompting them to try again.</li>
    <li><strong>Date Validation</strong>: The program ensures that dates are entered in the correct format (DD/MM/YYYY).</li>
    <li><strong>Habit Existence</strong>: The program checks if a habit exists before performing actions like updating or deleting.</li>
</ul>

<h2>Features Left to Implement</h2>
<ul>
    <li><strong>Habit Streaks</strong>: Track consecutive successful days for a habit.</li>
    <li><strong>Reminders</strong>: Send reminders to users to log their habits.</li>
    <li><strong>Graphical Progress</strong>: Display habit progress in a graphical format (e.g., bar charts).</li>
</ul>

<h2>Logical Flow</h2>
<ol>
    <li>Main Menu</li>
    ![Main Menu](https://github.com/mark0698/Python-Project/blob/main/docs/screenshots/main.png)
    <li>Add a New Habit</li>
    ![Add Habit](docs/screenshots/add.PNG)
    <li>Track Successful/Unsuccessful Days</li>
    ![Update habit](docs/screenshots/updatesuccess.PNG)
    <li>View All Habits</li>
    ![View All](docs/screenshots/gethabit.PNG)
    <li>Delete a Habit</li>
    ![Delete Habit](docs/screenshots/delete.PNG)
    <li>View Completion Percentage</li>
    ![completion percentage](docs/screenshots/percentage.PNG)
    <li>View Habit Progress</li>
    ![level of success](docs/screenshots/successcalc.PNG)
    <li>Exit</li>
    ![exit](docs/screenshots/exit.PNG)
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


</body>
</html>



