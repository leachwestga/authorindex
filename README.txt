To update the author index page:

1. navigate to the volume that contains papers that need to be added
2. save that html page with filename latest.html

3. run "python3 addNewAuthorsFromWebsite.py"
4. if happy with output, run "python3 addNewAuthorsFromWebsite.py update"
   this will update the file authorlist.txt

5. run "python3 addNewPapersFromWebsite.py"
6. if happy with output, run "python3 addNewPapersFromWebsite.py update"
   this will update the file uniquepapers.txt

7. run "python3 addNewAssociationsFromWebsite.py"
8. if happy with output, run "python3 addNewAssociationsFromWebsite.py update"
   this will update the file associationtable.txt

9. run "python3 generate_index_page.py"
   this will generate a file called out.html that is the newest author index page

Notes:
  1. don't run any commands with "update" until you are happy with the output
  2. when running these scripts with "update", a backup of the existing file will be created 
     with today's date added to the end.


File Descriptions:

Author Index.html: the last manually-maintained author index page (should be deleted eventually)

README.txt: the file you are reading now

associationtable.txt: list of author-paper pairs

authorlist.txt: list of all authors

uniquepaperlist.txt: list of all papers

There are many files that should probably be deleted; Leach will get around to that eventually. 
