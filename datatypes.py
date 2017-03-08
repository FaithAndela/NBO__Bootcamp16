
def data_type(faith): 
	
    if faith is None:
        return 'no value'
       
    if isinstance(faith, str):
        return len(faith)
      
    elif isinstance(faith, bool):
        return faith
        
    elif isinstance(faith, int):
    	
        if faith < 100:
            return "less than 100"
        elif faith == 100:
            return "equal to 100"
        return "more than 100"
        
    elif type(faith) == list:
		    if len(faith) < 3:
			      return None
		    else:
			      return faith[2]
			  