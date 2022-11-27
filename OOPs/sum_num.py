class SumNum:
   

    def sum_num(arr, k):
        new_arr = []
        stop = False
        for i in arr:
            for j in arr:
                if i + j == k and stop == False:
                    new_arr.append(i)
                    new_arr.append(j)
                    stop = True
                elif len[arr] == 0:
                    return -1
        print(new_arr)      
        return new_arr

if __name__ == "__main__":
    test = [
        {
            "input": {
                "arr1": [10,15,3,7], 
                "k": 17
            },
            "output": [10,7]
        },
        {
            "input": {
                "arr2": [],
                "k": 17
            },
            "output": -1
        }
    ]

    sumNum = SumNum()
    result = sumNum.sum_num(**test["input"]) == test["output"]

    print(result)