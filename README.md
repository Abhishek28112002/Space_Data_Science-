# Space_Data_Science- AUTO CLASSIFIER FOR KEPLARS TCE
# Built With

- Python
	- sklearn
	- seaboarn
	- pandas
	- csv
- Node.JS
	- PythonShell
- Express JS
- HTML
- CSS

# Features Used
- tce_period 
- tce_time0bk_err 
- tce_impact_err 
- tce_depth 
- tce_depth_err 
- tce_prad_err 
- tce_steff_err 
- tce_slogg_err                       
 

# Model Used

Using Score probability combination of Random forest  with 100 trees 
and k-nearest neighbour while using the 8 features from the given list 
As this model was performing better than the other models tried SVM,LR,SVC,Neural Network, GCP(slow) in terms of speed and accuracy

# Input File Format

- Should be a CSV file containing values of the features used and in the given order
	- tce_period 
	- tce_time0bk_err 
	- tce_impact_err 
	- tce_depth 
	- tce_depth_err 
	- tce_prad_err 
	- tce_steff_err 
	- tce_slogg_err   



# Output File Format

- The output CSV file having one column with name "CLASS" containing the predicted TCE type of that row.
- Zip file containing the CSV file and features.txt ( count of each class along with features list)

- On WebPage 
	- Button to download zip file
<!-- Link to download to resultant CSV file containing class -->

# For testing accuracy on the tested data
- uncomment the call to accu function at the end of file
<br>


**NOTE - IF UNABLE TO DOWNLOAD OUTPUT FILE IT IS PRESENT IN THE UPLODS FOLDER AS  "python.csv"**
