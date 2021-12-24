from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, num_of_weeks):
        self.name=name
        self.num_of_weeks= num_of_weeks
    #regular method
    def display_user(self):
        print('{} has been subscribed for {} weeks'.format(self.name, self.num_of_weeks))

    #abstract method
    @abstractmethod
    def fee(self):
        pass

class subscription_fee(User):
    fee_zine=15

    def fee(self):
        return self.num_of_weeks * subscription_fee.fee_zine

user1= subscription_fee('Mallory Humphries', 12)
user1.display_user()
fee_owed= user1.fee()
print('Fee is: ', fee_owed)
