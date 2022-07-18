
def filter_data(products,filter_by, value):
  if filter_by=="title":
    return return_filtered_data('Title',products,value) 

  elif filter_by=="category": 
    return return_filtered_data('Category',products,value)   
    

  elif filter_by=="description":   
    return return_filtered_data('Description',products,value) 
   

  elif filter_by=="price":  
    return return_filtered_data('Price',products,value) 
    

def return_filtered_data(key,products,value):
    list_category=list()
    for i in products:
      if value in i.get(key):
        list_category.append(i)
        list_category
    return list_category
    