import data
import figures
import numerical_results

#############
# IMPORT DATA
#############

dat = data.import_data()

#####################################
# GENERATE AND SAVE NUMERICAL RESULTS
#####################################

numerical_results.write_numerical_results(dat)

###########################
# GENERATE AND SAVE FIGURES
###########################

figures.fig2(dat)
figures.fig3(dat)


