import string

import sys
from dedupFuncs import *
from diffFuncs import *

def run_dedup(fileList):
    print 'Reading records...'
    all_records = []
    for fileName in fileList:
        all_records += read_records(fileName[:-4])
        
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
        output_records(fileName[:-4], 'Duplicates' + str(i), results[i].duplicates)
        print 'it {0} - duplicates: {1}\tremaining: {2}'.format(i, len(results[i].duplicates), len(results[i].edit))
        total_dups += len(results[i].duplicates)

    print 'deduplication complete.'
    print 'duplicates: {0}'.format(total_dups)    

    return results

def run_diff(fileName1, fileName2):
    print 'Reading records...'
    
    all_records_f1 = read_records(fileName1[:-4])
    all_records_f2 = read_records(fileName2[:-4])
        
    print 'Creating markers for file 1'
    seen = create_seen_list(all_records_f1, lambda x: x[len(x)-1:][0])

    print 'Differencing...'
    #i could use unqiue_title function if seen was an optional parameter
    edited_records = diff(all_records_f2, seen, lambda x: x[len(x)-1:][0])
    
    print 'Outputting results...'
    output_records(fileName2[:-4], 'diff', edited_records.edit)
    output_records(fileName2[:-4], 'dups', edited_records.duplicates)

    print 'differencing complete'
    print 'unique files found: ', len(edited_records.duplicates)
    
    return DedupResultContainer(all_records_f2,  edited_records)

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
        
        
