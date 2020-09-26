# Judgements of hand location and hand spacing show minimal proprioceptive drift
Alex Rana 1,2
 
Annie A. Butler 1,2 

Simon C. Gandevia 1,3 

Martin E. Héroux 1,2

1 Neuroscience Research Australia, Margaret Ainsworth Building, Sydney, NSW 2031, Australia 

2 School of Medical Sciences, University of New South Wales, Wallace Wurth Building, Sydney, NSW 2052, Australia

3 Prince of Wales Clinical School, University of New South Wales Medicine, Sydney, NSW 2052, Australia

## Notes 

Published in Experimental Brain Research (2020) volume 238 pages 1759-1767

### Data
Data is contained in the `data` folder. Each subject has a dedicated folder that contains 4 files. For example for `sub01`, these files would be:

    sub01.txt
    sub01_data.txt
    sub01_log.txt
    sub01_summary.txt

**sub01.txt**: Simple demographics (id, age, gender, handedness)

**sub01_data.txt**: Raw data from all trials

**sub01_log.txt**: Details of each experimental session and trial

**sub01_summary.txt**: Summary of trial order and associated rulers (if used)

### Code
Code is located in the `code` folder. It was written in Python 3.7.

**Dependencies**

    * matplotlib
    * scipy
    * numpy
    * pandas

**Running code**

run `processing_script.py` to generate and save numerical results in `numerical results folder` and figures 2 and 3 in the `figures` folder.





