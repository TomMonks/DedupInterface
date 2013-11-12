import string

import sys
from dedupFuncs import *

def run_dedup(fileName):
    print 'Reading records...'
    all_records = read_records(fileName[:-4])

    print 'Excluding duplicate titles...'
    edited_records = unique_titles(all_records, lambda x: x[len(x)-1:][0])
    
    print 'Outputting results...'
    output_records(fileName, 'edit', edited_records.edit)
    output_records(fileName, 'dups', edited_records.duplicates)

    print 'deduplication complete'
    print 'duplicates titles removed: ', len(edited_records.duplicates)
    
    return DedupResultContainer(all_records,  edited_records)
    
def iterate_dedup(fileName, funcContainer):
    """ Dedup by iteration """
    print 'Reading records...'
    all_records = read_records(fileName[:-4], funcContainer.authorFunc)
    total_dups = 0

    print "Running..."
    results = uniquify(all_records)
    
    remaining = 0

    for i in range(1, len(results)):
        output_records(fileName[:-4], 'Iteration' + str(i), results[i].edit)
        print 'it {0} - duplicates: {1}\tremaining: {2}'.format(i, len(results[i].duplicates), len(results[i].edit))
        total_dups += len(results[i].duplicates)

    print 'deduplication complete.'
    print 'duplicates: {0}'.format(total_dups)    

    return results

class DedupResultContainer():
    def __init__(self,  found,  edited):
        """
        Constructor
        """
        self.found = found
        self.edited_records = edited

    def count_found(self):
        return len(self.found)
        
    def count_title_duplicates(self):
        return len(self.edited_records.duplicates)
            
    def count_unique(self):
        return len(self.found) -  len(self.edited_records.duplicates)
        
        
