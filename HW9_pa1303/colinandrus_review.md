![plot](andrusplot.png)

Hi Colin,

I've looked at your dataset and your plot and see that its reflects the ratio of accidents caused by drunk driving compared to the total number of vehicular accidents. In terms of color and labels it is very well done but I think there are a couple of things you can change. In your legend it says "Alcohol contributing factor for Vehicle 1" but this may not be fully representative. It would be best to take the sum of alcohol contributing factor for all vehicles in the dataset. Also I'm not sure it was clear why you needed to use a log scale to make the plot. The ratio of values change when you take the log of values. For instance, say the number of accidents caused by drunk driving is 100 and total accidents is 1000 and the ratio is .10 but if using log base 10, 100 becomes 2 and 1000 becomes 3 making the ratio .66 which is clearly not the case. Try plotting the data without taking the logs which would also allow us to see the true number of accidents.

Best,
Prince

# FBB feedback

Hi Prince, good suggestion on the scale, and also on the ambiguity of Vehicle 1. Where you say "ratio" you should say "fraction": it would be ratio if the data were normalized, thus the total number would be 1 and the length of the yellow bar would in fact represent a ratio. Fraction is generally a more vague term, so although what is plotted in both cases is absolute numbers, you can say fraction to indicate that the relative lenght of the bars is proportional. Very good point about the log scale modifying the intended perception! However given the large number plotting in natural scale would make the DUI accidents fraction too small to see (or to see differences in it). What should be done is probably plot the total number of accidents and the fraction due to DUI in two separate plots. Side by side may also work, but the scales would have to be different, so having a scale on the left for the tot number of accident, from 0 to ~50,000 - possibly in log scale, and a scale on the right for the fraction of DUI accidents, the latter would need to go from 0 to ~0.001, given the number

