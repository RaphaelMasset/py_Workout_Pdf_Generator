    # Strenght program
    #### Video Demo:  https://youtu.be/F_D2KRARkAw
    #### Description:
    When the program is launched, it asks the user a few simple questions, such as their current weight, height, age and body fat percentage. If this percentage is unknown, 20% is assigned by default. Next, the program will use those 3 datas to calculate the maximum weight that can be reached genetically speaking, as well as the FFMI, which stands for fat free mass index. Then, if the user uses pounds rather than kgs, it will convert the pounds into kgs for this last calculation. For the other data it will use pounds and convert it without problems. After that It will promt the users for his maxium weight on the benche-press, the squat and the dealift for 5 repetitions. Based on that it will estimate the maximum for one signle repetition and it will create a 20 weeks program. The program is composed of 3 warm-up sets and 3 working sets 3 times a week for 3 weeks then an active resting week with only  3 sets 3 times a week. The program is composed with week of high volume low intensity and week of lower volume and higher intensities. It is more effective than linear progression training and could theoretically increase strength by at least 10% on each of the movements at the end of the program it is advisable to restart the program each time the user achieves a major progression (on his maximum squat, bench press and deadlift) to recalculate everything. Finally, all this information is summarized in a PDF created by the program using fpdf2.

    Everything fit in the project.py file. Execpt the logo the will appeared on the top-left corner "logoG.png" of the output pdf. The output pdf is called "Training.pf" each time it will create a new one erasing the previous one, so save it!

    Raphael Masset.
#   p y _ W o r k o u t _ P d f _ G e n e r a t o r  
 