# Data Cleaning Steps
After webscraping NUFORC.org data using [NUFORCscrape.py](Webscrape/NUFORCscrape.py) the output data (NUFORCraw.csv) requires a lot of preparation before it can be used as an input dataset for GIS or text analysis.

This file acts as a walkthrough for every step in the data cleaning process. I aim to document every spreadsheet formula, code snippet, and the reasoning behind many selection and exclusion decisions made while cleaning the data. Tools used include LibreOffice Spreadsheets (or Microsoft Excel), Python, and GoogleRefine.

Datasets were saved after every step. Cleaned data is not available for download at the present moment.

Data used in this example was gathered on 8-30-2018.  

#
### Step 0: Raw Data
| 'A' |  'B'   | 'C'     |  'D'    |  'E'  |   'F'   |  'G'    |  'H'    |   'I'    |
|-:|:--|:--|:--|:--|:--|:--|:--|:--------|
1|	http://www.nuforc.org/webreports/001/S01001.html |	Occurred : 11/17/1995 22:35|	Reported: 11/20/1995 08:30	| Posted: 3/4/2003 |	Location: Biddeford, ME |	Shape: 	|Duration:2 min.	|Observer had left work about one hour early, and drove home along the Maine Turnpike
1|	http://www.nuforc.org/webreports/001/S01002.html |	Occurred : 11/19/1995 20:45 |	Reported: 11/20/1995 08:53	 | Posted: 3/21/2003 | 	Location: Holton, KS |	Shape: 	 | Duration:15 min.	| Youth w/ friend pursue on Hwy. 16 "triangular thing in sky, w/ yellow, blue, and green" lights. Obj. turned abruptly, flew north.
1	| http://www.nuforc.org/webreports/001/S01003.html |	Occurred : 11/20/1995 06:15	| Reported: 11/20/1995 09:50	| Posted: 3/21/2003	 | Location: Belle Fourche, SD |	Shape: | 	Duration:2 sec.	| MUFON State Dir. relays rpt:  Postal empl. heading W on highway witnesses very large white w/ green tail streak vert. to horizon.

These are the first three rows from the raw output of the [NUFORCscrape.py](Webscrape/NUFORCscrape.py) script. (The header row is included for reference.)

The first two columns, 'A' & 'B' were added while writing every line and they record the batch number and the text's source url.

The rest of the data comes a font html element on each page. Breaks separate each column of data in the original html, so the xpath method in the following line automatically formats each columnar value as a new column when data is written to a .csv.

    sightpath = sightdata.xpath('//tbody/tr/td/font/text()')

The result is a fairly well structured dataset.

The first irregularity to correct has to do with how breaks are interpreted.

