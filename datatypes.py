
def data_type(checkdata_type): 
	
    if checkdata_type is None:
        return 'no value'
       
    if isinstance(checkdata_type, str):
        return len(checkdata_type)
      
    elif isinstance(checkdata_type, bool):
        return checkdata_type
        
    elif isinstance(checkdata_type, int):
    	
        if checkdata_type < 100:
            return "less than 100"
        elif checkdata_type == 100:
            return "equal to 100"
        return "more than 100"
        
    elif type(checkdata_type) == list:
		    if len(checkdata_type) < 3:
			      return None
		    else:
			      return checkdata_type[2]
print(data_type(45))
			  