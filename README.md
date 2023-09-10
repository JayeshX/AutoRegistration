# AutoRegistration
If you organize events or workshops that require participants to fill out registration forms, this Python application can greatly simplify the process by automating form filling. This automation can save time, reduce manual errors, and streamline the registration experience for both organizers and participants.
You can also use this project as a base for auto google form filling through python


# What is does?
The program fetches data from a excel file. This data is usually redundant. It uses a unique id given to participants (like roll no) to fetch data from this excel and automatically fill a google form.
connect this file to an excel sheet to record the data
the path to the data excel and the google form should be mentioned in the .env file

# Important Steps.
<ul>
<li> Install selenium,fsspec,openpyxl and pandas</li>
<li> Download the latest chromedriver. Extract it</li>
<li> The Paid status field is binary i.e. (1==paid and 0==not paid)</li>
<li> .env file should have the two fields
<ol>
<li> data_file_path => will store the path of the file where the redundant data is stored.</li>
<li> weburl => will store the link to the google form link ensure that the google form is open and does not require the filler to signin </li>
</ol>

</li>
</ul>