| 'A' |  'B'   | 'C'     |  'D'    |  'E'  |   'F'   |  'G'    |  'H'    |   'I'    | 'j' | 'k ' | 'l' | 'm'|
|-:|:--|:--|:--|:--|:--|:--|:--|:--------|:--|:--|:--|:--|
2 |	http://www.nuforc.org/webreports/002/S02549.html	|Occurred : 11/18/1995 21:00  (Entered as : 11-18-1995 21:00)	| Reported: 7/17/1997 11:37	Posted: 3/21/2003	| Location: Ringgold, GA	| Shape: Delta |	Duration:15 min.	 | Summary : On Saturday evening just after dark on November 18, 1995 an arrowhead-shaped ufo was spotted to the east approx. 100 yrds. from Davis Ridge Road hoovering just above tree top level, shinning a beam downward behind the neighbors home. It was motionless and totally silent. It had a light at each corner and the beam came from the center. It was approx. 40' x 25'. After I got out it started moving west at about 5 mph. | We followed until it descended behind a ridge out of sight about a half mile away. The neighbors had cattle out back. -((deleted)) Administrator	I also work as the founder and administrator of ((deleted)) , a satellite and high altitude survey and mapping oriented organization that provides information about new technology for discovering natural resources and minerals, surveying, guides, and related issues  ((URL deleted)) . | I'll take any test to prove the validity of my observation. My family is highly respected in the community as honest and truthful. On one Saturday evening just after dark  | The black, arrowhead-shaped ufo was hoovering silently as it casted a cone-shaped beam into the neighbors back yard. We couldn't see what it was shinning on as it was behind the crest of the high-ground behind the house where the cattle were kept. I got out of the car which was stopped in the middle of the road and looked over the roof at the ufo in astonishment. It was completely silent. It had a light at each corner underneath and the beam came from the bottom center of the craft. | Apparently, we were spotted too, and the ufo turned the beam off. Then it proceed at a low speed (approx. 5 mph) to the west. We were observing the ufo eastward from Davis Ridge Road at first. It came almost directly over us. It was about 80' off of the ground. It continued west and we turned the car around and followed. The road ran north and south though, and b! y the time we were heading west coming off the ridge we saw it descend below a ridge to the west of us. We saw it no more.  | The whole affair lasted about 15 minutes. Everyone in the car saw it. We all had gotten out to see it before we jumped back in to pursue it. I got the impression that the occupants of the craft could care less if we saw it that night, as it seemed to be in no hurry for the most part.																																						
Take line 1549, seen above, as an example: paragraph breaks  - sets of two br tags - create new column for each block of text displayed as a new paragraph. This unnecessarily extends the width of the data structure and splits the text narratives apart.

Recombining the text narratives into one column and normalizing the shape of the data is the first data cleaning step to be taken, otherwise every sort of the data will risk losing parts of sighting narratives.
#
### Step 1: Concatenate sighting text in to one column
     =CONCATENATE(J1," ",K1," ",L1," ",M1," ",N1," ",O1," ",P1," ",Q1," ",R1," ",S1," ",T1," ",U1," ",V1," ",W1," ",X1," ",Y1," ",Z1," ",AA1," ",AB1," ",AC1," ",AD1," ",AE1," ",AF1," ",AG1," ",AH1," ",AI1," ",AJ1," ",AK1," ",AL1," ",AM1," ",AN1," ",AO1," ",AP1," ",AQ1," ",AR1," ",AS1," ",AT1," ",AU1," ",AV1," ",AW1," ",AX1," ",AY1," ",AZ1)

Create a new column in the .csv file to the immediate left of the sighting narrative column (initially column 'I', which becomes 'J' upon the inserting the new row). Using the formula shown above as a spreadsheet formula will concatenate each additional column created by paragraph breaks into the new column ('I'), when the formula is applied to the entire column.

Both LibreOffice and Microsoft Excel add extra rows after applying formulas to entire columns on large datasets. Once the sightings narratives have been concatenated and their text values have been pasted into the same column (as opposed to formula values), copy the rows and columns that contain unique data into a new spreadsheet.

This can be done by selecting the 1st through the final row from column A to I into a new spreadsheet. (Data used for this project totaled 142,000 rows)

#
### Step 2: Add a sighting number to each row

Sighting numbers add unique ID numbers to every row. A simple way to do this is to use the end of the url, stripped of .html.

Add a new column between columns 'A' and 'B'. Use the following formula to populate the column with a new value.

     =RIGHT(C1,12)

Copy the text values produced and paste them into the same column.

Use find and replace to remove '.html' and the leading '/'

 When step two is complete the first three columns of the dataset should look like:

|  |     |      |
|-:|:--|:--|
1|	S01001 |	http://www.nuforc.org/webreports/001/S01001.html |
1|	S01002 |	http://www.nuforc.org/webreports/001/S01002.html |
1|  S01003 |  http://www.nuforc.org/webreports/001/S01003.html

#
### Step 3: Split 'Occurred' column by '('

The 'Occurred' column (formerly column 'C', now 'D') has a parenthetical value included in many of the data (see line 1549, above). The values that start '(Entered as:)' need to be split out of this column and into a new one.

Using 'Text to Columns' runs the risk of overwriting columns that hold existing data with mostly blank columns created by errant delimiters.

