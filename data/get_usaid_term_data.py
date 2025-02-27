import pandas as pd
from us_state_to_abbrev import us_state_to_abbrev

sheet_name = 'USAIDTerminatedActivities(NotOfficial)' 
sheet_id = '1Q-WLZkl-q39mCl6GwItuRQxhg6Ote_OOqvp8mcYV3fI' 
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

def get_usaid_term_data():
    usaid_term_data = pd.read_csv(url)

    #Crosswalk state abbreviations
    usaid_term_data['state_abbrev'] = usaid_term_data['Prime State'].str.title().map(us_state_to_abbrev)

    #Create count variable to generate counts of terminations by state 
    usaid_term_data['state_term_count'] = usaid_term_data['state_abbrev'].map(usaid_term_data['state_abbrev'].value_counts())

    #Create sum variable to sum total amount obligated by state
    usaid_term_data['state_oblg_funds'] = usaid_term_data['Obligation'].replace('\$|,', '', regex=True).astype(float).groupby(usaid_term_data['state_abbrev']).transform('sum').apply(lambda x: "${:,.2f}".format(x))
    
    return(usaid_term_data)




