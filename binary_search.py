class BinarySearch(list):

    #create a class BinarySearch

    def __init__(self,a,b):

      my_list = []

      my_list.append(b)

      list_length = 1

      while list_length < a:

        my_list.append(my_list[list_length -1] + b)

        list_length +=  1

      super(BinarySearch,self).__init__(my_list)

      self.length = len(my_list)

    def search(self,number):

        count  = 0

        first_number  = 0

        self.length = len(self)

        last_number  = self.length - 1

        middle_point = int((last_number) / 2)

        object_location = {'count':'','index':''}

        while first_number < middle_point:
            
            if (first_number == middle_point) and (self[first_number] > number):

                index = -1 

                object_location["count"] = self.length

                object_location["index"] = index

                return object_location

            
            elif self[first_number] == number:

                index = first_number

                object_location["count"] = count

                object_location["index"] = index

                return object_location

            elif self[last_number] == number:

                index = last_number

                object_location["count"] = count

                object_location["index"] = index

                return object_location

            elif self[middle_point] == number:

                index = middle_point

                object_location["count"] = count

                object_location["index"] = index

                return object_location

            else:

                if self[middle_point] > number:

                    last_number = mid_point - 1

                    first_number = first_number + 1

                    middle_point = (last_number + first_number)//2

                else:

                    first_number = middle_point + 1

                    last_number = last_number - 1

                    middle_point = ((last_number + first_number)//2) + 1

            count += 1

        object_location = {'count':count,'index':-1}    

        return object_location

class BinarySearch(list):

    #create a class BinarySearch

    def __init__(self,a,b):

      my_list = []

      my_list.append(b)

      list_length = 1

      while list_length < a:

        my_list.append(my_list[list_length -1] + b)

        list_length +=  1

      super(BinarySearch,self).__init__(my_list)

      self.length = len(my_list)

    def search(self,number):

        count  = 0

        first_number  = 0

        self.length = len(self)

        last_number  = self.length - 1

        middle_point = int((last_number) / 2)

        object_location = {'count':'','index':''}

        while first_number < middle_point:
            
            if (first_number == middle_point) and (self[first_number] > number):

                index = -1 

                object_location["count"] = self.length

                object_location["index"] = index

                return object_location

            
            elif self[first_number] == number:

                index = first_number

                object_location["count"] = count

                object_location["index"] = index

                return object_location

            elif self[last_number] == number:

                index = last_number

                object_location["count"] = count

                object_location["index"] = index

                return object_location

            elif self[middle_point] == number:

                index = middle_point

                object_location["count"] = count

                object_location["index"] = index

                return object_location

            else:

                if self[middle_point] > number:

                    last_number = mid_point - 1

                    first_number = first_number + 1

                    middle_point = (last_number + first_number)//2

                else:

                    first_number = middle_point + 1

                    last_number = last_number - 1

                    middle_point = ((last_number + first_number)//2) + 1

            count += 1

        object_location = {'count':count,'index':-1}    

        return object_location