GoogleRefine provides the option to split data into a maximum number of columns.

Using the data saved after Step 2, create a project in GoogleRefine. Select the 'Occurred:' column ('Column 4'), next select 'Edit column' and then 'Split into several columns'.

Input '(Entered' as a the value in the separator box, and split into '2' columns at most.

The new column, 'Column 4 2', will contain the raw 'Entered As:' data and 'Column 4 1' will now only contain standardized 'Occurred' data.

#
### Step 4: Remove leading string segments

Every value scraped from the 'font' element is preceded by a value title, like 'Occurred', 'Reported', or 'Location'. Most of the sighting narratives are also preceded by 'Summary'.

These values can also be cleaned in GoogleRefine.

Select a column, such as 'Column 4 1', next select 'Edit cells', and then 'Transform cells'. In the GREL dialog box use the following code snippet:

    replace(value, 'Occurred :', '')

This effectively deletes every occurrence of 'Occurred:' in the column's values. Note that the space following the colon is left intact. Leading spaces allow the column to retain the string data type.

Rename the column based on the string segment being removed. Repeat the replace and rename process for every applicable column. For the sighting narrative column replace 'Summary :'

These edits applied to 116,448 cells in each column for the dataset being used in this project.

When this step has been completed the first three rows of the dataset should resemble:

| 'bNo' |  'sNo'   | 'url'     |  'occurred'    |  'enteredAs'  |   'reported'   |  'posted'    |  'locationRaw'    |   'shape'    |  'duration' | 'sighting' |
|-:|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--------|
1	| S01001 |	http://www.nuforc.org/webreports/001/S01001.html |	 11/17/1995 22:35	|	 | 11/20/1995 08:30	| 3/4/2003|	 Biddeford, ME	| |	2 min.|	Observer had left work about one hour early, and drove home along the Maine Turnpike                                          
1	| S01002	|http://www.nuforc.org/webreports/001/S01002.html	 | 11/19/1995 20:45	|	| 11/20/1995 08:53	| 3/21/2003	 | Holton, KS	| |	15 min.	| Youth w/ friend pursue on Hwy. 16 "triangular thing in sky, w/ yellow, blue, and green" lights. Obj. turned abruptly, flew north.                                          
1	| S01003 |	http://www.nuforc.org/webreports/001/S01003.html	| 11/20/1995 06:15	|| 11/20/1995  09:50	 | 3/21/2003 |	 Belle Fourche, SD	| |	2 sec. |	MUFON State Dir. relays rpt:  Postal empl. heading W on highway witnesses very large white w/ green tail streak vert. to horizon.                                          

#
### Step 5: Check errors, remove empty rows

##### Error Checking

This step can be completed in GoogleRefine or by opening the data in a spreadsheet program.

Begin by sorting the values by the first column, the batch number ('bNo').

This will separate all successfully loaded rows from the rows where an error occurred during the request or writing stage. Errors can be brought to the top of the dataset using a descending sort.

The 38 rows written with errors contain several repeats and international sightings (which are ultimately going to be excluded) contain sightings and should be included with the main dataset. I copied the information for these 20 or so rows manually.

##### Removing empty rows

Sort the data by the sightings column using a descending sort. This will bring empty 'sightings' values to the top. These are also errors and their urls should be checked for content.

Once these sightings have been pasted in place, a few leading spaces need correcting, then it is on to a final descending sort.

At the end of the dataset, sorted in descending order based on the text in the 'sighting' column, there are empty rows which correspond to web pages that respond with 404 errors. These are blank pages, which are ostensibly placeholders for hoax reports that have been removed.

The rows above these empty reports should be copied in their entirety into a new spreadsheet, sorted the 'sNo' column, and saved.

The resulting dataset used in this project, after this step was completed totaled 116,455 rows of UFO sighting narratives.

#
### Step 6: Split by 'locationRaw'

In GoogleRefine, select the 'locationRaw' column and create a column based on it. Name the new column 'locCopy'.

Testing.
![locCopy Test][/img/locCopy.png]
