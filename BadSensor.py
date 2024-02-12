class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        """
        1 of the sensore have bad values 
        need to find the one with bad values 
        the moment 
        [i:len(sensor)-1] == [i+1:len(sensor2)-1]
        1st sensor is bad 
        """
        
        for i in range(0, len(sensor1)-1):
            if sensor1[i] != sensor2[i]:
                if sensor1[i:len(sensor1)-1] == sensor2[i+1:len(sensor2)]:
                    return 1 if sensor1[i+1:len(sensor1)] != sensor2[i:len(sensor2)-1] else -1
                elif sensor1[i+1:len(sensor1)] == sensor2[i:len(sensor2)-1]:
                    return 2 if sensor1[i:len(sensor1)-1] != sensor2[i+1:len(sensor2)] else -1
                else:
                    return -1
        return -1
