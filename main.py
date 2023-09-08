def count_batteries_by_health(present_capacities):
  
  #create dictionary to store the count of healthy,exchange and failed batteries
  d={"healthy":0,"exchange":0,"failed":0}
  
  rated_capacity=120                                #assume rated capacity as 120 (given)
  SoH = 0                                           #initilize SoH as 0 
  
  for i in present_capacities:                      #loop through each iteam in present_capacities to calculate SoH
    SoH=100*i/rated_capacity
    
    if 80<SoH and SoH<=100:                         #healthy battery(SoH more than 80%, up to 100%)
      key="healthy"
      d[key]+=1
    elif 65<=SoH and SoH<=80:                       #exchange battery(SoH between 80% and 65%)
      key="exchange"
      d[key]+=1
    else:                                           #failed battery(SoH below 65%)
      key="failed"
      d[key]+=1
      
    SoH=0
      
  return d
  


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
