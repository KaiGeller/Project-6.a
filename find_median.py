#Kai Geller
#GitHub User: KaiGeller
#5/4/2022
#To find the median of a given list of numbers
some_nums= [1,2,3,4,5]
def find_median(some_nums):
    """This function will return the median value of a list"""
    if len(some_nums) % 2 != 0:
        sorted(some_nums)
        print(sorted(some_nums)[len(some_nums)//2])
    if len(some_nums) % 2 == 0:
        sorted(some_nums)
        print((sorted(some_nums)[len(some_nums)//2+1]+sorted(some_nums)[len(some_nums)//2])/2)
