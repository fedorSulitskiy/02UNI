# 2
class Robot1():
    
    def __init__(self):
        self.batteryCharge = 5.0
    
    def batteryReCharge(self,charge):
        ''''
        Takes in input charge and returns the 
        current battery fullness.
        '''
        self.batteryCharge += charge
        print(f'Battery charge is: {self.batteryCharge}')
    
    def move(self,distance):
        '''
        Takes in the distance required to travel,
        returns the number of steps taken before
        the battery goes flat or until the input
        distance is covered.
        '''
        for i in range(distance):
            self.batteryCharge -= 0.5
            print(f'[{i+1}]', self.batteryCharge)
            if self.batteryCharge <= 0.5:
                print('We are out of juice!')
                break

# 3
import random
class Robot2(Robot1):
    
    def __init__(self):
        Robot1.__init__(self)
    
    def setSaying(self,inpt):
        '''
        Returns a random value from input list of
        availbale sayings
        '''
        return random.choice(inpt)

# 4
import datetime
class CreditCard():
    
    def __init__(self, expiryMonth, expiryYear, firstName, lastName, ccNumber):
        self.expiryMonth = expiryMonth
        self.expiryYear = expiryYear
        self.firstName = firstName
        self.lastName = lastName
        self.ccNumber = ccNumber
        
    def formatExpiryDate(self):
        return f'{self.expiryMonth}/{self.expiryYear}'
    
    def formatFullName(self):
        return f'{self.firstName} {self.lastName}'
    
    def formatCCNumber(self):
        return ' '.join([self.ccNumber[i:i+4] for i in range(0, len(self.ccNumber), 4)])
    
    def isValid(self):
        return datetime.date(int(self.expiryYear), int(self.expiryMonth), 1) > datetime.date.today()
    
    def __str__(self):
        return f'Number: {self.formatCCNumber()} Expiry Date: {self.formatExpiryDate()} Account holder: {self.formatFullName()} Is valid: {self.isValid()}'

# 5
class DNAStrand():
    
    def __init__(self, dna):
        self.dna = dna
    
    def isValidDNA(self):
        dna = self.dna.replace('-', '')
        bases ='ACGT'
        return all(ch in bases for ch in dna)
          
    def complementWC(self):
        watson_dct = {}
        bases = ['A','C','G','T']
        for i in range(len(bases)):
            watson_dct[bases[i]] = bases[-i-1]
        dna = self.dna.replace('-', '')
        complement = ''
        for i in dna:
            complement += watson_dct[i]
        complement = '-'.join(complement)
        return complement
    
    def palindromeWC(self):
        return self.dna[::-1]
        
    def containsSequence(self, seq):
        return seq in self.dna
    
    def __str__(self):
        return self.dna

        

    
    