'''
To find mean,median and mode
mean->The average of the given set of numbers
median->The middle value
mode->The most repeated value
'''
import statistics
def mean_median_mode(list1):
    mean=round(statistics.mean(list1),2)
    median=statistics.median(list1)
    mode=statistics.mode(list1)
    return mean,median,mode
mean,median,mode=mean_median_mode([3,9,5,7,4,3])
print(f"The mean is {mean} , median is {median}, and mode is {mode}")

'''
Output:
The mean is 5.17 , median is 4.5, and mode is 3
'''
