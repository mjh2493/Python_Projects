#Parent class
class NYC:
    neighborhood= 'Upper East Side'
    address= ''
    borough= 'Manhattan'
    activity_type= ''
    name=''

    def information(self):
        msg= "\nActivity: {}\nName: {}\nBorough: {}\nNeighborhood: {}\nAddress: {}\n".format(self.activity_type, self.name, self.borough, self.neighborhood, self.address)
        return msg

#child class for restaurant
class Eat(NYC):
    name= 'Barking Dog'
    activity_type= 'Place to Eat'
    address= '123 3rd Ave'
    cuisine= 'Southern Brunch'
    dining_type= 'Indoor and Outdoor'

    def rest_info(self):
        msg= "\nCuisine: {}\nDining Options: {}\n".format(self.cuisine, self.dining_type)
        return msg

#child class for fun activities
class Explore(NYC):
    name='The Metropolitan Museum of Art'
    activity_type= 'Things to Do'
    address='478 5th Ave'
    place_name= 'Museum'
    covid= 'Vaccination and Masks Required'

    def explore_info(self):
        msg= "\nType of Activity: {}\nCOVID policies: {}\n".format(self.place_name, self.covid)
        return msg


if __name__=="__main__":
    eat=Eat()
    print(eat.information())
    print(eat.rest_info())

    explore= Explore()
    print(explore.information())
    print(explore.explore_info())
    
